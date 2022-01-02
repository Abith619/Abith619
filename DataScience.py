#                                                          Projects
#                                                                   encryption(+) & Decryption(-)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg = ' '
message=input('Enter the Message : ')
for character in message:
    position = alphabet.find(character)
    newposition = (position+key)%26      #   (-) for decryption
    newchar = alphabet[newposition]
    print("Encrypted new character is ",newchar)
    newmsg+=newchar
print("the encrypted final message is ", newmsg)
#                                                                       GUI-Based project using Tkinter
#          basic-Code
from tkinter import *
from typing import Sized
top=Tk()                                          # main class
L1=Label(top,text="UserName")                     # top = area
L1.grid(column=0,row=0)                           # grid = window

E1=Entry(top,bd=5) # text box
E1.grid(column=1,row=0)
E2=Entry(top,bd=5)                                # border = 5
E2.grid(column=2,row=0)
def submit():
    messagebox.showinfo( "CONFIRMATION",E1.get()+"-Your Data")     # def messagebox
redbutton=Button(top,text="Abith Button",fg="red" ,command=submit) # colorbutton, to call this function click this button
redbutton.grid(column=1,row=1)
top.mainloop()
#                                                            To get the Staticstical data
import pandas as pd
import quandl
df = quandl.get("WIKIPEDIA/GOOGL")
print(df.head())

#                                                                                                                        Extract features from Dictionary
import Numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer  # Import Library

staff = [{'Name': 'Abith Raj', 'age': 33}]          # create Dictionary
vec = DictVectorizer()                              # convert Dict to feature Object
vec.fit_transform(staff).toarray()                  # Fit then transform the Dict with vec,then
vec.get_feature_names()                             # View Feature names

#                                                      Creating a Chart
x = np.arange(0,10) 
y = x ^ 2 
#                                                          Simple Plot
plt.plot(x,y)

#                                                   Labling the Axes
x = np.arange(0,10) 
y = x ^ 2 
#                                                  Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#                                                  Simple Plot
plt.plot(x,y)

#                                           Formatting Line type and Colour
x = np.arange(0,10) 
y = x ^ 2 
#                                   Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#                                     Formatting the line colors
plt.plot(x,y,'r')
#                                  Formatting the line type  
plt.plot(x,y,'>')

#                                                                                        Saving the Chart File
x = np.arange(0,10) 
y = x ^ 2 
#                      Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 

#                           Formatting the line colors
plt.plot(x,y,'r')

#                             Formatting the line type  
plt.plot(x,y,'>') 

#                                  save in pdf formats
plt.savefig('timevsdist.pdf', format='pdf')

#                                                                                           Chart Styling
#                                                                         Annotations 
x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 
# Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)

#                            Annotate
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry')

#                                                    Adding Legends
# Whenever you create a chart in Excel, a legend for the chart is automatically generated at the same time. 
x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 
#                                            Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)
#                                              Annotate
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry') 
#                                                 Adding Legends
plt.plot(x,z)
plt.plot(x,t)
plt.legend(['Race1', 'Race2','Race3'], loc=4)

#                                                                        Chart presentation Style
# Pedigree Chart Templates = PPT
#                                                      Style the background
plt.style.use('fast')
plt.plot(x,z)

#                                                            Heatmap
# heatmap contains values representing various shades of the same colour for each value to be plotted as a matrix of values
#                                                 two-dimensional plot of values which are mapped to the indices and columns
data=[{2,3,4,1},{6,3,5,2},{6,3,5,4},{3,7,5,4},{2,8,1,5}]
Index= ['I1', 'I2','I3','I4','I5']
Cols = ['C1', 'C2', 'C3','C4']
df = DataFrame(data, index=Index, columns=Cols)
plt.pcolor(df)
plt.show()

#                                                                                               Bubble Charts - 3D 
# display three variables without using 3D graphs;
#                                                            Drawing a Bubble Chart
DataFrame.plot.scatter()
#                               create data
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = np.random.rand(40) 
#                                        use the scatter function
plt.scatter(x, y, s=z*1000,c=colors)
plt.show()

#                                                              scatter plot, scatter graph, and correlation
#           x = Independent, y = Dependent
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b') 

#                                                                                                              3D Charts
# 3dPlot is drawn by mpl_toolkits.mplot3d to add a subplot to an existing 2d plot.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

chart = plt.figure()
chart3d = chart.add_subplot(111, projection='3d')
#                                                                   Create some test data.
X, Y, Z = axes3d.get_test_data(0.08)
#                                                                      Plot a wireframe.
chart3d.plot_wireframe(X, Y, Z, color='r',rstride=15, cstride=10)
plt.show()

#                                                                      Time Series
# take the value of stock prices every day for a quarter for a particular stock symbol.
# We capture these values as a csv file and then organize them to a dataframe 
# set the date field as index of the dataframe by recreating the additional Valuedate column as index and deleting the old valuedate column
# sample data for the price of the stock on different days of a given quarte
"""valueDate	Price
01-01-2018,	1042.05
02-01-2018,	1033.55
03-01-2018,	1029.7
04-01-2018,	1021.3
05-01-2018,	1015.4
...
...                        # save as stock.csv
...
...
23-03-2018,	1161.3
26-03-2018,	1167.6
27-03-2018,	1155.25
28-03-2018,	1154"""

#                                                                                            Measuring Central Tendency
# center or distribution of location of values of a data set
# chances of a new input fitting into the existing data set and hence probability of success

# Mean - It is the Average value of the data which is a division of sum of the values with the number of values.This function returns the arithmetic average of the data it operates on. If called on an empty container of data, it raises a StatisticsError.
#           is the most frequently used measure of central tendency and generally considered the best measure of it
# Median - It is the middle value in distribution when the values are arranged in ascending or descending order.For data of odd length, this returns the middle item; for that of even length, it returns the average of the two middle items.
#          There are a few extreme scores in the distribution of the data.(
#          There are some missing or undetermined values in your data. c
#          There is an open ended distribution, You have data measured on an ordinal scale   
# Mode - It is the most commonly occurring value in a distribution.This function returns the most common value in a set of data. This gives us a great idea of where the center lies.
#                                                                  Calculating Mean and Median
import pandas as pd
#                                                                  Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#                                                                   Create a DataFrame
df = pd.DataFrame(d)
print "Mean Values in the Distribution"
print df.mean()
print "*******************************"
print "Median Values in the Distribution"
print df.median()
#                                                   Calculating Mode
#C                                           reate a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46])}
#                                                  Create a DataFrame
df = pd.DataFrame(d)
print df.mode()

#                                                                                                 Measuring Variance()
# Statistics module provides very powerful tools, which can be used to compute anything related to Statistics. 
# variance() is one such function. This function helps to calculate the variance from a sample of data (sample is a subset of populated data).
# pvariance() is used to calculate the variance of an entire population
# variance is the squared deviation of a variable from its mean
#          it measures the spread of random data in a set from its mean or median value.
#          A low value for variance indicates that the data are clustered together and are not spread apart widely,
# whereas a high value would indicate that the data in the given set are much more spread apart from the average value.
# It is measured by using standard deviation. The other method commonly used is skewness.
#                                                          Measuring Standard Deviation
# Standard deviation is square root of variance. variance is the average of squared difference of values in a data set from the mean value
#                                                            Calculate the standard deviation
print df.std()
#                                                             Measuring Skewness
# used to determine whether the data is symmetric or skewed. If the index is between -1 and 1, then the distribution is symmetric.
# If the index is no more than -1 then it is skewed to the left and if it is at least 1, then it is skewed to the right
print df.skew()
# the distribution of  rating is symmetric while the distribution of age is skewed to the right

#                                                         Normal Distribution
# presenting data by arranging the probability distribution of each value in the data
# symmetric.scipy.stats.norm() is a normal continuous random variable. It is inherited from the of generic methods as an instance of the rv_continuous class.
# It completes the methods with details specific for this particular distribution
# probability distribution describes how the values of a random variable is distributed.
# It is a statistical function that describes all the possible values and likelihoods that a random variable can take within a given range.
# A probability distribution can be discrete if the set of possible outcomes consists of discrete values(e.g. toss of a coin where the possible outcome of a toss is either head or tail) or
# continuous if the set of possible outcomes consists of real numbers (e.g. humidity measured on a day)
#                                                                               Parameters :
#       q : lower and upper tail probability
#       x : quantiles
#     loc : [optional]location parameter. Default = 0
#   scale : [optional]scale parameter. Default = 1
#    size : [tuple of ints, optional] shape or random variates.
# moments : [optional] composed of letters [‘mvsk’]; ‘m’ = mean, ‘v’ = variance, ‘s’ = Fisher’s skew and ‘k’ = Fisher’s kurtosis. (default = ‘mv’).

# the Central limit theorem : if you have many independent variables that may be generated by all kinds of distributions,
import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
#                                                     Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, normed=True)
#                                                              Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()

#                                                                                 Binomial Distribution
# finding the probability of success of an event which has only two possible outcomes in a series of experiments
# Discrete Distribution, It describes the outcome of binary scenarios
#    n - number of trials.
#    p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.
# Discrete Distribution:The distribution is defined at separate set of events
from scipy.stats import binom
import seaborn as sb

binom.rvs(size=10,n=20,p=0.8)

data_binom = binom.rvs(n=20,p=0.8,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')

#                                                                              Poisson Distribution
# the event can only be measured as occurring or not as occurring,
# meaning the variable can only be measured in whole numbers.Fractional occurrences of the event are not a part of the model
# independent events which occur at a constant rate within a given interval of time
# It estimates how many times an event can happen in a specified time
from scipy.stats import poisson
import seaborn as sb

data_binom = poisson.rvs(mu=4, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Poisson', ylabel='Frequency')

#                                                                                                Bernoulli's Distribution
# only two possible outcomes, namely 11 (success) and 00 (failure), and a single trial
# a coin toss. So the random variable XX which has a Bernoulli distribution can take value 11 
# with the probability of success, pp, and the value 00 with the probability of failure, qq or 1−p1−p.
# The probabilities of success and failure need not be equally likely.
# The Bernoulli distribution is a special case of the binomial distribution where a single trial is conducted (n=1n=1). 
# Its probability mass function is given by : f(k;p) = p^k(1-p)^1-k for k = {0,1}
# generate a bernoulli distributed discrete random variable using scipy.stats module's bernoulli.rvs() method
# which takes pp (probability of success) as a shape parameter. To shift distribution use the loc parameter. 
# size decides the number of times to repeat the trials. 
# If you want to maintain reproducibility, include a random_state argument assigned to a number.
# single experiment is conducted so that the number of observation is 1
from scipy.stats import bernoulli
import seaborn as sb

data_bern = bernoulli.rvs(size=1000,p=0.6)
ax = sb.distplot(data_bern,
                  kde=True,
                  color='crimson',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Bernouli', ylabel='Frequency')

#                                                                                                         P Value
# the strength of a hypothesis. We build hypothesis based on some statistical model and compare the model's validity using p-value.
# One way to get the p-value is by using T-test. p-value for a statistical model is the probability that when the null hypothesis is true
#                                                                        Python Decorators
"""The null hypothesis states that two measured phenomena experience no relationship to each other. We denote this as H or H0. 
One such null hypothesis can be that the number of hours spent in the office affects the amount of salary paid. 
For a significance level of 5%, if the p-value falls lower than 5%, the null hypothesis is invalidated. 
Then it is discovered that the number of hours you spend in your office will not affect the amount of salary you will take home. 
Note that p-values can range from 0% to 100% and we write them in decimals. A p-value for 5% will be 0.05."""
# two-sided test for the null hypothesis that the expected value (mean) of a sample of independent observations ‘a’ is equal to the given population mean, popmean
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print stats.ttest_1samp(rvs,5.0)

Ttest_1sampResult(statistic = array([-1.40184894, 2.70158009]),
pvalue = array([ 0.16726344, 0.00945234]))

# ttest_ind − Calculates the T-test for the means of two independent samples of scores.
# test assumes that the populations have identical variances by default.
#                                                                         $  Two-Sample T-Test vs. a Paired T-Test (Hypothesis)
# two samples must have come from two completely different populations, if your samples are connected in some way, 
# run a paired samples t-test. “Connected” means that you are collecting data twice from the same group, person, item or thing
from scipy import stats
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print stats.ttest_ind(rvs1,rvs2)
# You can test the same with a new array of the same length, but with a varied mean. Use a different value in loc and test the same

#                                                                                                     Correlation
# statistical relationships involving dependence between two data sets
# correlation between the price for a product and its supplied quantity.
# Correlation coefficients quantify the association between variables or features of a dataset.
# Correlation values range between -1 and 1
# Useful as a pointer for further, more detailed research
# magnitude – The larger the magnitude (closer to 1 or -1), the stronger the correlation
#      sign – If negative, there is an inverse correlation. If positive, there is a regular correlation.
# Based on the correlation found, a strong model could be created which easily distinguishes one species from another.
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
#                                       without regression
sns.pairplot(df, kind="scatter")
plt.show()
#                                                                                                 Creating Time Series
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_file/stock.csv')
df = pd.DataFrame(data, columns = ['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']


df.plot(figsize=(15, 6))
plt.show()

#                                                              Geographical Data & visualization
# mpl_toolkits, cartopy
# Cartopy is a Python package for cartography. It will let you process geospatial data, analyze it, and produce maps
# Object-oriented projection definitions.
# Publication quality maps.
# Ability to transform points, lines, polygons, vectors, and images.
#                     $                                         show a portion of the world map showing parts of Asia and Australia
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent((60, 150, 55, -25))   # make the map global rather than have it zoom in to
#                                     extents of any plotted data
ax.stock_img()
ax.coastlines()
ax.tissot(facecolor='purple', alpha=0.8)
plt.show()

#                                                                                                                 $   sparse Graph
# CSGraph = Compressed Sparse Graph
# sparse graph  = collection of nodes, which have links between them
# where each node is a person and is connected to acquaintances;
# images, where each node is a pixel and is connected to neighbouring pixels; points in a high-dimensional distribution,
# where each node is connected to its nearest neighbours and practically anything else you can imagine.
# The matrix G is of size N x N, and G[i, j] gives the value of the connection between node ‘i' and node ‘j’
#      Isomap                      − A manifold learning algorithm, which requires finding the shortest paths in a graph.
#      Hierarchical clustering     − A clustering algorithm based on a minimum spanning tree.
#      Spectral Decomposition      − A projection algorithm based on sparse graph laplacians.
#                                                                     create graph with three nodes
G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],          # node 0 and 1 are connected by an edge of weight 2
                     [1, 0, 0] ])         #   nodes 0 and 2 are connected by an edge of weight 1
G_masked = np.ma.masked_values(G_dense, 0)
from scipy.sparse import csr_matrix
G_sparse = csr_matrix(G_dense)
print G_sparse.data 

# nodes 0 and 2 are connected by an edge of zero weight
from scipy.sparse.csgraph import csgraph_from_dense
G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print G2_sparse.data
#                                                                 Chi Square Test
# test of statistical significance for categorical variables
# testing relationships between categorical variables
# he Test of Independence assesses whether an association exists between the two variables
# by comparing the observed pattern of responses in the cells to the pattern that would be expected 
# if the variables were truly independent of each other
# fo = the observed frequency (the observed counts in the cells)
# and fe = the expected frequency if NO relationship existed between the variables
# Calculating the Chi-Square statistic and comparing it against a critical value from the Chi-Square distribution allows the researcher to assess whether the observed cell counts are significantly different from the expected cell counts
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig,ax = plt.subplots(1,1)

linestyles = [':', '--', '-.', '-']
deg_of_freedom = [1, 4, 7, 6]
for df, ls in zip(deg_of_freedom, linestyles):
  ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

plt.xlim(0, 10)
plt.ylim(0, 0.4)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Chi-Square Distribution')

plt.legend()
plt.show()



#                                                                             Processing csv Data
data = pd.read_csv('filepath')
print(data)
print(data[0:5]['salary'])                                    # slice the result for first 5 rows, dtype: float64
#                                                                      DictReader class
#                                                              reading specific columns
print(data.loc[:,['salary','name']])                        # multi axes indexing function
# reading specific columns for range of rows
print(data.loc[:,['salary','name']])

# JSON (JavaScript Object Notation)
# create a sample json file .json
"""
{ 
   "ID":["1","2","3","4","5","6","7","8" ],
   "Name":["Rick","Dan","Michelle","Ryan","Gary","Nina","Simon","Guru" ]
   "Salary":["623.3","515.2","611","729","843.25","578","632.8","722.5" ],
   
   "StartDate":[ "1/1/2012","9/23/2013","11/15/2014","5/11/2014","3/27/2015","5/21/2013",
      "7/30/2013","6/17/2014"],
   "Dept":[ "IT","Operations","IT","HR","Finance","IT","Operations","Finance"]
}
""" # .json
#                                                                                                    pd.read_json()
import pandas as pd
data = pd.read_json('path/input.json')
print (data)
#                                                                                            Reading Specific Columns and Rows
data = pd.read_json('path/input.xlsx')                      # Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])
#                                                                          Reading JSON file as Records
data = pd.read_json('path/input.xlsx')
print(data.to_json(orient='records', lines=True))

data = pd.read_excel('path/input.xlsx')                                     # Reading an Excel File
print (data)
# Reading Specific Columns and Rows
data = pd.read_excel('path/input.xlsx')   #                         Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])
#                                                                   Reading Multiple Excel Sheets
with pd.ExcelFile('C:/Users/Rasmi/Documents/pydatasci/input.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
print("****Result Sheet 1****")
print (df1[0:5]['salary'])
print("")
print("***Result Sheet 2****")
print (df2[0:5]['zipcode'])

#                                                                  Word Tokenization
# Tokenization is the process of replacing sensitive data with 
# unique identification symbols that retain all the essential information about the data.
# booster the security of credit card and e-commerce transactions while minimizing the cost and complexity
# Word tokenization is the process of splitting a large sample of text into words.
# text into a list of tokens. 
# Text into sentences tokenization
# Sentences into words tokenization
# Sentences using regular expressions tokenization
import nltk
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)

#                                                          Tokenizing Sentences
import nltk
sentence_data = "Sun rises in the east. Sun sets in the west."
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)

#                                                       Box Plot
# median, upper quartile, lower quartile, minimum and maximum data values.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')

#                                                                       Processing Unstructued Data
#                 Reading Data
filename = 'path\input.txt'  

with open(filename) as fn:  

#                                                          Read each line
   ln = fn.readline()

#                                                       Keep count of lines
   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1

#                                            Counting Word Frequency
from collections import Counter

with open(r'pathinput2.txt') as f:
   p = Counter(f.read().split())
   print(p)

#                                                                                           Natural Language Processing
# agreed, agreeing and agreeable have the same root word agree
#                                                 Stemming 
# normalization for words, variation according to the context or sentence are normalized.
#                                                               Lemmatization 
# finding the lemma of a word depending on their meaning
# Text preprocessing includes both stemming as well as lemmatization
"""Stemming algorithm works by cutting the suffix from the word. In a broader sense cuts either the beginning or end of the word.

On the contrary, Lemmatization is a more powerful operation, and it takes into consideration morphological analysis of the words.
 It returns the lemma which is the base form of all its inflectional forms."""
# linguistic knowledge is required to create dictionaries and look for the proper form of the word. Stemming is a general operation
#  while lemmatization is an intelligent operation where the proper form will be looked in the dictionary
# Text Mining is the process of analysis of texts written in natural language and extract high-quality information from text.
# text categorization, text clustering, concept/entity extraction, production of granular taxonomies, sentiment analysis,
# document summarization, and entity relation modeling (i.e., learning relations between named entities)
#                                        Information Retrieval (IR) Environments
#                                                 Sentiment Analysis
# Sentiment Analysis is the analysis of people's reviews and comments about something.
# It is widely used for analysis of product on online retail shops.
# Stemming and Lemmatization is used as part of the text-preparation process before it is analyzed.

#                                                                      Document clustering
# Automatic document organization, topic extraction, and fast information retrieval or filtering
# document is prepared through tokenization, removal of stop words
# and then Stemming and Lemmatization to reduce the number of tokens that carry out the same information and hence speed up the whole process

#                                                        Porter Stemming Algorithm for stemming
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
#                                                         First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#                                                          Next find the roots of the word
for w in nltk_tokens:
       print "Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w))

#                                   Lemmatization = brings context to the words by Linking words with similar meaning to one word.
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       print "Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w))



#                                                                                          Relational Databases - SqlAlchemy
# raw sql, SQL Expression Language,
# Orm - Object-relational mapping, translates data between different system types
#                                                                           Reading Relational Tables
"""
1. data replication between a master database and one or more read-only slave instances
2. advanced column types that can efficiently store semi-structured data such as JavaScript Object Notation (JSON)
3. sharding, which allows horizontal scaling of multiple databases that each serve as read-write instances at the cost of latency in data consistency
4. monitoring, statistics and other useful runtime information for database schemas and tables"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')                 # Create the db engine
data = pd.read_csv('/path/input.csv')
data.to_sql('data_table', engine)                            # Store the dataframe as a table
#                                                              Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)
print('')
#                                                             Query 2 on the relational table
res2 = pd.read_sql_query('SELECT dept,sum(salary) FROM data_table group by dept', engine)
print('Result 2')
print(res2)
#                                                                Inserting Data to Relational Tables
from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd
data = pd.read_csv('C:/Users/Rasmi/Documents/pydatasci/input.csv')
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine) #        Store the Data in a relational table
# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])
#                                       Read from the relational table
res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)
#                                                        Deleting Data from Relational Tables
data = pd.read_csv('C:/Users/Rasmi/Documents/pydatasci/input.csv')
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine)

sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Gary')])

res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)

#                                                                                                  NoSql Database
#                                                                                        Inserting Data
#                                   Import the python libraries
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()                             # Choose the appropriate client


db=client.test                                     # Connect to the test db 

#                                              Use the employee collection
employee = db.employee
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

#                                                Use the insert method
result = employee.insert_one(employee_details)

#                                                Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)

#                                                                                  Updating Data
# update mode (lock type), cursor type, and cursor location.
# save any changes you have made to the current record of a Recordset object since calling the AddNew method
# or since changing any field values in an existing record. The Recordset object must support updates.
#                                                             Use the condition to choose the record and use the update method                                                
db.employee.update_one(
        {"Age":'42'},
        {
        "$set": {
            "Name":"Srinidhi",
            "Age":'35',
            "Address":"New Omsk, WC"
        }
        }
    )

Queryresult = employee.find_one({'Age':'35'})

pprint(Queryresult)

#                                                                              Deleting Data
#                                             Use the delete method
db.employee.delete_one({"Age":'35'})

Queryresult = employee.find_one({'Age':'35'})

pprint(Queryresult)

#                                                                                        date, time, calendar
#                               Date Time Representation
# Two simple examples of this format = (2007-03-04 20:32:17, 20070304T203217)
import datetime

print 'The Date Today is  :', datetime.datetime.today()

date_today = datetime.date.today()
print date_today
print 'This Year   :', date_today.year
print 'This Month    :', date_today.month
print 'Month Name:',date_today.strftime('%B')
print 'This Week Day    :', date_today.day
print 'Week Day Name:',date_today.strftime('%A')

#                                                             Date Time Arithmetic

day1 = datetime.date(2018, 2, 12)              # Capture the First Date
print 'day1:', day1.ctime()

day2 = datetime.date(2017, 8, 18)             # Capture the Second Date
print 'day2:', day2.ctime()

print 'Number of Days:', day1-day2            # Find the difference between the dates


date_today  = datetime.date.today() 
 
no_of_days = datetime.timedelta(days=4)       # Create a delta of Four Days 

before_four_days = date_today - no_of_days    # Use Delta for Past Date
print 'Before Four Days:', before_four_days 
 
after_four_days = date_today + no_of_days     # Use Delta for future Date
print 'After Four Days:', after_four_days

#                                                                          Date Time Comparison
import datetime
date_today  = datetime.date.today() 
print 'Today is: ', date_today

no_of_days = datetime.timedelta(days=4)  # Create a delta of Four Days 

before_four_days = date_today - no_of_days                                   # Use Delta for Past Date
print 'Before Four Days:', before_four_days 
after_four_days =  date_today + no_of_days
date1 = datetime.date(2018,4,4)
print 'date1:',date1              
if date1 == before_four_days :
    print 'Same Dates'
if date_today > date1:
    print 'Past Date'
if date1 < after_four_days:
    print 'Future Date'

#                                                                                                     Data Wrangling
#                          merging, grouping, concatenating
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print left
print right
# merge two data frames (datasets) horizontally with the merge function
#                                                                syntax
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

#                                                                          Grouping Data
#                                                              group the data by year and then get the result for a specific year
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print grouped.get_group(2014)

#                                                                                Concatenating Data
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two])

#                                                                                  Data Aggregation
# sum(), mean(), median(), min(), and max() = Computing Aggreations
#                                                                              Applying Aggregations on DataFrame
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print df

r = df.rolling(window=3,min_periods=1)
print r

#                                       Apply Aggregation on a Whole Dataframe
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df

r = df.rolling(window=3,min_periods=1)
print r.aggregate(np.sum)

#                                                     Apply Aggregation on a Single Column of a Dataframe
#                          Spark data frames provide an agg() 
# where you can pass a Map [String,String] (of column name and respective aggregate operation ) as input
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df
r = df.rolling(window=3,min_periods=1)
print r['A'].aggregate(np.sum)

#                                                 Apply Aggregation on Multiple Columns of a DataFrame
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df
r = df.rolling(window=3,min_periods=1)
print r[['A','B']].aggregate(np.sum)

#                                                         Reading HTML Pages
#  Beautiful Soup is a library that makes it easy to scrape information from web pages
#                         Reading the HTML file
import urllib2
from bs4 import BeautifulSoup
#                                                                               Fetch the html file
response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()
#                                                                              Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')
#                                                                              Format the parsed html file
strhtm = soup.prettify()
#                                                                             Print the first few characters
print (strhtm[:225])

#                                                             Extracting Tag Value
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print (soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

#                                                                 Extracting All Tags
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all('b'): print(x.string)




#                                                                                                        DocStrings
# Doc strings are carried with executing code
# We can use triple-quoting to create doc strings that span multiple lines
def foo():                                                                      # docstring tool
""" """
pass
class Data:
   """ """
print(foo.__doc__)
print(Data.__doc__)                                                          # Accessing docstrings
#                                                $  Working with files
With open("myfile.txt", "w") as myfile:
Print(“Hello!”,file=myfile)

With open(‘myfile.txt’, ‘w’) as myfile:
myfile.write(“Hello!”)

With open(‘myfile.txt’, ‘r’) as myfile:
data = myfile.read()

#                                                                                                                              # Load Iris Datasets
from sklearn.datasets import load_iris

iris = load_iris()
iris
x = iris.data
x[0]
#                                                                                                                        Create Histogram using Iris Data Sets
iris.feature_names  #
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)                     # create Data-Frames
iris_df['sepal length (cm)'].hist(bins=30)                                        # draw the Histogram
#                                                                                                                         simulated Data for Classification
from sklearn.datasets import make_classification
features, output = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=5, n_classes=3, weights=[.2, .3, .8])
pd.DataFrame(features).head()
#                                                                                                                            simulated Data for Clustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=200, n_features=2, centers=3, cluster_std=0.5, shuffle=True)
plt.scatter(X[:, 0], X[:, 1])
#                                                                                                                         simulated Data for Regression
from sklearn.datasets import make_regression
from matplotlib import pyplot

X, y = make_regression(n_samples=100, n_features=1, noise=0.1)                       # generate regression datasets
pyplot.scatter(X, y)                                                                 # plot regression datasets
pyplot.show()
#                                                                                                                                 dot product of Matrix
import numpy as np

vector_a = np.array([1, 2, 3])                       # create vector
vector_b = np.array([4, 5, 6])
np.dot[vector_a, vector_b]
vector_a @ vector_b                                  # calculate dot product

# list of values are added & divided by the total no of columns                                                                   mean-Manipulation

import pandas as pd
from scipy import stats
data = {
   'name': ['Abith', '',
            '', 'Abi',                                              # create dataframe with two values
            '', 'Raj'],
   "ID": [6, 1, 9]
   }
df = pd.DataFrame(data)
df                                                                # create mean & trim data
df['ID'].nean()                                                       # calc_non-trimmed mean value
stats.trim_mean(df['score'], proportiontocut=0.2)                                            # trim off the 20 % scores
stats.trimboth(df['score'], proportiontocut=0.2)             # trim off the 20 % scores & view non-trimmed mean values

stats.trim1(df['score'], proportiontocut=0.2, tail="right").mean()                   # trim specific data
stats.trim1(df['name'], proportiontocut=0.2, tail="right")
trim(DataFrameColumn, RemovePercentage, remove(data).mean()                                           # calculate mean
                                                                                                                          # probability mass function
import matplotlib.pyplot as plt;
data = [6,1,9];                                                       # create Dictionary = data + key value pair
count = {}
for observation in data:                                                              # create Dictionary
   count[observation] = count.get(observation, 0) + 1
   n = len(data)
probability_mass_function = {}                                      # initialize the dictionary
for unique_value, count in count.items():                                        # create probability_mass_function
   probability_mass_function[unique_value] = count /n  # loop through unique values of array & calculate probability_mass_function
plt.bar(list(columns), prob.values(), color='g')                       # plot probability_mass_function
plt.show():

#                                                                $ Data Operations using numpy
numpy.array()

a = np.array([[1, 2], [3, 4]])
print (a)
# minimum dimensions
a = np.array([1, 2, 3,4,5], ndmin = 2)
print a
#                                                                     dtype parameter
a = np.array([1, 2, 3], dtype = complex)
print a
#                                              Series in pandas
#
pandas.Series( data, index, dtype, copy)    # series = 1d array's
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s
# pandas data = series, dataFrame, panel, size-mutable, heterogeneous tabular data
# Labeled axis (rows, columns)
# labels must be hashable type, label-indexing
# axis labels = index
pandas.DataFrame( data, index, columns, dtype, copy)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}  #  Data Operations in Pandas
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
# panel = 3D container of Data
# transform wide format into long(stacked) as DataFrames
# column = panel items, index = panel's major and minor axis
#pandas - pan(el)-da(ta)-s
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
       'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p

#                                                                                              Python Data Cleansing & Missing datas
# using re indexing create dataframe With missing values
# NAN = not an number
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df
# check for missing values = isnull(0, NOTNULL()
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                         # Check for Missing Values
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df['one'].isnull()
#                                                                                      CLEANING / FILLING MISSING DATA
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
                                                                       'two', 'three'])
df = df.reindex(['a', 'b', 'c'])                             # Replace NaN with a Scalar Value
print df
print ("NaN replaced with '0':")  # replace "NAN" with "0"
print df.fillna(0)  # "fill" in NA values with non-null data
# pad/fill = fill forward
# bfill/backfill = fill backwards
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                    # Fill NA Forward and Backward
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df.fillna(method='pad')
# dropNA()
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                      # Drop Missing Values
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df.dropna()
# replace({1000:6,2000:1,3000:9})
df = pd.DataFrame({'one':[10,20,30,40,50,2000],                     # Replace Missing (or) Generic Values
                  'two':[1000,0,30,40,50,60]})
print df.replace({1000:10,2000:60})
#                                                                                                              Analyze baby name trends with Data Science
Mary,F,7065
Anna,F,2604
Emma,F,2003
Elizabeth,F,1939
Minnie,F,1746
Margaret,F,1578
Ida,F,1472
Alice,F,1414
Bertha,F,1320
Sarah,F,1288
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
names1880 = pd.read_csv("./babynames/yob1880.txt",
                       names=["name", "sex", "births"])
names1880.head()
names1880.groupby("sex").sum()
years = range(1880, 2019)
pieces = []
columns = ["name", "sex", "births"]
for year in years:
   path = rf"./babynames/yob{year}.txt"
   frame = pd.read_csv(path, names=columns)
   frame['year'] = year
   pieces.append(frame)
names = pd.contact(pieces, ignore_index=True)
names.head()
plt.figure(figsize=(15, 8))_ = sns.barplot(y-names.groupby("year").sum().values[-10:].rave1(), x=list(years)[-10:])
plt.ylabel("number of births")
plt.xlabel("year")_ - plt.title("number of births- (2009-2018)")

#                                                                                                                          Projects
#                                                       GUI Based Encryption & Decryption
from tkinter import *
top=Tk()
L1=Label(top,text="UserName")
L1.grid(column=0,row=0)                           # grid = window

E1=Entry(top,bd=5)
E1.grid(column=1,row=0)
alphabet ='abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg= ''
E2=Entry(top,bd=5)                                # border = 5
E2.grid(column=2,row=0)

def submit():
    messagebox.showinfo( "CONFIRMATION",E1.get()+"- Your Data")     # def messagebox
    global newmsg
    for character in E1.get():
        position = alphabet.find(character)
        newposition = (position+key)%26    # (-) for decryption
        newchar = alphabet[newposition]
        print("Encrypted new character is ",newchar)
        newmsg+=newchar
print(newmsg)
E2.insert(0, newmsg)
redbutton=Button(top,text="Abith Button",fg="red" ,command=submit) # colorbutton
redbutton.grid(column=1,row=1)
top.mainloop()
#                                                                                                                 image Processing
from PIL import image
import glob
image_list = []
for filename in glob.glob("/run/media/abith/Abith/py/my.jpg"):
    im=image.open("/run/media/abith/Abith/py/my.jpg")
    image.show();
#                                                                             tRANSPOSING iMAGE
transposed_img = image.transpose(Image.FLIP_LEFT_RIGHT)
#                                                                              Save  transposed image
transposed_img.save("transposed.jpg")
transposed_img.show()
# 
from PIL import image
image = image.open("my.jpg")  # import image
width, height = image.size  # finding Size
area = (0, 0, width/2, height/2) 
img = image.crop(area)       # cropping
img = image.resize((int(width/4), int(height/4)))                # Resizing the Image
#           Saved in same Relative Location
img.save("cropped_picture.jpg")
img.show();

# 

#                                                                                                                   R programing...
print(sample=(1:3)) # Generate series of sample values in a given rage
print(sample=(1:3, size=3, prob=c(1,3), replace=False))                    # With duplicate values = True
#                                                         prob = probability
#                                                       Already In-Built Datasets
print(head(mtcars))
#                                                         Generating the Datasets
print(matrix(runif(6*3), nrow=6, ncol=3))
input <-mtcars[,c("mpg","disp","hp","wt")]
print(head(input))

input <-mtcars[,c("mpg","disp","hp","wt")]
model <-lm(mpg~disp+hp+wt,data=input) # intercept(mpg)
print(model)
cat("####the co-efficient values are","\n")
a<-coef(model)[1]
print(a)
Xdisp<-coef(model)[2]
Xhp<-coef(model)[3]
Xwt<-coef(model)[4]
print(Xdisp)
print(Xhp)
print(Xwt)
#                                    for a car with disp = 221, hp = 102, wt = 2.91 The predicted Milleage is,,,,,............
Y = a + X1.Xdisp + X2.Xhp + X3.Xwt
Y = 37.105505 + (221*-0.000937) + (102* -0.0.32257) + (2.91* -3.8008g1)
