#                                                                 Machine Learning ;

#  Clustering
# Libraries = SciKit Learn
# Training the imputer (impute) object with strategy
# Make simulated data regression using plotting , Pre-processing ,
# Minimum,Max Scale using Standard Deviation (standard.scaler)
# Libraries Import: Sklearn.datasets , numpy , matplotlib.pyplot as plt, make_blobs
# plt.scatter ,
# create an array, filter-dataframe.dropna , isNan(x)
# Shuffle Values , Null Values
# Generate dataset to print a matrix : 
print(matrix(runif(6*3), n row=6, n col=3))
# create imputer object: 
impute = SimpleImpute(missing_values=np.nan, Strategy=‘most_frequent’)
impute.fit_transform(x)
# Declare an object 
df = pd.dataframe() # to create pandas dataframe
df = pd.dataframe()

new_observation = [[0.8, 0.8, 0.8, 0.8]]   # create new Observation
model.predict(new_observation)   # predict observation cluster
array([0])
model.cluster_centers_  # View cluster centers

#                                                                                            creating a data-frame
from sklearn import preprocessing
import pandas as pd
rawdata={
    "patient" : ["Rob","Rani","Abith","jose","Michael"], #                                    creating raw data
    "obs" : [1,2,3,1,2],
    "treatment" : [0,1,1,0,1],
    'treatment_score' : ["weak","strong","normal","weak","strong"]
}
pdframe = pd.DataFrame(rawdata,colums=['patient','obs',"treatment","treatment_score"]) # creating DF from raw data
pdframe #                                                                                     display data 
#                                               mapping a number to a column in a table & unique value
# fetch distinct column values, Distinct values = no duplicates
pdframe = pd.DataFrame(rawdata,columns=['patient','obs',"treatment","treatment_score"])
distinct_value = preprocessing.LabelEncoder() # create object
distinct_value.fit(pdframe["treatment_score"]) # load the data
list(distinct_value.classes_) # dtype = object
distinct_value.classes_
distinct_value.transform(pdframe["treatment_score"]) # transform data into values
# o/p = array([2, 1, 0, 2, 1])
# map data with corresponding values
pdframe["treatment_score"] # normal is 0, strong is 1, weak is 2
# transforming the values to the numbers

# map values using mappers



#                                                                  Feature Selection
from sklearn import datasets
from sklearn.feature_selection import VarianceThreshold
iris = datasets.load_iris()
x = iris.data
y = iris.target
thresholder = VarianceThreshold(threshold=.5)
X_threshold = threshold.fit_transform(X)
print("Reduced number of features", X_threshold.shape[1])



# #                                                                                                                        String Manipulations & Functions
#
# # len(s) in string counted with quotes in middle separate with coma or exclude with \
# #  Array = (' ', " ", " ')
# # S = '"Abith"', \t      Raj, \n S / print(S) O/P = Abith Raj
# #  \t = tab    space, \n = next line
# # Slicing the string = print(s[0:-2]) = Abi : -2 = last two Letters is removed                         $ Slicing
# # slicing[1:2] = 1:2-1 = 2 arguments = starting, ending -1, stepping value

# # Concatenation = combining two statements : s1 = "Abith" 'Raj' / s1 = ("Abith",'Raj')                $ Concatenation
# # / s2 = "-' / print(s2.join(s1)),
# # Stepping or Stepper : stepping[1:2] = 3 arguments = starting, ending -1, stepping value
s1 = "Abith"
s2 = 'Raj'
sum = s1 + s2
print(sum)
# # Finding letters or values in string = 
print(s1.find(s2))
# # Finding in Reverse = 
print(s1.rfind(s2))
if s1.startswith(s2):
    if s1.endswith(s2):
#
if s1.islower():
    if s1.upper():
#
print(s1.title()) , print(s1.swaps())
print(s1.swaps().title().upper().lower())
#                                                                                                               Advanced Functions in string
# # print(s1,centre(15)), print(s1.ljust(15)), print(s1.rjust(15)), ljust = left justification
# # to Check = if s1.isalpha():, if s1.isalnum():, if s1.isspace():, alpha = alphabet
#                                                                                                                     LDA = Linear Discriminant Analysis (LDA)
# Find the best set of basic vectors for projecting the Data points

# "Form the Projection such that the variability across the different classes is maximized, while the variability within each class is minimised"
#
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = LinearDiscriminantAnalysis()
clf.fit(X, Y)
LinearDiscriminantAnalysis()
print(clf.predict(clf.predict([[-0.8, -1]])
Methods = decision_function(X), fit(X,y),
#                                                                                                                                Iris Dataset
load iris.dataset
sepal Length & Width, petal Length & Width
x = iris.data, y = iris.target
from iris load setosa
iris.setosa = to Find the category
Supervised Learning
K-means, DBSCAN = Cluster Models
# non-Supervised Learning = Support Vector Classifier = no Output
#                                                            Methods
# Collect the Data
# Process the Data => Row-Wise processing (pre-processing)
# Feature Engineering => Column-Wise Filtration
# Model Evaluation
# Model Selection
# Algorithm Implementation & Prediction = Final ML Model
#                                                                                                                                Algorithm Implementation
#                                                                   # Load Libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
#                                                                 Load Data
iris = datasets.load_iris()
X = iris.data
Y = iris.target
# (eg) import numpy as np
from sklearn import decomposition, datasets
from sklearn.preprocessing import StandardScaler
dataset = datasets.load_breast_cancer()
dataset '
#                                                                                                                               Standarize feautures
StandardScaler = Converting the data into Scaler Standard
scaler = StandardScaler()
X_std = scaler.fit_transform(x)
#                                                         Create K-mean object
clt = KMeans(n_Clusters=3, random_state=0, n_jobs=-1)
#                                                        Create new Observation
new_observation = [[0.8], 0.9, 0.7, 0.9]
#                                                        Predict a Observation Cluster
model.predict(new_observation)
#                                                        View Cluster Centers
model.cluster_centers_
 #                         Converting into scaler standard
scaler = standardScaler()
X_std = scaler.fit_transform(X)

clt = KMeans(n_Clusters=3, random_state=0, n_jobs=-1) # (n_jobs=-1) => unlimited
model = clt.fit_transform(X_std)
n_Clusters=3 => number of clusters, random_state=0 => data processing in Random Order, n_jobs=-1 => Threading => Indicates Unlimited
#
#                                                                                                                                               DBSCAN
clt = DBSCAN(n_jobs=-1)
#                                             Train Model
model = clt.fit(X_std)
#                                         Create new Observation
new_observation = [[5.1, 3.5, 1.4, 0.3]]
#                                         predict Observation Cluster
model.fit_predict(new_observation)
model.labels_
#                                                                                                                        $ sample (PCA)
import numpy as np
from sklearn import decomposition, datasets
dataset = dataset.load_breast_cancer()
X = dataset.data                                  # Fetch the data & store in variable X
X.shape                                           # Data with 569 rows and 30 columns
sc = StandardScaler()
X_std = sc.fit_transform(X)
pca = decomposition.PCA(n_components=2)           # Create PCA decomposition Algorithm
X_std_pca = pca.fit_transform(X_std)              # fit & Transform with PCA decomposition Algorithm
X_std_pca.shape # (569, 2)
X_std_pca
X.shape
pca = decomposition.PCA(n_components=2)
X_pca = pca.fit_transform(X)                # pca Algorithm
X_pca.shape                                                # Final Transformed Data
"""
#                                                                                        $   Without StandardScaler
"""
import numpy as np
from sklearn import decomposition, datasets
dataset = dataset.load_breast_cancer()
X = dataset.data                                  # Fetch the data & store in variable X
X.shape
pca = decomposition.PCA(n_components=2)           # Create PCA decomposition Algorithm
X_std_pca = pca.fit_transform(X_std)              # fit & Transform with PCA decomposition Algorithm
X_pca.shape 
#                                                                                                                              $ CHI Square
# To use X square for feature selection, To process clear data in using Decimal & negative values
# Squaring the data will give more rounded values to finalise
# calculate X square between each feature & Target
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
X = X.astype(int)
chi2_algorithm = SelectKBest(chi2, k=2)
X_Output = chi2_algorithm.fit_transform(x, y)
print("Original number of features:", X.shape[1])
print("Reduced number of features:",X_Output.shape[1])
#                                                    Load the Iris flower dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
X = X.astype(int)
chi2_algorithm = SelectKBest(chi2, k=2)
X_Output = chi2_algorithm.fit_transform(x, y)
print("Reduced number of features", X_Output.shape[1])
#                                                                                                                                 Non-Supervised Learning
#                                                                                           Clustering - KMeans
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X = iris.data
Y = iris.target
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
clt = KMeans()

# 



