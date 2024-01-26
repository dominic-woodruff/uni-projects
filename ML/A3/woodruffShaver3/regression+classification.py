#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:30:51 2023

@author: domin
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV    
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import shuffle



# Returns array containing the 
#   data as an array, target column, Target Name, and Features 
def load(filename):
    arr = pd.read_excel(filename)
    descriptions = list(arr)[1:]
    arr = arr.to_numpy()
    targetcol = arr[:, 1]
    arr = np.delete(arr, obj=0, axis=1)
    sampleNum = len(arr)
    featureNum = len(descriptions)
    target = descriptions[-1:]
    print (target)
    print(featureNum)
    for item in descriptions:
        print(item)
    print(len(arr))
    for num in range(5):
        print(arr[num])
    return [arr, featureNum, descriptions, target, sampleNum, targetcol]

def corrMatrix(arr, descriptions):
    corrs = []
    corrful = []
    arr = pd.DataFrame(arr)
    for (_, columnData) in arr.items():
        for (_, alsocolumnData) in arr.items():
            c = columnData.corr(alsocolumnData)
            corrs.append(round(c, 3))
        corrful.append(corrs)
        corrs = []
    
    corrful = pd.DataFrame(corrful)
    corrful.columns = descriptions 
    corrful.index = descriptions
    print(corrful.to_string())

def regression(arr, X_train, X_test, y_train, y_test):
    ridge = Ridge().fit(X_train, y_train)
    print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))
    
def ridge(arr, targ):
    X_train, X_test, y_train, y_test = train_test_split(
        arr, targ, shuffle=True, random_state=42, train_size=.8, test_size=.2)
    from sklearn.linear_model import Ridge
    grid = {'alpha': [0, 0.1, 1, 10, 20, 50, 100]}
    ridge = Ridge()
    grid_search = GridSearchCV(ridge, grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    ridge = Ridge(0)
    ridge.fit(X_train, y_train)
    
    from sklearn.metrics import confusion_matrix
    print("Training set score: {:.2f}".format(grid_search.score(X_train, y_train)))
    print("Test set score: {:.2f}".format(grid_search.score(X_test, y_test)))
    pred = ridge.predict(X_test)
    #conf = confusion_matrix(y_test, pred)<---Broken confusion matrix code
    #print(conf)
    
    #print best value from ridge model
    print(grid_search.best_estimator_)
    
def lasso(arr, targ):
    X_train, X_test, y_train, y_test = train_test_split(
        arr, targ, shuffle=True, random_state=42, train_size=.8, test_size=.2)
    from sklearn.linear_model import Lasso
    grid = {'alpha': [0, 0.1, 1, 10, 20, 50, 100]}
    lasso = Lasso()
    grid_search = GridSearchCV(lasso, grid, cv=5)
    grid_search.fit(X_train, y_train)
    
    #print best value from lasso model
    print(grid_search.best_estimator_)

def loadBanknote(filename):
    #import the data from the file manually, because that's what the assignment says to do
    
    #open the file
    file = open(filename, "r")

    #create a list to hold the data
    data = []
    features = []
    target = []

    #read the file line by line
    for line in file:
        #split the line into a list of strings
        line = line.split(",")
        #convert the strings to floats
        line = [float(i) for i in line]
        #put the last element off the list and store it as the target
        features.append(line[:])
        target.append(features[-1].pop())
        #add the list to the data
        data.append(line)
    
    #close the file
    file.close()

    #return the data
    return [data, features, target, ["variance", "skewness", "curtosis", "entropy"], "target_class"]

def lassoridge():
    arr = load('realEstateValuationDataSet.xlsx')
    corrMatrix(arr[0], arr[2])
    lasso(arr[0], arr[5])
    ridge(arr[0], arr[5])
    
lassoridge()

bankData = loadBanknote("data_banknote_authentication.txt")

# b) Meet the Data Section: Provide the following information about the data.
# a) Number of features (comes from the load function above)
print("Number of features: " + str(len(bankData[0][0])))
# b) Names of the features (comes from load function above)
print("Names of features: " + str(bankData[3]))
# c) Name of target (comes from load function above)
print("Name of target: " + str(bankData[4]))
# d) Number of samples (comes from the load function above)
print("Number of samples: " + str(len(bankData[0])))
# e) Description of data (comes from load function above)
print("Description of data: " + str(bankData[1]))
# f) First five rows of the data
print("First five rows of the data: " + str(bankData[0][:5]))
# g) Correlation Studies: Present the correlation between each pair of data
# columns including target
corrMatrix(bankData[0], bankData[3] + ["target"])

# c) Model Fitting Perform Logistic regression without cross validation. Split
# the data into 80% training and 20% test. Note that Logistic Regression on
# scikit-learn by default uses L2 penalty of 1. Each time use the same test set
# for comparison. State the accuracy.
from sklearn.linear_model import LogisticRegression

#randomize both the features and the target
bankData[1], bankData[2] = shuffle(bankData[1], bankData[2], random_state=45)

#split the data into 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(bankData[1], bankData[2], test_size=0.2, random_state=45)

#fit the model
model = LogisticRegression().fit(X_train, y_train)

#predict the test data
y_pred = model.predict(X_test)

#calculate the accuracy
print("Accuracy: " + str(accuracy_score(y_test, y_pred)))

# d) Metrics: Logistic Regression can predict class labels or class probabilities
# (Continuous valued prediction) Using class label predictions, compute
print("Classification Report:")
# a) Precision,
# b) Recall,
# c) Sensitivity
# d) Accuracy
print(classification_report(y_test, y_pred, digits=4))

# e) Metrics: Create an ROC curve and find the best threshold as shown below
# (use the same test set as above)
from sklearn.metrics import roc_curve, auc

#calculate the false positive rate and true positive rate
fpr, tpr, thresholds = roc_curve(y_test, y_pred)

#calculate the area under the curve
roc_auc = auc(fpr, tpr)
print("Area under the curve: " + str(roc_auc))

#plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='Logistic (area = %0.2f)' % roc_auc, marker='o')

#plot the line of no discrimination
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='No Skill')

#plot the best threshold
plt.plot(fpr[thresholds == 1.0], tpr[thresholds == 1.0], marker='o', markersize=10, color="black", label="Best")

#set the limits of the axes
plt.xlim([0.0, 1.0])

#set the labels of the axes
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

#legend
plt.legend(loc="lower right")

#show the graph
plt.show()

