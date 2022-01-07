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

#                                                                                      Linear Regression
# makes predictions for continuous/real or numeric variables such as sales, salary, age, product price
# Simple Linear Regression = to predict the value of a numerical dependent variable
# Multiple Linear regression = more than one independent variable is used to predict the value of a numerical dependent variable
#                                  Linear Regression Line
# Positive Linear Relationship = dependent variable increases on the Y-axis and independent variable increases on X-axis
# Negative Linear Relationship = dependent variable decreases on the Y-axis and independent variable increases on the X-axis
#                                   Finding the best fit line
# the error between predicted values and actual values should be minimized(least error)
#                                            Cost function
# Cost function = to find the best fit line, to find the accuracy of the mapping function(Hypothesis function)
# Mean Squared Error (MSE)  = avg(squared error occurred between the predicted values and actual values)
#                                                Residuals
# distance between the actual value and predicted values
#                                              Gradient Descent
# minimize the MSE by calculating the gradient of the cost function
# to update the coefficients of the line by reducing the cost function
# a random selection of values of coefficient and then iteratively update the values to reach the minimum cost function
#                                              Model Performance
# R-squared method = measures the strength of the relationship between the dependent and independent variables on a scale of 0-100%.
# coefficient of determination, or coefficient of multiple determination for multiple regression
#                                             Assumptions of Linear Regression
# Linear relationship = linear relationship between the dependent and independent variables
# Small or no multicollinearity between the features = high-correlation between the independent variables.
#                                                        Homoscedasticity Assumption
# the error term is the same for all the values of independent variables
#                                                    Normal distribution
# Normal distribution of error terms = checked using the q-q plot
# the plot shows a straight line without any deviation, which means the error is normally distributed
#                                                                    No autocorrelations
# any correlation in the error term, then it will drastically reduce the accuracy of the model
# occours when dependency between residual errors
#                                                                                            Simple Linear Regression
# dependent variable must be a continuous/real value
# Forecasting new observations, Model the relationship between the two variables
#                                                          Simple Linear Regression Model
y= a0+a1x+ ε"""a0= It is the intercept of the Regression line (can be obtained putting x=0)
a1= It is the slope of the regression line, which tells whether the line is increasing or decreasing.
ε = The error term. (For a good model it will be negligible)"""
# We want to find out if there is any correlation between these two variables
# We will find the best fit line for the dataset.
# How the dependent variable is changing by changing the dependent variable.
#                     Step 1: Data Pre-processing
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
# Next, we will load the dataset into our code:
data_set= pd.read_csv('Salary_Data.csv')
# extract the dependent and independent variables from the given dataset
x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 1].values
# split both variables into the test set and training set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 1/3, random_state=0)
#                                        Fitting the Simple Linear Regression to the Training Set
# overfitting can produce misleading R-squared values, regression coefficients, and p-values
# import the LinearRegression class of the linear_model library from the scikit learn, regressor = object of the class
#                                      Fitting the Simple Linear Regression model to the training dataset  
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train, y_train) # fit() method to fit our Simple Linear Regression object to the training set
# o/p = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
#                                     Prediction of test, training-set result(Training)
# Visualizing the Training set results, performance of our model 
mtp.scatter(x_train, y_train, color="green")   # create a scatter plot of observations.
mtp.plot(x_train, x_pred, color="red")    # plot the regression line, predicted salary for training set x_pred, and color of the line
mtp.title("Salary vs Experience (Training Dataset)")  # title for the plot
mtp.xlabel("Years of Experience")  # assign labels for x-axis and y-axis
mtp.ylabel("Salary(In Rupees)")  
mtp.show()
#                                          visualizing the Test set results(Test)
mtp.scatter(x_test, y_test, color="blue")   # Test
mtp.plot(x_train, x_pred, color="red")      # Train
mtp.title("Salary vs Experience (Test Dataset)")  
mtp.xlabel("Years of Experience")  
mtp.ylabel("Salary(In Rupees)")  
mtp.show()
#                                                                                                    Multiple Linear Regression
# response variable is affected by more than one predictor variable
# (MLR) is to model the linear relationship between the explanatory (independent) variables and response (dependent) variable
# linear relationship between a single dependent continuous variable and more than one independent variable
# For MLR, the dependent or target variable(Y) must be the continuous/real
# predictor or independent variable may be of continuous or categorical form
Y= b0+b1x1+ b2x2+ b3x3+...... bnxn       ............... (a)
"""Y= Output/Response variable
b0, b1, b2, b3 , bn....= Coefficients of the model.
x1, x2, x3, x4,...= Various Independent/feature variable"""
#                Assumptions for Multiple Linear Regression
# Multivariate Normality = residuals are normally distributed.
# No Multicollinearity = independent variables are not highly correlated with each other, tested using Variance Inflation Factor (VIF) values
# Homoscedasticity = variance of error terms are similar across the values of the independent variables
# at least two independent variables, which can be nominal, ordinal, or interval/ratio level variables.
# The regression residuals must be normally distributed, MLR assumes little or no multicollinearity in data
#                                                             implementation of Multiple Linear Regression model
#                                                 Problem
"""We have a dataset of 50 start-up companies. This dataset contains five main information: 
R&D Spend, Administration Spend, Marketing Spend, State, and Profit for a financial year. Our goal is to create a model that can 
easily determine which company has a maximum profit, and which is the most affecting factor for the profit of a company."""
#                                Data Pre-processing Steps
import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd
#                   importing datasets  
data_set= pd.read_csv('50_CompList.csv')
#                   Extracting Independent and dependent Variable  
x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 4].values
#                                         Encoding Dummy Variables
#                      Catgorical data  
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  
labelencoder_x= LabelEncoder()  
x[:, 3]= labelencoder_x.fit_transform(x[:,3])  
onehotencoder= OneHotEncoder(categorical_features= [3])    #  create the dummy variables
x= onehotencoder.fit_transform(x).toarray()
#                               avoiding the dummy variable trap
x = x[:, 1:]
#                           Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)

# Fitting the MLR model to the training set
from sklearn.linear_model import LinearRegression  
regressor= LinearRegression()  
regressor.fit(x_train, y_train)
# o/p = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
# Predicting the result of the test set
y_pred= regressor.predict(x_test) #               create a y_pred vector
#                                 check the score for training dataset and test dataset
print('Train Score: ', regressor.score(x_train, y_train))
print('Test Score: ', regressor.score(x_test, y_test))
"""Effectiveness of Independent variable on prediction.
Predicting the impact of changes
to find the relations between two or more variables""" 
#                                                                                   Terminologies Related to the Regression Analysis
# Dependent Variable = a target variable to predict or understand is called the dependent variable
# Independent Variable (predictor) = used to predict the values of the dependent variables
# Multicollinearity = variables are highly correlated with eachother
# Outliers = points on the graph that fall significantly outside the cloud made up of other points
# Overfitting = occurrence when the variables start to show random errors rather than efficiently describing the relationship among the variables
# Underfitting = number of variables scarcely fits a given model
# Heteroscedasticity (heteroskedasticity) = while reading variable’s standard error (SE) measured over a given time is not constant
#                                                                                         $         Linear Regression
# Analyzing trends, sales estimates, Salary forecasting, Real estate prediction, Arriving at ETAs in traffic.
#                                                                                         $     Logistic regression(sigmoid function)
# categorical variable such as 0 or 1, Yes or No, True or False, Spam or not spam
# sigmoid function is used to model the data, sig(x)=1/1+e^-x
# Binary(0/1, pass/fail), Multi(cats, dogs, lions), Ordinal(low, medium, high)
#                                                                                         $   Support Vector Machine
# Kernel : is a function used to map a lower-dimensional data into higher dimensional data
# Hyperplane: SVM is a separation line between two classes
# in SVR, line which helps to predict the continuous variables and cover most of the datapoints
# Boundary lines are the two lines apart from hyperplane, which creates a margin for datapoints
# Support vectors are the datapoints which are nearest to the hyperplane and opposite class
#                                                                                             $      Decision Tree Regression
# solve problems for both categorical and numerical data
# tree-like structure in which each internal node represents the "test" for an attribute, 
# each branch represent the result of the test, and each leaf node represents the final decision or result
# is constructed starting from the root node/parent node (dataset), which splits into left and right child nodes (subsets of dataset).
# These child nodes are further divided into their children node, and themselves become the parent node of those nodes
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
pd.set_option('display.max_columns',None)
df = pd.read_csv("train.csv")
df.head()
df.drop(['PassengerId','SibSp','Name','Parch','Fare','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
df.head()
inputs = df.drop('Survived',axis='columns')
target = df.Survived
inputs.Sex = inputs.Sex.map({'male': 1, 'female': 2})
inputs.head()
inputs.Age[:10]
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
inputs.Age[:10]
X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.2)
model = tree.DecisionTreeClassifier()
model.fit(X_train,y_train)
model.score(X_test,y_test)
#                                                                                           $      Random Forest Regression
# ensemble learning method which combines multiple decision trees and predicts the final output based on the average of each tree output
# g(x)= f0(x)+ f1(x)+ f2(x)+.,,,
# Bagging or Bootstrap Aggregation technique of ensemble learning in which aggregated decision tree runs in parallel and do not interact with each other
# Overfitting in the model by creating random subsets of the dataset
#                                                                                            $       Ridge Regression
# The amount of bias added to the model is known as Ridge Regression penalty
# by multiplying with the lambda to the squared weight of each individual features 
βridge=(X′X+λI)−1(X′Y)
# high collinearity between the independent variables, regularization technique, which is used to reduce the complexity of the model
#                                                                                               $       Lasso Regression
# penalty term contains only the absolute weights instead of a square of weights
# it takes absolute values, hence, it can shrink the slope to 0

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
