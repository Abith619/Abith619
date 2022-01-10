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
from typing import no_type_check
from pandas.core.frame import DataFrame
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib_inline
from scipy import stats

print(matrix(runif(6*3), nrow=6, ncol=3))
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

#                                                        Creating Raw  Data with 4 Fields
#                            Aplying Filters in DataFrames
houses[houses['Bedroom']<20]
# Outlier Detection = Discard some of the data, Fitting the outlier Data
abithHouseDf['Outlier'] = np.where(abithHouseDf['HouseCost']>=11000,0,1)
abithHouseDf
# Inliner = Considered,  some data
#                                                                                      Applying logarthmic Data
abithHouseDf['logofsqFt'] = [np.log(x) for x in abithHouseDf['HouseSizeSqFt']]
#                                  create Dataframe
houses = pd.DataFrame()
houses['price'] = [534433, 392333, 293222, 4322032]
houses['Bedroom'] = [2,3.5,2,116]
houses['Square_feet'] = [1500, 2500, 1500, 48000]
houses
#                                       Drop Observation greater than some value
houses[houses['Bedroom']<20]
import numpy as np
#                                       create feature based on boolean condition
houses['Outliner']=np.where(houses['Bathrooms']<20,0,1)
houses                                # show data
#                                                       Log Data
houses['Log_of_square_feet']=[np.log(x) for x in houses['square_Feet']]
houses
houses = pd.DataFrame(
    {
        'price' : [534433, 392333, 293222, 4322032],
        'Bedroom' : [2, 3.5, 2, 116],
        "Square_feet" : [1500, 2500, 1500, 48000]
    }
)
houses
#                                                           Appending
abithHouseDf.append(abithHouseDf1,ignore=True)
#                                                        remove null(NAN) values 
import numpy as np
import pandas as pd
#                  Create feature matrix
X=np.array([
    [1,2],
    [6,3],
    [9,5],
    [np.nan,4]
])
# Load data as a DataFrame
df=pd.DataFrame(X, columns=['feature_1','feature_2'])
# observations
df
df.dropna() # removes null value
#                                                   Fit & Transform in replacing null values
# import numpy, pandas, scikit-learn
from sklearn.impute import SimpleImputer
df=pd.DataFrame()
df['x0']=[0.3051,0.4949,0.6974,4436,0.5]
df['x1']=[np.nan,0.2654,0.2654,0.2615,0.6731]
#                                             Replace nan values with mean value, with Imputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean') # creating Imputer Object
#                                           train(fit) the Imputer
mean_Imputer=mean_Imputer.fit(df)
#                                            Apply Imputer to dataset
imputed_df=mean_imputer.transform(df.values)
imputed_df

#                                                                                                                        String Manipulations & Functions
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
#                                                                                          Classification Algorithm
# to categorize our data into a desired and distinct number of classes where we can assign label to each class
# Classes can be called as targets/labels or categories
y=f(x)  # y = categorical output
# (eg) = Email Spam Detector
# class A and Class B
#                                                   Binary Classifier
# YES or NO, MALE or FEMALE, SPAM or NOT SPAM, CAT or DOG, etc
#                                                   Multi-class Classifier
# Classifications of types of crops, music
#                                                                                     Learners
# Lazy Learners = firstly stores the training dataset and wait until it receives the test dataset
# (eg) =  K-NN algorithm, Case-based reasoning
# Eager Learners = develop a classification model based on a training dataset before receiving a test dataset
# (eg) = Decision Trees, Naïve Bayes, ANN
#                                                                   Types of ML Classification Algorithms
# Linear Models = Logistic Regression, Support Vector Machines
#                                                        Logistic Regression
# binary classification of data-points, of the two classes (1 or 0)
# (eg predict whether it will rain today or not, based on the current weather conditions
# Hypothesis = derive the likelihood of the event, data fit to log(), that creates an S-shaped curve known as “sigmoid”, 0Sigmoid Curve

#                                                                                                 Decision Tree Classification
# used for both predictions & classifications, 2Types = Induction & Pruning
# map the various outcomes that are a result of the consequences or decisions
# result of various hierarchical steps that will help you to reach certain decisions
#  tree-structured classifier, where internal nodes represent the features of a dataset, 
# branches represent the decision rules and each leaf node represents the outcome
# Decision Node, Leaf Node(Output), Splitting, Branch/Sub Tree, Pruning, Parent/Child node, 
"""Step 1 : Begin the tree with the root node, says S, which contains the complete dataset.
Step 2 : Find the best attribute in the dataset using Attribute Selection Measure (ASM).
Step 3 : Divide the S into subsets that contains possible values for the best attributes.
Step 4 : Generate the decision tree node, which contains the best attribute.
Step 5 : Recursively make new decision trees using the subsets of the dataset created in step -3. Continue this process until a stage is 
reached where you cannot further classify the nodes and called the final node as a leaf node."""
node = output
# select the best attribute for the nodes of the tree = Information Gain, Gini Index
#                                                          Information Gain
# measurement of changes in entropy after the segmentation of a dataset based on an attribute
Information Gain= Entropy(S)- [(Weighted Avg) # *Entropy(each feature)
#                                                                Entropy
#  metric to measure the impurity in a given attribute
Entropy(s)= -P(yes)log2 P(yes)- P(no) log2 P(no)
#                                                                 Gini Index
#  measure of impurity or purity used while creating a decision tree in the CART(Classification and Regression Tree) algorithm
# creates binary splits, and the CART algorithm uses the Gini index to create binary splits
Gini Index= 1- ∑jPj2
#                                                                   Pruning
# Getting an Optimal Decision tree
# technique that decreases the size of the learning tree without reducing accuracy
# 2 Types = Cost Complexity Pruning, Reduced Error Pruning
#                                                                     Implementation of Decision Tree
"""Data Pre-processing step
Fitting a Decision-Tree algorithm to the Training set
Predicting the test result
Test accuracy of the result(Creation of Confusion matrix)
Visualizing the test set result."""
#                                    importing datasets  
data_set= pd.read_csv('user_data.csv')  
#                                    Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values  
#                                    Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)  
#                                   feature Scaling  
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)
#                                                             Fitting a Decision-Tree algorithm to the Training set
#                        Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)  
#                                                feature Scaling  
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)
# "criterion='entropy': Criterion is used to measure the quality of split
# random_state=0": For generating the random states
#                                  Predicting the test result
y_pred= classifier.predict(x_test)
#                                         Test accuracy of the result (Creation of Confusion matrix)
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
#                                                                      Visualizing the training set result
from matplotlib.colors import ListedColormap  
x_set, y_set = x_train, y_train  
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
alpha = 0.75, cmap = ListedColormap(('purple','green' )))  
mtp.xlim(x1.min(), x1.max())  
mtp.ylim(x2.min(), x2.max())  
fori, j in enumerate(nm.unique(y_set)):  
mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
        c = ListedColormap(('purple', 'green'))(i), label = j)  
mtp.title('Decision Tree Algorithm (Training set)')  
mtp.xlabel('Age')  
mtp.ylabel('Estimated Salary')  
mtp.legend()  
mtp.show()

#                                                                                                  Random Forest Classification
# ensemble learning method that is used for classification, regression and other tasks that can be performed with the help of the decision trees
# correct the habit of overfitting to the training set,  more accurate than the decision trees
#                                                                                           Evaluating a Classification model
#                              Log Loss or Cross-Entropy Loss
# good binary Classification model, the value of log loss should be near to 0
?(ylog(p)+(1?y)log(1?p))
#                                              Confusion Matrix(error matrix.)
# predictions result in a summarized form, total number of correct predictions and incorrect predictions
# O/P => Matrix(Actual Positive, Negative : Predicted Positive, Negative)
#                                                            AUC-ROC curve
# Area Under the Curve(AUC), Receiver Operating Characteristics Curve(ROC)
# to visualize the performance of the multi-class classification model
# The ROC curve is plotted with TPR and FPR, where TPR (True Positive Rate) on Y-axis and FPR(False Positive Rate) on X-axis


#                                                                                                K-Nearest Neighbor(KNN) Algorithm
# stores all the available data and classifies a new data point based on the similarity
#  non-parametric algorithm, lazy learner algorithm,  Euclidean distance of K number of neighbors
"""Step 1 : Select the number K of the neighbors
Step 2: Calculate the Euclidean distance of K number of neighbors
Step 3: Take the K nearest neighbors as per the calculated Euclidean distance.
Step 4: Among these k neighbors, count the number of the data points in each category.
Step 5: Assign the new data points to that category for which the number of the neighbor is maximum"""
#                                                                                            implementation of the KNN algorithm
#                                                                Data Pre-Processing Step
#                                            importing libraries
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
#                                        importing datasets  
data_set= pd.read_csv('user_data.csv')  
#                                       Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values
y= data_set.iloc[:, 4].values
#                                           Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
#                                                         feature Scaling
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)
#                                                      Fitting K-NN classifier to the Training data
"""n_neighbors: To define the required neighbors of the algorithm. Usually, it takes 5.
metric='minkowski': This is the default parameter and it decides the distance between the points.
p=2: It is equivalent to the standard Euclidean metric."""
from sklearn.neighbors import KNeighborsClassifier
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )
classifier.fit(x_train, y_train)
#                                                              Predicting the test set result
y_pred= classifier.predict(x_test)
#                                               Creating the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
#                                                        Visulaizing the trianing set result  
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
alpha = 0.75, cmap = ListedColormap(('red','green' )))
mtp.xlim(x1.min(), x1.max())
mtp.ylim(x2.min(), x2.max())
for i, j in enumerate(nm.unique(y_set)):
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
        c = ListedColormap(('red', 'green'))(i), label = j)
mtp.title('K-NN Algorithm (Training set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()
#                                                            Visualizing the test set result  
from matplotlib.colors import ListedColormap  
x_set, y_set = x_test, y_test  
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),  
alpha = 0.75, cmap = ListedColormap(('red','green' )))  
mtp.xlim(x1.min(), x1.max())  
mtp.ylim(x2.min(), x2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
        c = ListedColormap(('red', 'green'))(i), label = j)  
mtp.title('K-NN algorithm(Test set)')  
mtp.xlabel('Age')  
mtp.ylabel('Estimated Salary')  
mtp.legend()  
mtp.show()
#                                                        Support Vector Machines (svm)
# plotting in the n-dimensional space
#                                                       Non-linear Models
# K-Nearest Neighbours = pattern recognition, data mining, and intrusion detection
# the KNN classifies the coordinates into groups that are identified by a specific attribute
#                                                                            Naïve Bayes
# an extension of the Bayes theorem wherein each feature assumes independence
# easy and quick way to predict the class of the dataset, multi-class prediction
#                                                                           Naive Bayes Classifier Algorithm
# text classification that includes a high-dimensional training dataset
# models that assign class labels to problem instances, represented as vectors of feature values
#                                                                   Bayes' Theorem:
"""P(c|x) is Posterior probability: Probability of hypothesis A on the observed event B.
P(x|c) is Likelihood probability: Probability of the evidence given that the probability of a hypothesis is true.
P(c) is Class Prior Probability: Probability of hypothesis before observing the evidence.
P(x) is Predictor Prior Probability: Probability of Evidence."""
#                                                                         Working of Naïve Bayes' Classifier:
"""Convert the given dataset into frequency tables.
Generate Likelihood table by finding the probabilities of given features.
Now, use Bayes theorem to calculate the posterior probability"""
#                                                                     Applying Bayes'theorem:
P(Yes|Sunny)= P(Sunny|Yes)*P(Yes)/P(Sunny)
P(Sunny|Yes)= 3/10= 0.3
P(Sunny)= 0.35
P(Yes)=0.71
So P(Yes|Sunny) = 0.3*0.71/0.35= 0.60

P(Yes|Sunny)>P(No|Sunny)
P(No|Sunny)= P(Sunny|No)*P(No)/P(Sunny)
P(Sunny|NO)= 2/4=0.5
P(No)= 0.29
P(Sunny)= 0.35
So P(No|Sunny)= 0.5*0.29/0.35 = 0.41
#                                        Applications
# Multi-class Prediction, Recommendation System,  real-time predictions, Text classification such as Spam filtering and Sentiment analysis
#                                                              3 Types = Gaussian, Multinomial, Bernoulli
#                                                              Implementation of the Naïve Bayes algorithm
"""Data Pre-processing step
Fitting Naive Bayes to the Training set
Predicting the test result
Test accuracy of the result(Creation of Confusion matrix)
Visualizing the test set result."""
#                                     Importing the dataset  
dataset = pd.read_csv('user_data.csv')
x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values
#                                           Splitting the dataset into the Training set and Test set  
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
#                                        Feature Scaling  
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
#                                  Fitting Naive Bayes to the Training set  
from sklearn.naive_bayes import GaussianNB  
classifier = GaussianNB()  
classifier.fit(x_train, y_train)
#                                         Predicting the Test set results  
y_pred = classifier.predict(x_test)
#                                               Making the Confusion Matrix  
from sklearn.metrics import confusion_matrix  
cm = confusion_matrix(y_test, y_pred)
#                                                        Visualising the Training set results  
from matplotlib.colors import ListedColormap  
x_set, y_set = x_train, y_train  
X1, X2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),  
                     nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(X1, X2, classifier.predict(nm.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),  
             alpha = 0.75, cmap = ListedColormap(('purple', 'green')))  
mtp.xlim(X1.min(), X1.max())  
mtp.ylim(X2.min(), X2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
                c = ListedColormap(('purple', 'green'))(i), label = j)  
mtp.title('Naive Bayes (Training set)')  
mtp.xlabel('Age')  
mtp.ylabel('Estimated Salary')  
mtp.legend()  
mtp.show()
#                                                  Visualising the Test set results  
from matplotlib.colors import ListedColormap  
x_set, y_set = x_test, y_test  
X1, X2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),  
                     nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  
mtp.contourf(X1, X2, classifier.predict(nm.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),  
             alpha = 0.75, cmap = ListedColormap(('purple', 'green')))  
mtp.xlim(X1.min(), X1.max())  
mtp.ylim(X2.min(), X2.max())  
for i, j in enumerate(nm.unique(y_set)):  
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],  
                c = ListedColormap(('purple', 'green'))(i), label = j)  
mtp.title('Naive Bayes (test set)')  
mtp.xlabel('Age')  
mtp.ylabel('Estimated Salary')  
mtp.legend()  
mtp.show()



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
# finds the hidden patterns in data
#                                                                                           Clustering
#                                                             Evaluating Clustering
# clustering data points to groups, ) Clustering tendency, Number of clusters(k), Clustering quality
#                                                              Clustering tendency
# making sure does not contain uniformly distributed points
# Null Hypothesis (Ho) : Data points are generated by non-random, uniform distribution (implying no meaningful clusters)
# Alternate Hypothesis (Ha): Data points are generated by random data points (presence of clusters)
#                                                         Number of Optimal Clusters, k
# a) Distribution shape (b) scale in the data set (c) clustering resolution required by user
#                                                  find optimal number of clusters:
# Domain knowledge = finding number of clusters, driven k value gives more relevant insights.
# Data driven approach = mathematical methods help in finding out right number of clusters.
# Empirical Method = Square root of N/2 where N is total number of data points
# Elbow method = Within-cluster variance is a measure of compactness of the cluster
#                                                                    Statistical approach
# Gap statistic, sum of within-cluster (intra-cluster) variance is calculated for different values of k
#                                                            Clustering quality
# minimal intra cluster distance and maximal inter cluster distance
# 2 types to assess the clustering performance
# Extrinsic Measures = ground truth labels, (eg) = Adjusted Rand index, Fowlkes-Mallows scores, Mutual information based scores, Homogeneity, Completeness and V-measure.
# Intrinsic Measures = Silhouette Coefficient, Calinski-Harabasz Index, Davies-Bouldin Index etc
#                                                                                   K-means
# cluster =  collection of data points aggregated together because of certain similarities
# centroid is the imaginary or real location representing the center of the cluster.
# Step 2:                                                            Generate random data
X= -2 * np.random.rand(100,2)
X1 = 1 + 2 * np.random.rand(50,2)
X[50:100, :] = X1
plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = ‘b’)
plt.show()
# Step 3:                                                                Use Scikit-Learn
from sklearn.cluster import KMeans
Kmean = KMeans(n_clusters=2) # k (n_clusters) an arbitrary value of 2)
Kmean.fit(X)
KMeans(algorithm=’auto’, copy_x=True, init=’k-means++’, max_iter=300
n_clusters=2, n_init=10, n_jobs=1, precompute_distances=’auto’,
random_state=None, tol=0.0001, verbose=0)
# Step 4:                                                                Finding the centroid
Kmean.cluster_centers_
#                            display the cluster centroids (using green and red color)
plt.scatter(X[ : , 0], X[ : , 1], s =50, c=’b’)
plt.scatter(-0.94665068, -0.97138368, s=200, c=’g’, marker=’s’)
plt.scatter(2.01559419, 2.02597093, s=200, c=’r’, marker=’s’)
plt.show()
# Step 5: Testing the algorithm
Kmean.labels_ # labels property of the K-means clustering
# data points are categorized into the two clusters
sample_test=np.array([-3.0,-3.0])
second_test=sample_test.reshape(1, -1) # predicting the cluster of a data point
Kmean.predict(second_test) # o/p = array([0])
# hidden Markow Model                                                       (fit & transform with standard scaler in iris Dataset)
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X = iris.data
Y = iris.target
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
clt = KMeans()
#                                                           Mini Batch K-means algorithm
# small random batches of data of a fixed size are stored in a memory
# Each mini batch updates the clusters using a convex combination of the values of the prototypes and the data
# the number of clusters or its size, affect the partition quality.
D = {d1, d2, d3, .....dn},
                       no. of iterations t,
                       batch size b, 
                       no. of clusters k.
k clusters C = {c1, c2, c3, ......ck}
initialize k cluster centers O = {o1, o2, .......ok}
#                                        initialize each cluster
Ci = Φ (1=< i =< k)
# _                                      initialize no. of data in each cluster
Nci = 0 (1=< i =< k)
for j=1 to t do:
    #                                       M is the batch dataset and xm
    #                                       the sample randomly chosen from D
    M = {xm | 1 =< m =< b}
    #                                           catch cluster center for each
    #                                             sample in the batch data set
    for m=1 to b do:
        oi(xm) = sum(xm)/|c|i (xm ε M and xm ε ci)
    end for
    #                                     update the cluster center with each batch set
     for m=1 to b do:
        # get the cluster center for xm
        oi = oi(xm)
        # update number of data for each cluster center
        Nci = Nci + 1
        #calculate learning rate for each cluster center
        lr=1/Nci
        # take gradient step to update cluster center
        oi = (1-lr)oi + lr*xm
     end for
end for

#                                                          using scikit-learn library
from sklearn.cluster import MiniBatchKMeans, KMeans 
from sklearn.metrics.pairwise import pairwise_distances_argmin 
from sklearn.datasets.samples_generator import make_blobs 
#                                              Load data in X  
batch_size = 45
centers = [[1, 1], [-2, -1], [1, -2], [1, 9]] 
n_clusters = len(centers) 
X, labels_true = make_blobs(n_samples = 3000, 
                            centers = centers, 
                            cluster_std = 0.9) 
#                                              perform the mini batch K-means 
mbk = MiniBatchKMeans(init ='k-means++', n_clusters = 4, 
                      batch_size = batch_size, n_init = 10, 
                      max_no_improvement = 10, verbose = 0) 
mbk.fit(X) 
mbk_means_cluster_centers = np.sort(mbk.cluster_centers_, axis = 0) 
mbk_means_labels = pairwise_distances_argmin(X, mbk_means_cluster_centers) 
#                                           print the labels of each data 
print(mbk_means_labels)

#                                                              DBSCAN Clustering
# Density-based spatial clustering of applications with noise
"""different distance measures. E.g. K-Means (distance between points), Affinity propagation (graph distance), 
Mean-shift (distance between points), DBSCAN (distance between nearest points), Gaussian mixtures (Mahalanobis distance to centers), 
Spectral clustering (graph distance)"""
# It can discover clusters of different shapes and sizes from a large amount of data, which is containing noise and outliers
# 2 Parameters = minPts = The minimum number of points (a threshold) clustered together for a region to be considered dense., 
# eps (ε) = A distance measure that will be used to locate the points in the neighborhood of any point.
"""Core — This is a point that has at least m points within distance n from itself.
Border — This is a point that has at least one Core point at a distance n.
Noise — This is a point that is neither a Core nor a Border. And it has less than m points within distance n from itself"""
# Algorithmic steps for DBSCAN clustering
#   implementation using sklearn
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
#                                                  Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)
X = StandardScaler().fit_transform(X)
#                                                                 Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_
#                                                     Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))
#                                                            Plot result
import matplotlib.pyplot as plt
%matplotlib inline
#                                                       Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]
    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


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
#                                                              Terminologies Related to the Regression Analysis
# Dependent Variable = a target variable to predict or understand is called the dependent variable
# Independent Variable (predictor) = used to predict the values of the dependent variables
# Multicollinearity = variables are highly correlated with eachother
# Outliers = points on the graph that fall significantly outside the cloud made up of other points
# Overfitting = occurrence when the variables start to show random errors rather than efficiently describing the relationship among the variables
# Underfitting = number of variables scarcely fits a given model
# Heteroscedasticity (heteroskedasticity) = while reading variable’s standard error (SE) measured over a given time is not constant
#                                                                                         $         Linear Regression
# Analyzing trends, sales estimates, Salary forecasting, Real estate prediction, Arriving at ETAs in traffic
# for continuous/real or numeric variables such as sales, salary, age, product price
# 2 Types = Simple Linear Regression = numerical dependent variable
# Multiple Linear regression = more than one numerical dependent variable
# Linear Regression Line = Positive Linear Relationship + Negative Linear Relationship
# the best fit line = error between predicted values and actual values should be minimized(least error)
#                                                         Cost function
# estimate the values of the coefficient for the best fit line.(Hypothesis function)
# optimizes the regression coefficients or weights. It measures how a linear regression model is performing
# Mean Squared Error (MSE) = average of squared error occurred between the predicted values and actual values
"""Yi = Actual value
(a1xi+a0)= Predicted value"""
#                                                           Residuals
# distance between the actual value and predicted values
# If the observed points are far from the regression line, then the residual will be high, and so cost function will high
# If the scatter points are close to the regression line, then the residual will be small and hence the cost function.
#                                                         Gradient Descent
# minimize the MSE by calculating the gradient of the cost function
# to update the coefficients of the line by reducing the cost function
# by a random selection of values of coefficient and then iteratively update the values to reach the minimum cost function.
#                                                                     Model Performance
#         R-squared method(fit)
# coefficient of determination, or coefficient of multiple determination 
# it measures the strength of the relationship between the dependent and independent variables on a scale of 0-100%.
#                            formal checks while building a Linear Regression model
# Linear relationship between the features and target, between the dependent and independent variables
# Small or no multicollinearity between the features, high-correlation between the independent variables
#                                                               Homoscedasticity Assumption
# error term is the same for all the values of independent variables. With homoscedasticity, 
# there should be no clear pattern distribution of data in the scatter plot.
"""                                                                                Types of Regression Algorithm:
Simple Linear Regression
Multiple Linear Regression
Polynomial Regression
Support Vector Regression
Decision Tree Regression
Random Forest Regression"""
#                                                                                                           Backward elimination
# smartly trained to come out with better recognition of real-world objects
# to remove those features that do not have a significant effect on the dependent variable or prediction of output
# array of ones all elements of that array are “1”
# 5% significance level for P-value, P-value = 0.05
#                                                   Fit the model with all features
import statsmodels.api as sm 
X_train_opt = np.append(arr = np.ones((274,1)).astype(int), values = X_train, axis = 1) 
X_train_opt = X_train_opt[:,[0, 1, 2, 3, 4, 5, 6, 7]] 
regressor_OLS = sm.OLS(endog = y_train, exog = X_train_opt).fit()
regressor_OLS.summary()
# to build a model in Machine Learning
"""All-in
Backward Elimination
Forward Selection
Bidirectional Elimination
Score Comparison"""
# Step 1 : to select a significance level to stay in the model. (SL=0.05)
import statsmodels.api as smf
#         Adding a column in matrix of features :
x = nm.append(arr = nm.ones((50,1)).astype(int), values=x, axis=1)
# Step 2 : Fit the complete model with all possible predictors/independent variables
x_opt=x [:, [0,1,2,3,4,5]]  
regressor_OLS=sm.OLS(endog = y, exog=x_opt).fit()  
regressor_OLS.summary()
# Step 3 : Choose the predictor which has the highest P-value
# If P-value >SL, go to step 4.
# Else Finish, and Our model is ready
# Step 4 : Remove that predictor
# Step 5 : Rebuild and fit the model with the remaining variables
"""This process is used to optimize the performance of the MLR model
as it will only include the most affecting feature and remove the least affecting feature"""
# Sample program
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
#                                                         importing datasets  
data_set= pd.read_csv('50_CompList.csv')
#                                                         Extracting Independent and dependent Variable  
x= data_set.iloc[:, :-1].values
y= data_set.iloc[:, 4].values
#                                                         Catgorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x= LabelEncoder()
x[:, 3]= labelencoder_x.fit_transform(x[:,3])
onehotencoder= OneHotEncoder(categorical_features= [3])
x= onehotencoder.fit_transform(x).toarray()
#                                                         Avoiding the dummy variable trap:  
x = x[:, 1:]
#                                                         Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2, random_state=0)
#                                                         Fitting the MLR model to the training set
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train, y_train)
#                                                         Predicting the Test set result
y_pred= regressor.predict(x_test)
#                                                         Checking the score
print('Train Score: ', regressor.score(x_train, y_train))
print('Test Score: ', regressor.score(x_test, y_test))

#                                                                                         $     Polynominal Regression
# non-linear Datasets are used
y= b0+b1x1+ b2x12+ b2x13+...... bnx1n
# the original features are converted into Polynomial features of required degree (2,3,..,n) and then modeled using a linear model
# it depends on the coefficients, which are arranged in a linear fashion
# Simple Linear Regression equation:         
y = b0+b1x
# Multiple Linear Regression equation:         
y= b0+b1x+ b2x2+ b3x3+....+ bnxn
# Polynomial Regression equation:         
y= b0+b1x + b2x2+ b3x3+....+ bnxn
# non-linear relationship between the Position levels and the salaries, Bluffing detector regression
#                                                                Data Pre-processing
# we will not use feature scaling, and also we will not split our dataset into training and test set

# Build a Linear Regression model and fit it to the dataset
from sklearn.linear_model import LinearRegression  
lin_regs= LinearRegression()  
lin_regs.fit(x,y)
#                                                      Build a Polynomial Regression model and fit it to the dataset  
from sklearn.preprocessing import PolynomialFeatures  
poly_regs= PolynomialFeatures(degree= 2)  
x_poly= poly_regs.fit_transform(x)  
lin_reg_2 =LinearRegression()  
lin_reg_2.fit(x_poly, y)
#                                                     Visualize the result for Linear Regression model
mtp.scatter(x,y,color="blue")
mtp.plot(x,lin_regs.predict(x), color="red")
mtp.title("Bluff detection model(Linear Regression)")
mtp.xlabel("Position Levels")
mtp.ylabel("Salary")
mtp.show()
#                                                     Visualizing the result for Polynomial Regression
mtp.scatter(x,y,color="blue")  
mtp.plot(x, lin_reg_2.predict(poly_regs.fit_transform(x)), color="red")  
mtp.title("Bluff detection model(Polynomial Regression)")  
mtp.xlabel("Position Levels")  
mtp.ylabel("Salary")  
mtp.show()
#                                                        Predicting the output with Linear Regression model
lin_pred = lin_regs.predict([[6.5]])
print(lin_pred)
#                                                         Predicting the output with Polynomial Regression model
poly_pred = lin_reg_2.predict(poly_regs.fit_transform([[6.5]]))
print(poly_pred)

#                                                                                         $     Logistic regression(sigmoid function)
# categorical variable such as 0 or 1, Yes or No, True or False, Spam or not spam
# sigmoid function is used to model the data, sig(x)=1/1+e^-x
# Binary(0/1, pass/fail), Multi(cats, dogs, lions), Ordinal(low, medium, high)
# fit an "S" shaped logistic function, which predicts two maximum values (0 or 1)
# range between -[infinity] to +[infinity], then take logarithm of the equation
# 3 Types = Binomial = 0 or 1, Pass or Fail,, Multinomial = cat", "dogs", or "sheep", Ordinal = "low", "Medium", or "High"
# Softmax function is used for multiclassification
# predict the target class (more than 2 target classes)
#                                       Multinomial Logistic Regression
"""Inputs
Linear model
Logits
Softmax Function
Cross Entropy
One-Hot-Encoding"""
#                          Inputs
# sepal length, width and petal length and width parameters
# assign an integer value to each attribute of the features like for RED we can assign 1
#                                                                    Linear Model
# X = [x1,x2,x3], W = [w1,w2,w3],  w1*x1,  w2*x2, w3*x3  
#                                                                     Logits
# scores, outputs of the linear model
#                                                          Softmax Function
# probabilistic function, calculates the probabilities for the given score
import numpy as np
def softmax(inputs):
    """
    Calculate the softmax for the give inputs (array)
    :param inputs:
    :return:
    """
    return np.exp(inputs) / float(sum(np.exp(inputs)))
softmax_inputs = [2, 3, 5, 6]
print "Softmax Function Output :: {}".format(softmax(softmax_inputs))
# cross-entropy function to find the similarity distance between the 
# distance calculation function, right target class, the distance value will be less
# probabilities calculated from the softmax function and the target one-hot-encoding matrix
# One-Hot Encoding is a method to represent the target values or categorical attributes into a binary representation  [0, 1, 0]
# weights calculated and update the weights is know as the Parameters Optimization
#                                                          Parameters Optimization
# iteration process,to calculate Loss function
#                                                             Loss function
# input =  calculated weights and all the training observations
#                                                                                   Implementation of Logistic Regression (Binomial)
# Data Pre-processing step
# importing libraries, Datasets
#                                Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values 
#                                Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
#                                                       feature Scaling  
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()    
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)
#                                     Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression  
classifier= LogisticRegression(random_state=0)  
classifier.fit(x_train, y_train)
#                                     Predicting the Test Result
y_pred= classifier.predict(x_test)
#                                     Test Accuracy of the result
#        Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix  
cm= confusion_matrix()
#                                      Visualizing the training set result
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),  # range of -1(minimum) to 1 (maximum)
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))  # nm.meshgrid command to create a rectangular grid
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), # mtp.contourf command - To create a filled contour
alpha = 0.75, cmap = ListedColormap(('purple','green' ))) # classifier.predict to show the predicted data points predicted by the classifier
mtp.xlim(x1.min(), x1.max())
mtp.ylim(x2.min(), x2.max())
for i, j in enumerate(nm.unique(y_set)):
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
        c = ListedColormap(('purple', 'green'))(i), label = j)
mtp.title('Logistic Regression (Training set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()

#                                                      Linear Classifier
#              Visualizing the test set result:
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
alpha = 0.75, cmap = ListedColormap(('purple','green' )))
mtp.xlim(x1.min(), x1.max())
mtp.ylim(x2.min(), x2.max())
for i, j in enumerate(nm.unique(y_set)):
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
        c = ListedColormap(('purple', 'green'))(i), label = j)
mtp.title('Logistic Regression (Test set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()

#                                                                                         $   Support Vector Machine
# Kernel : is a function used to map a lower-dimensional data into higher dimensional data
# Hyperplane: SVM is a separation line between two classes
# in SVR, line which helps to predict the continuous variables and cover most of the datapoints
# Boundary lines are the two lines apart from hyperplane, which creates a margin for datapoints
# Support vectors are the datapoints which are nearest to the hyperplane and opposite class
# 2 Types = Linear = dataset can be classified into two classes by using a single straight line, Non-Linear
# Linear SVM = coordinates in either green or blue
# distance between the vectors and the hyperplane is called as margin
# hyperplane with maximum margin is called the optimal hyperplane.
# Non-Linear SVM = 3rd dimension(Z), To find the descision boundary
z=x2 +y2
#                                                                               Implementation of Support Vector Machine
#                                        Data Pre-processing step
#                                                 Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values
y= data_set.iloc[:, 4].values
#                                                   Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
#                                                        feature Scaling  
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)
#                                            Fitting the SVM classifier to the training set
from sklearn.svm import SVC         # "Support vector classifier"  
classifier = SVC(kernel='linear', random_state=0)  
classifier.fit(x_train, y_train)
#                                            Predicting the test set result
y_pred= classifier.predict(x_test)
#                                       Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix  
cm= confusion_matrix(y_test, y_pred)
#                                               Visualizing the training set result
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
alpha = 0.75, cmap = ListedColormap(('red', 'green')))
mtp.xlim(x1.min(), x1.max())
mtp.ylim(x2.min(), x2.max())
for i, j in enumerate(nm.unique(y_set)):
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
        c = ListedColormap(('red', 'green'))(i), label = j)
mtp.title('SVM classifier (Training set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()
#                                   Visualizing the test set result
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = nm.meshgrid(nm.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step  =0.01),
nm.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
mtp.contourf(x1, x2, classifier.predict(nm.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
alpha = 0.75, cmap = ListedColormap(('red','green' )))
mtp.xlim(x1.min(), x1.max())
mtp.ylim(x2.min(), x2.max())
for i, j in enumerate(nm.unique(y_set)):
    mtp.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
        c = ListedColormap(('red', 'green'))(i), label = j)
mtp.title('SVM classifier (Test set)')
mtp.xlabel('Age')
mtp.ylabel('Estimated Salary')
mtp.legend()
mtp.show()

#                                  SVM using Scikit-Learn load iris datasets
# non-linear feature makes SVMs capable of linearly separating the data
# map non-separable data to a higher dimensionality to make it separable and then map back (Kernal trick)
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
iris = load_iris()
#                     Create data
X = iris.data
y = iris.target
#                      Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#                                  Instantiate
svm = SVC(kernel='linear')
#                                  Fit
svm.fit(X_train, y_train)
#                                  Predict 
y_pred = svm.predict(X_test)
#                                  Accuracy calculation
acc = accuracy_score(y_pred, y_test)
acc
#                                                                            Hyperparameters Tuning with Scikit-Learn
# Common kernels = 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'
# C parameter tells the SVM optimization how much you want to avoid misclassifying each training example
# large C = optimizer will choose a smaller-margin hyperplane
# Small C = larger-margin separating hyperplane
# gamma =  how far the influence of a single example reaches
# Low values = Far, Only consider close points
# High values = Low, Even far-away points get considered, You can end up with a wiggly decision boundary (over-fitting)


#                                                                                             $      Decision Tree Regression
# solve problems for both categorical and numerical data
# tree-like structure in which each internal node represents the "test" for an attribute, 
# each branch represent the result of the test, and each leaf node represents the final decision or result
# is constructed starting from the root node/parent node (dataset), which splits into left and right child nodes (subsets of dataset).
# These child nodes are further divided into their children node, and themselves become the parent node of those nodes
# A decision node (e.g., Outlook) has two or more branches
# Leaf node (e.g., Hours Played) represents a decision on the numerical target
#                                                             Standard Deviation
# to calculate the homogeneity of a numerical sample
# Step 1: The standard deviation of the target is calculated (eg)Standard deviation (Hours Played) = 9.32
# Step 2: The resulting standard deviation is subtracted from the standard deviation before the split.
# Step 3: The attribute with the largest standard deviation reduction is chosen for the decision node
# Step 4a: The dataset is divided based on the values of the selected attribute
# Step 4b: "Overcast" subset does not need any further splitting because its CV (8%) is less than the threshold (10%)
#                                                                                           $      Random Forest Regression
# ensemble learning method which combines multiple decision trees and predicts the final output based on the average of each tree output
# g(x)= f0(x)+ f1(x)+ f2(x)+.,,,
# Bagging or Bootstrap Aggregation technique of ensemble learning in which aggregated decision tree runs in parallel and do not interact with each other
# Overfitting in the model by creating random subsets of the dataset
#                                                                                                             Feature Selection
"""Prepare the dataset
Train a random forest classifier
Identify the most important features
Create a new ‘limited featured’ dataset containing only those features
Train a second classifier on this new dataset
Compare the accuracy of the ‘full featured’ classifier to the accuracy of the ‘limited featured’ classifier"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
#                                 Load the iris dataset
iris = datasets.load_iris()
#                                Create a list of feature names
feat_labels = ['Sepal Length','Sepal Width','Petal Length','Petal Width']
X = iris.data #                                  Create X from the features
y = iris.target #                                 Create y from output
X[0:5] #                                   View the features
y # #                                View the target data
#                                                              Split The Data Into Training And Test Sets
#                Split the data into 40% test and 60% training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
#                                                              Train A Random Forest Classifier
# #                            Create a random forest classifier
clf = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
#                                         Train the classifier
clf.fit(X_train, y_train)
#                          Print the name and gini importance of each feature
for feature in zip(feat_labels, clf.feature_importances_):
#                                                      Identify And Select Most Important Features
# Create a selector object that will use the random forest classifier to identify
# features that have an importance of more than 0.15
sfm = SelectFromModel(clf, threshold=0.15)
#                                             Train the selector
sfm.fit(X_train, y_train)
SelectFromModel(estimator=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=10000, n_jobs=-1, oob_score=False, random_state=0,
            verbose=0, warm_start=False),
        prefit=False, threshold=0.15)
# #                                                                  Print the names of the most important features
for feature_list_index in sfm.get_support(indices=True):
    print(feat_labels[feature_list_index])
#                                         Create A Data Subset With Only The Most Important Features
# Transform the data to create a new dataset containing only the most important features
# Note: We have to apply the transform to both the training X and test X data.
X_important_train = sfm.transform(X_train)
X_important_test = sfm.transform(X_test)
# Train A New Random Forest Classifier Using Only Most Important Features
# Create a new random forest classifier for the most important features
clf_important = RandomForestClassifier(n_estimators=10000, random_state=0, n_jobs=-1)
# Train the new classifier on the new dataset containing the most important features
clf_important.fit(X_important_train, y_train)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=10000, n_jobs=-1, oob_score=False, random_state=0,
            verbose=0, warm_start=False)
#                                             Compare The Accuracy Of Our Full Feature Classifier To Our Limited Feature Classifier
#    Apply The Full Featured Classifier To The Test Data
y_pred = clf.predict(X_test)
#                             View The Accuracy Of Our Full Feature (4 Features) Model
accuracy_score(y_test, y_pred)
#                             Apply The Full Featured Classifier To The Test Data
y_important_pred = clf_important.predict(X_important_test)
#                              View The Accuracy Of Our Limited Feature (2 Features) Model
accuracy_score(y_test, y_important_pred)
#                                                                    Random forest creation pseudocode
# Pseudocode to perform prediction from the created random forest classifier
"""Randomly select “k” features from total “m” features.
Where k << m
Among the “k” features, calculate the node “d” using the best split point.
Split the node into daughter nodes using the best split.
Repeat 1 to 3 steps until “l” number of nodes has been reached.
Build forest by repeating steps 1 to 4 for “n” number times to create “n” number of trees."""
#                                                  Random forest prediction pseudocode
"""Takes the test features and use the rules of each randomly created decision tree to predict the oucome and stores the predicted outcome (target)
Calculate the votes for each predicted target.
Consider the high voted predicted target as the final prediction from the random forest algorithm."""
g(x)=f0(x)+f1(x)+f2(x)+..
import graphlab as gl
#                                           Load the data
data =  gl.SFrame.read_csv('https://static.turi.com/datasets/xgboost/mushroom.csv')
#                                         Label 'p' is edible
data['label'] = data['label'] == 'p'
#                                 Make a train-test split
train_data, test_data = data.random_split(0.8)
#                                             Create a model.
model = gl.random_forest_regression.create(train_data, target='label',
                                           max_iterations=2,
                                           max_depth =  3)
#                                             Save predictions to an SArray
predictions = model.predict(test_data)
#                                         Evaluate the model and save the results into a dictionary
results = model.evaluate(test_data)
#                                     visualize the models using
model.show(view="Tree", tree_id=0)
model.show(view="Tree", tree_id=1)
#                                          Tuning hyperparameters
# num_trees, max_depth, step_size, min_child_weight, min_loss_reduction, row_subsample, column_subsample

#                      Regression problem statement
# to build regression algorithms for predicting unemployment within an economy
"""psavert - personal savings rate.
pce - personal consumption expenditures, in billions of dollars.
uempmed - median duration of unemployment, in weeks.
pop - total population, in thousands.
unemploy- number of unemployed in thousands (dependent variable)."""
# two metrics - R-squared value and Root Mean Squared Error (RMSE)
# Step 1 -                                                  Loading the Required Libraries and Modules
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
# Step 2 -                                          Reading the Data and Performing Basic Data Checks
df = pd.read_csv('regressionexample.csv') # reads in the data as pandas dataframe
print(df.shape) #  prints the shape - 574 observations of 5 variables
df.describe()  # summary statistics of the numerical variables
# Step 3 -                                          Creating Arrays for the Features and the Response Variable
# 
target_column = ['unemploy'] # creates an object of the target variable called 'target_column
predictors = list(set(list(df.columns))-set(target_column)) # list of all the features, excluding the target variable 'unemploy'
df[predictors] = df[predictors]/df[predictors].max() # normalizes the predictors, 
df.describe() # summary of the normalized data
# Step 4 -                                           Creating the Training and Test Datasets
#                                  holdout-validation method
X = df[predictors].values  # create arrays of the independent (X) and dependent (y) variables
y = df[target_column].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)  # splits the data into training and test dataset
print(X_train.shape); print(X_test.shape)
# Step 5 -                                  Build, Predict and Evaluate the Regression Model
# Loss function = OLS + alpha * summation (squared coefficient values)
#                                                                                            $       Ridge Regression
# The amount of bias added to the model is known as Ridge Regression penalty
# by multiplying with the lambda to the squared weight of each individual features 
βridge=(X′X+λI)−1(X′Y)
# high collinearity between the independent variables, regularization technique, which is used to reduce the complexity of the model
#                                                                                                    Lasso Regression
# penalty term contains only the absolute weights instead of a square of weights
# it takes absolute values, hence, it can shrink the slope to 0
#                                                                                    Elastic Net Regression
#                                                                                    Linear Regression
rr = Ridge(alpha=0.01)  #                                 instantiates the Ridge Regression model with an alpha value of 0.01
rr.fit(X_train, y_train) #                                fits the model to the training data
pred_train_rr= rr.predict(X_train) #                      predicts
print(np.sqrt(mean_squared_error(y_train,pred_train_rr)))
print(r2_score(y_train, pred_train_rr))  #                print the evaluation metrics
pred_test_rr= rr.predict(X_test)
print(np.sqrt(mean_squared_error(y_test,pred_test_rr))) 
print(r2_score(y_test, pred_test_rr))
#                                                         Fit the linear regression
model = regr.fit(X_std, y)
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
#                                                                                                       Handling Missing data
# deleting the particular row
# calculating the mean
#                             handling missing data (Replacing missing data with the mean value)  
from sklearn.preprocessing import Imputer  
imputer= Imputer(missing_values ='NaN', strategy='mean', axis = 0)  
#                                              Fitting imputer object to the independent variables x.   
imputerimputer= imputer.fit(x[:, 1:3])  
#                                                 Replacing missing data with the calculated mean value  
x[:, 1:3]= imputer.transform(x[:, 1:3])

#                                                                                                   Encoding Categorical data
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
#                                                                                                Encoding for dummy variables  
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
#                                                                                                                 Feature Scaling
# to standardize the independent variables of the dataset in a specific range
# our variables in the same range and in the same scale so that no any variable dominate the other variable.
Euclidean distance between A and B = root value of (x2-x1)2+(y2-y1)2
# two ways to perform feature scaling
# Standardization, Normalization
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()  
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)

#                                                                                                                  ciphertext
# converts the plaintext to ciphertext and ciphertext to plain text
pip install simple-crypt
from simplecrypt import encrypt, decrypt
message = "Hello!! Welcome to AIM!!"
ciphercode = encrypt('AIM', message)
print(ciphercode)
# call the decrypt function and decode the original message from this ciphertext
original = decrypt('AIM', ciphercode)
print(original)
#                                                                                               encryption and decrypting the files
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
