#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:47:27 2023

@author: domin
"""

#Using breast cancer dataset

import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold

from math import sqrt
from math import floor
from statistics import mean

def train_model(arr):
    X_train, X_test, y_train, y_test = train_test_split(
        arr[0], arr[1], stratify=arr[1], shuffle=True, random_state=42, train_size=.8, test_size=.2)
    training_accuracy = []
    test_accuracy = []
    #try n_neighbors from 1 to sqrt(n) + 3
    maxsize = floor(sqrt(len(arr[0]) + 3))
    neighbors_settings = range(1, maxsize)
    
    for n_neighbors in neighbors_settings:
        #build the model
        clf = KNeighborsClassifier(n_neighbors=n_neighbors)
        clf.fit(X_train, y_train)
        #record training set accuracy
        training_accuracy.append(clf.score(X_train, y_train))
        #record generalization accuracy
        test_accuracy.append(clf.score(X_test, y_test))
        
    plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
    plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()
    plt.show()
    
    
def stratkfoldval(arr):
    skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)
    skf.get_n_splits(arr[0], arr[1])
    training_accuracy = []
    test_accuracy = []
    for i, (train_index, test_index) in enumerate(skf.split(arr[0], arr[1])):
        #build the model
        clf = KNeighborsClassifier(n_neighbors=11)
        clf.fit(arr[0][train_index], arr[1][train_index])
        #record training set accuracy
        training_accuracy.append(clf.score(arr[0][train_index], arr[1][train_index]))
        #record generalization accuracy
        test_accuracy.append(clf.score(arr[0][test_index], arr[1][test_index]))
            
    plt.plot(range(1, 6), training_accuracy, label="training accuracy")
    plt.plot(range(1, 6), test_accuracy, label="test accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("fold")
    plt.xticks([1, 2, 3, 4, 5])
    plt.legend()
    plt.show()
    
    print("Training accuracy: ", training_accuracy)
    print("Mean training accuracy", mean(training_accuracy))
    print("Test accuracy: ", test_accuracy)
    print("Mean test accuracy: ", mean(test_accuracy))


# Returns array containing the 
#   data as an array, target column, Target Name, and Features 
def loadCSV(filename):
    arr = np.loadtxt(filename, delimiter=",", dtype=str)
    arr = np.delete(arr, obj=0, axis=1)
    target = arr[1:,0]
    targetname = arr[:,0][0]
    features = arr[0]
    arr = np.delete(arr, obj=0, axis=0)
    arr = np.delete(arr, obj=0, axis=1)
    arr = arr.astype(float)
    return [arr, target, targetname, features]

# Plots the features of the data
def plot_features(data, featureNo1, featureNo2):
    # Map the target names to integers
    target = data[1]
    targetname = data[2]
    features = data[3]
    
    # map target short name to long name
    np.place(target, target == "M", "Malignant")
    np.place(target, target == "B", "Benign")

    # Plot the data using matplotlib plot method
    for target in set(data[1]):
        # Filter the data by target class
        filtered_data = data[0][data[1] == target]
        
        # Plot the filtered data with a label, marker, and color
        plt.plot(filtered_data[:,featureNo1], filtered_data[:,featureNo2], label=target, marker="o", linestyle="")
    
    plt.xlabel(features[featureNo1])
    plt.ylabel(features[featureNo2])
    plt.title(targetname + " Dataset")
    
    # Add a legend with the target names
    plt.legend(loc="best")
    
    plt.show()



# Step 1: Selecting the Dataset: Breast Cancer Wisconsin (Diagnostic) Data Set
print("From Breast Cancer Wisconsin Diagnostic Data Set")

# Step 2: Loading the Dataset
data = loadCSV("wdbc.csv")

# Step 3: Meet the Data
# a. Number of features
print("\nNumber of features: ", str(len(data[3])))

# b. List all the features
print("\nFeatures: ", str(data[3]))

# c. Name of target column
print("\nTarget column: ", str(data[2]))

# d. Number of samples
print("\nNumber of samples: ", str(len(data[0])))

# e. First 5 rows of data
print("\nFirst 5 rows of data: \n", data[0][range(0, 5), :])

# f. Histograms of the first 2 features
print("\n\nHistograms of the first 2 features:")

plt.hist(data[0][:,1])
plt.xlabel(data[3][1])
plt.ylabel("Frequency")
plt.show()

plt.hist(data[0][:,2])
plt.xlabel(data[3][2])
plt.ylabel("Frequency")
plt.show()

# g. Scatter plot of two influential features
print("\n\nScatter plot of two influential features:")
plot_features(data, 2, 6)

# Step 4: Model Development and Training
print("\n\nAccuracy per n-neighbors")
train_model(data)

# Step 5: k-NN with Cross Validation
print("\n\nAccuracy per fold")
stratkfoldval(data)