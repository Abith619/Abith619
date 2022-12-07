import numpy as np 
import os
import copy
from math import *
import matplotlib.pyplot as plt
from functools import reduce
# reading in dicom files
import pydicom
# skimage image processing packages
from skimage import measure, morphology
from skimage.morphology import ball, binary_closing
from skimage.measure import label, regionprops
# scipy linear algebra functions 
from scipy.linalg import norm
import scipy.ndimage
# ipywidgets for some interactive plots
from ipywidgets.widgets import * 
import ipywidgets as widgets
# plotly 3D interactive graphs 
import plotly
from plotly.graph_objs import *
import chart_studio.plotly as py

def load_scan(path):
    slices = [pydicom.dcmread(path + '/' + s) for s in               
              os.listdir(path)]
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key = lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] -   
                          slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    for s in slices:
        s.SliceThickness = slice_thickness
    return slices
def get_pixels_hu(scans):
    image = np.stack([s.pixel_array for s in scans])
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    
    # Convert to Hounsfield units (HU)
    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope
    
    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)
        
    image += np.int16(intercept)
    
    return np.array(image, dtype=np.int16)

path = '/home/xmedia/Desktop/pydicom/.dicom/pydicom/pydicom/data/test_files'
patient_dicom = load_scan(path)
patient_pixels = get_pixels_hu(patient_dicom, force=True)
#sanity check
plt.imshow(patient_pixels[326], cmap=plt.cm.bone)

def largest_label_volume(im, bg=-1):
    vals, counts = np.unique(im, return_counts=True)
    counts = counts[vals != bg]
    vals = vals[vals != bg]
    if len(counts) > 0:
        return vals[np.argmax(counts)]
    else:
        return None
def segment_lung_mask(image, fill_lung_structures=True):
    # not actually binary, but 1 and 2. 
    # 0 is treated as background, which we do not want
    binary_image = np.array(image >= -700, dtype=np.int8)+1
    labels = measure.label(binary_image)
 
    # Pick the pixel in the very corner to determine which label is air.
    # Improvement: Pick multiple background labels from around the patient
    # More resistant to “trays” on which the patient lays cutting the air around the person in half
    background_label = labels[0,0,0]
 
    # Fill the air around the person
    binary_image[background_label == labels] = 2
 
    # Method of filling the lung structures (that is superior to 
    # something like morphological closing)
    if fill_lung_structures:
        # For every slice we determine the largest solid structure
        for i, axial_slice in enumerate(binary_image):
            axial_slice = axial_slice - 1
            labeling = measure.label(axial_slice)
            l_max = largest_label_volume(labeling, bg=0)
 
            if l_max is not None: #This slice contains some lung
                binary_image[i][labeling != l_max] = 1
    binary_image -= 1 #Make the image actual binary
    binary_image = 1-binary_image # Invert it, lungs are now 1
 
    # Remove other air pockets inside body
    labels = measure.label(binary_image, background=0)
    l_max = largest_label_volume(labels, bg=0)
    if l_max is not None: # There are air pockets
        binary_image[labels != l_max] = 0
 
    return binary_image

# get masks 
segmented_lungs = segment_lung_mask(patient_pixels,    
                  fill_lung_structures=False)
segmented_lungs_fill = segment_lung_mask(patient_pixels,     
                       fill_lung_structures=True)
internal_structures = segmented_lungs_fill - segmented_lungs
# isolate lung from chest
copied_pixels = copy.deepcopy(patient_pixels)
for i, mask in enumerate(segmented_lungs_fill): 
    get_high_vals = mask == 0
    copied_pixels[i][get_high_vals] = 0
seg_lung_pixels = copied_pixels
# sanity check
plt.imshow(seg_lung_pixels[326], cmap=plt.cm.bone)

class GK:
    def __init__(self, n_clusters=4, max_iter=100, m=2, error=1e-6):
        super().__init__()
        self.u, self.centers, self.f = None, None, None
        self.clusters_count = n_clusters
        self.max_iter = max_iter
        self.m = m
        self.error = error
def fit(self, z):
        N = z.shape[0]
        C = self.clusters_count
        centers = []
        u = np.random.dirichlet(np.ones(N), size=C)
        iteration = 0
        while iteration < self.max_iter:
            u2 = u.copy()
            centers = self.next_centers(z, u)
            f = self._covariance(z, centers, u)
            dist = self._distance(z, centers, f)
            u = self.next_u(dist)
            iteration += 1
            # Stopping rule
            if norm(u - u2) < self.error:
                break
        self.f = f
        self.u = u
        self.centers = centers
        return centers
def gk_segment(img, clusters=5, smooth=False):
    # expand dims of binary image (1 channel in z axis)
    new_img = np.expand_dims(img, axis=2)
    # reshape
    x, y, z = new_img.shape
    new_img = new_img.reshape(x * y, z)
    # segment using GK clustering
    algorithm = GK(n_clusters=clusters)
    cluster_centers = algorithm.fit(new_img)
    output = algorithm.predict(new_img)
    segments = cluster_centers[output].astype(np.int32).reshape(x,    
    y)
    # get cluster that takes up least space (nodules / airway)
    min_label = min_label_volume(segments)
    segments[np.where(segments != min_label)] = 0
    segments[np.where(segments == min_label)] = 1
    return segments

# cluster slices (#324 - #328)
dist = 2
selected_slices = seg_lung_pixels[326-dist:326+(dist+1)]
gk_clustered_imgs = np.array([gk_segment(x) for x in    
                              selected_slices])
# display middle slice (slice #326)
plt.imshow(gk_clustered_imgs[2], cmap=plt.cm.bone)

def plot_3d(image):
    
    # Position the scan upright, 
    # so the head of the patient would be at the top facing the   
    # camera
    p = image.transpose(2,1,0)
    
    verts, faces, _, _ = measure.marching_cubes_lewiner(p)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    # Fancy indexing: `verts[faces]` to generate a collection of    
    # triangles
    mesh = Poly3DCollection(verts[faces], alpha=0.70)
    face_color = [0.45, 0.45, 0.75]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)
    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])
    plt.show()
# run visualization 
plot_3d(internal_structures_mask)

def interactive_3d_plot(segmented_3d, single_color=False):
    
    verts, faces = make_mesh(segmented_3d, fairing='fairing',   
                             regularization='regularization')
    data1 = plotly_trisurf(verts, faces, single_color, 
                           colormap=plt.cm.RdBu, plot_edges=True)
    axis = dict(
    showbackground=True, 
    backgroundcolor="rgb(230, 230,230)",
    gridcolor="rgb(255, 255, 255)",      
    zerolinecolor="rgb(255, 255, 255)",  
    )
    layout = Layout(
             title='3D Interactive',
             width=800,
             height=800,
             scene=Scene(  
             xaxis=XAxis(axis),
             yaxis=YAxis(axis), 
             zaxis=ZAxis(axis), 
            aspectratio=dict(
                x=1,
                y=1,
                z=1
            ),
            )
            )
    
    fig1 = Figure(data=data1, layout=layout)
    return fig1, verts, faces
# create vertices and faces
def make_mesh(image, step_size=1):
    
    # transpose images
    p = image.transpose(2,1,0)
    p = p[:,:,::-1]
    
    # use marching cubes to get verts and faces
    verts, faces, _, _ = measure.marching_cubes_lewiner(p, 
                         step_size=step_size,  
                         allow_degenerate=False)
    return verts, faces
def map_z2color(zval, colormap, vmin, vmax, single_color):
    # green value: 'rgb(0.078, 0.239, 0.133)'
    
    # map the normalized value zval to a corresponding color in the    
    # colormap
    if vmin>vmax:
        raise ValueError('incorrect relation between vmin and vmax')
    if single_color: 
        return 'rgb(0.078, 0.239, 0.133)'
    else:
        # normalized values 
        t = (zval - vmin) / float(vmax - vmin)
        R, G, B, alpha = colormap(t)
        
        return    'rgb('+'{:d}'.format(int(R*255+0.5))+','+'{:d}'.format(int(G*255+0.5))+\
               ','+'{:d}'.format(int(B*255+0.5))+')'
def tri_indices(simplices):
    #simplices is a numpy array defining the simplices of the     
    #triangularization
    #returns the lists of indices i, j, k
    return ([triplet[c] for triplet in simplices] for c in range(3))
def plotly_trisurf(verts, simplices, single_color,   
              colormap='rgb(0.078, 0.239, 0.133)', plot_edges=None):
    #x, y, z are lists of coordinates of the triangle vertices 
    #simplices are the simplices that define the triangularization;
    #simplices  is a numpy array of shape (no_triangles, 3)
    #insert here the  type check for input data
    
    x,y,z = zip(*verts) 
    points3D=np.vstack((x,y,z)).T
    
    # vertices of the surface triangles 
    tri_vertices=map(lambda index: points3D[index], simplices)
    tri_vertices = list(tri_vertices)
    
    # mean values of z-coordinates of triangle vertices
    zmean=[np.mean(tri[:,2]) for tri in tri_vertices]                                            
    min_zmean=np.min(zmean)
    max_zmean=np.max(zmean)  
    facecolor=[map_z2color(zz,  colormap, min_zmean, max_zmean, 
               single_color) for zz in zmean] 
    I,J,K = tri_indices(simplices)
    
    triangles=Mesh3d(x=x,
                     y=y,
                     z=z,
                     facecolor=facecolor, 
                     i=I,
                     j=J,
                     k=K,
                     name=''
                    )
    # the triangle sides are not plotted 
    if plot_edges is None:
        return plotly.graph_objs.Scatter([triangles])
    else:
        #define the lists Xe, Ye, Ze, of x, y, resp z coordinates of   
        #edge end points for each triangle
        #None separates data corresponding to two consecutive    
        #triangles
        lists_coord=[[[T[k%3][c] for k in range(4)]+[ None] for T in 
                       tri_vertices] for c in range(3)]
        Xe, Ye, Ze=[reduce(lambda x,y: x+y, lists_coord[k]) for k in 
                    range(3)]
        
        #define the lines to be plotted
        lines=Scatter3d(x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        line=Line(color= 'rgb(50,50,50)', width=1.5)
               )
        return Data([triangles, lines])
# crop image based on centroid and radius
def crop_image(img, centroid, r=10): 
    img = np.array(img)
    row, column, _ = centroid
    r_min, r_max = int(row - r), int(row + r)
    c_min, c_max = int(column - r), int(column + r)
    cropped = img[r_min:r_max, c_min:c_max]
    return cropped

# crop that specific region in each slice 
centroid = (210, 160, 0)
cropped_region = np.array([crop_image(i, centroid) for i in 
                           gk_clustered_imgs])
# plot it interactively! 
fig, verts, faces = interactive_3d_plot(cropped_region)
py.iplot(fig, filename='region_3d_example')
