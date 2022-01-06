#                                                                 Machine Learning ;

#  Clustering
# Libraries = SciKit Learn
# Training the imputer (impute) object with strategy
# Make simulated data regression using plotting , Pre-processing ,
# Minimum,Max Scale using Standard Deviation (standard.scaler)
# Libraries Import: Sklearn.datasets , numpy , matplotlib.pyplot as plt, make_blobs
# plot.scatter
# create an array, filter-dataframe.dropna , isNan(x)
# Shuffle Values , Null Values
# Generate dataset to print a matrix : 
from pandas.core.frame import DataFrame

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
#                                            map values using mappers, (specific_values)
myscale = {
    'strong' : 6,
    'weak' : 1, # raw data
    'normal' : 9
}
pdframe['myscale'] = pdframe['treatment_score'].replace(myscale) # replacing a value in a column
pdframe

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
iris_df = pd.DataFrame(iris, columns =iris.feature_names )
iris_df['sepal length (cm)']
iris_df
# iris.setosa = to Find the category
# Supervised Learning
# K-means, DBSCAN = Cluster Models
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
#                                                                                                                                 Un-Supervised Learning
# models itself find the hidden patterns and insights from the given data
# cannot be directly applied to a regression or classification problem because unlike supervised learning
# find the underlying structure of dataset, group that data according to similarities, and represent that dataset in a compressed format
# clustering = svd, pca, k-means 
# Assocation = Association Rule Mining or Market basket analysis
# Assocation analysis = Apriori, fp-growth,Eclat Association mining identifies sets of items which often occur together in your dataset
# to analyze large dataset to find patterns 
# Algorithms = k-means clustering, Decision tree, KNN (k-nearest neighbors), Hierarchal clustering, Anomaly detection,
# Neural Networks, Principle Component Analysis, Independent Component Analysis, Apriori algorithm, Singular value decomposition
# finds the hidden patterns in data.

#                                                                                           Clustering - KMeans
# 
# hidden Markow Model
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X = iris.data
Y = iris.target
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
clt = KMeans()

#                                                                                           Supervised Learning
# Datasets, training_sets, Labels, Annotations
# Classification, Regression
# Data + Algorithm = Predict Model
# Algorithms
# Regression = Linear, Polynomial
# Decision Tree , Random forest, 
# Classification = knn, trees, svm, nalve-bayes, Logistic Regression
# The model will identify the fruit and predict the output using a suitable algorithm.
# various algorithms such as Linear Regression, Logistic Regression,
# Support Vector Machine, Multi-class Classification, Decision tree, Bayesian Logic
Y=f(X)

#                                                                                                                 Regression
# Linear Regression, Logistic Regression, Polynomial Regression, Support Vector Regression,Decision Tree Regression
# Random Forest Regression, Ridge Regression, Lisso Regression


#                                                                                                              Data preprocessing
# Reader, 
# Splitter = partitioning data into training & performs Sreatification
# Loader = Loads images , Transformer = adjusting or rezize, crop
# augumenter to increase the training set additional images are synthesized by randomly augmenting (flipping, rotating, …) images
# Batcher & Network: GPU-based machine learning demands that image and label data are grouped in mini-batches 
# via a Batcher before passed on to the Network for training or inference
# Logger = employed to write training losses or accuracies to a log file
"""Importing datasets = import csv file using Spyder->variable explorer
Finding Missing Data
Encoding Categorical Data
Splitting dataset into training and test set
Feature scaling"""
data_set= pd.read_csv('Dataset.csv') # to read dataset
#                                              Extracting independent variables
iloc[ ] #                              method of Pandas library.
x= data_set.iloc[:,:-1].values
#                                              Extracting dependent variable
y= data_set.iloc[:,3].values
#                                                                                     Handling Missing data
# deleting the particular row
# calculating the mean
#                             handling missing data (Replacing missing data with the mean value)  
from sklearn.preprocessing import Imputer  
imputer= Imputer(missing_values ='NaN', strategy='mean', axis = 0)  
#                                              Fitting imputer object to the independent variables x.   
imputerimputer= imputer.fit(x[:, 1:3])  
#                                                 Replacing missing data with the calculated mean value  
x[:, 1:3]= imputer.transform(x[:, 1:3])

#                                                                                     Encoding Categorical data
# (eg.Country, and Purchased)
#                                          For Country variable
from sklearn.preprocessing import LabelEncoder  
label_encoder_x= LabelEncoder()  # imported LabelEncoder class of sklearn library
x[:, 0]= label_encoder_x.fit_transform(x[:, 0])
#                                              Dummy Variables
# number of columns equal to the number of categories.
# OneHotEncoder class of preprocessing library
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
label_encoder_x= LabelEncoder()  
x[:, 0]= label_encoder_x.fit_transform(x[:, 0])  
#                                                      Encoding for dummy variables  
onehot_encoder= OneHotEncoder(categorical_features= [0])    
x= onehot_encoder.fit_transform(x).toarray()
#                                                         For Purchased Variable
# purchased variable has only two categories yes or no
# not using OneHotEncoder class
labelencoder_y= LabelEncoder()  
y= labelencoder_y.fit_transform(y)
# Splitting the Dataset into the Training set and Test set
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)
#                                                                                          Feature Scaling
# to standardize the independent variables of the dataset in a specific range
# our variables in the same range and in the same scale so that no any variable dominate the other variable.
Euclidean distance between A and B = root value of (x2-x1)2+(y2-y1)2
# two ways to perform feature scaling
# Standardization, Normalization
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)

#                                                                           ciphertext
# converts the plaintext to ciphertext and ciphertext to plain text
pip install simple-crypt
from simplecrypt import encrypt, decrypt
message = "Hello!! Welcome to AIM!!"
ciphercode = encrypt('AIM', message)
print(ciphercode)
# call the decrypt function and decode the original message from this ciphertext
original = decrypt('AIM', ciphercode)
print(original)
#                                                   encryption and decrypting the files
class Encryptor():
    def key_create(self):
        key = Fernet.generate_key()
        return key
    def key_write(self, key, key_name):
with open(key_name, 'wb') as mykey:
    mykey.write(key)
def key_load(self, key_name):
    with open(key_name, 'rb') as mykey:
        key = mykey.read()
        return key
def file_encrypt(self, key, original_file, encrypted_file):
    f = Fernet(key)
with open(original_file, 'rb') as file:
    original = file.read()
    encrypted = f.encrypt(original)
with open (encrypted_file, 'wb') as file:
    file.write(encrypted)
def file_decrypt(self, key, encrypted_file, decrypted_file):
     f = Fernet(key)
with open(encrypted_file, 'rb') as file:
    encrypted = file.read()
    decrypted = f.decrypt(encrypted)
with open(decrypted_file, 'wb') as file:
    file.write(decrypted)
    encryptor=Encryptor()
    mykey=encryptor.key_create()
encryptor.key_write(mykey, 'mykey.key')
loaded_key=encryptor.key_load('mykey.key')
encryptor.file_encrypt(loaded_key, 'grades.csv', 'enc_grades.csv')
encryptor.file_decrypt(loaded_key, 'enc_grades.csv', 'dec_grades.csv')
