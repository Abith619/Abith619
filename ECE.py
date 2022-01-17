LinearDiscriminantAnalysis on Dataset
——————————–
# Load libraries
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load the Iris flower dataset:
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create an LDA that will reduce the data down to 1 feature
lda = LinearDiscriminantAnalysis(n_components=2)

# run an LDA and use it to transform the features
X_lda = lda.fit(X, y).transform(X)

lda

# Print the number of features
print(‘Original number of features:’, X.shape[1])
print(‘Reduced number of features:’, X_lda.shape[1])

————————————————–

Standard Scalar on lda with Iris Data

—————————————————-

from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(iris.data)

# Create an LDA that will reduce the data down to 1 feature
lda = LinearDiscriminantAnalysis(n_components=2)

Y_lda = lda.fit_transform(X,y)

# Show results
print(‘Original number of features:’, X.shape[1])
print(‘Reduced number of features:’, Y_lda.shape[1])

—————————————————
Variance Thresholding For Feature Selection

—————————————————-

from sklearn import datasets
from sklearn.feature_selection import VarianceThreshold

# Load the Iris flower dataset:
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create VarianceThreshold object with a variance with a threshold of 0.5
thresholder = VarianceThreshold(threshold=0.3)

# Conduct variance thresholding
X_high_variance = thresholder.fit_transform(iris.data)

iris.data

X_high_variance

—————————————————–
Train and Test dataset creation
——————————————————

X = list(range(15))
print (X)

y = [x * x for x in X]
print (y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, train_size=0.65,test_size=0.35, random_state=10)
print (“X_train: “, X_train)
print (“y_train: “, y_train)
print(“X_test: “, X_test)
print (“y_test: “, y_test)

————————————————–
Test and Train dataset creation from iris dataset
—————————————————

# Load libraries
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the digits dataset
iris = datasets.load_iris()

# Create the features matrix
X = iris.data

# Create the target vector
y = iris.target

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,
y,
test_size=0.1,
random_state=1)

X_train
X_test
y_train
y_test

——————————————–
Creating Standardizer with test and train dataset
———————————————–

# Create standardizer
standardizer = StandardScaler()

# Fit standardizer to training set
standardizer.fit(X_train)
# Apply to both training and test sets
X_train_std = standardizer.transform(X_train)
X_test_std = standardizer.transform(X_test)

X_train_std
X_test_std
