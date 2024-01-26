#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:31:01 2023

@author: domin
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# 1. Provided is a dataset for regression. The task is to predict sale price of homes.
def loadCSV(filename):
    arr = np.loadtxt(filename, delimiter=",", dtype=str)
    targetName = arr[0, -1]
    target = arr[:, -1]
    target = target[1:]
    arr = np.delete(arr, obj=-1, axis=1)#delete target col
    headers = arr[0]
    arr = np.delete(arr, obj=0, axis=0)
    return arr, target, targetName, headers

# 2. Provide a Meet the Data Section to introduce the data. Show visual displays with histograms for selected features.
def histograms(df):
    for col in df.columns:
        df.hist(column=col)
        plt.show()
        
# 3. Fill in missing information in the dataset if there are any. Explain why you chose to fill the data the way you chose.
def fill_missing_data(df):
    # mark cells with the contents 'NA' as missing
    df = df.replace('NA', np.nan)
    # fill missing data with mean
    df = df.fillna(df.mode().iloc[0])

    return df


# 4. Remove all columns that have very little correlation with the target. Remove 30% of the features. Show visual display of univariate correlation numbers.
def remove_columns(df, target):
    target = target.astype(float)
    # iterate through each coloumn to see if it is numeric
    dfc = df.copy()
    for col in dfc.columns:
        # try to convert the column to a float
        try:
            dfc[col] = dfc[col].astype(float)
        except ValueError:
            # if it fails, it is not numeric
            dfc = dfc.drop(columns=col)
    # calculate the correlation between each column and the target
    cols = []
    corr = []
    for col in dfc.columns:
        cols.append(col)
        corr.append(abs(dfc[col].corr(target['SalePrice'])))
    # create a dataframe of the correlation values
    dfc = pd.DataFrame({'col': cols, 'corr': corr})
    # sort the dataframe by correlation values
    dfc = dfc.sort_values(by=['corr'], ascending=False)
    # remove the columns with the lowest correlation
    dfc = dfc.iloc[0:int(len(df.columns) * 0.3)]
    # remove the columns from the original dataframe
    for col in df.columns:
        if col in dfc['col'].values:
            df = df.drop(columns=col)
    
    return df
    

# 5. Use column transformation for each column as needed: one hot encoding, standard scalar etc.
def column_transformation(df):
    # get list of categorical columns by checking if the column cannot be converted to a float
    cat_cols = []
    num_cols = []
    for col in df.columns:
        try:
            df[col].astype(float)
            num_cols.append(col)
        except ValueError:
            cat_cols.append(col)
    # one hot encode the categorical columns
    df = pd.get_dummies(df, columns=cat_cols)

    # standard scalar for numerical data
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df


# 6. Using model based feature selection (use linear regression as your base model), select only top 50% of the remaining features. Show visuals to indicate which ones they are.
def model_based_feature_selection(df, targ):
    RFE_selector = RFE(estimator=LinearRegression(), n_features_to_select=int(len(df.columns) * 0.5), step=10, verbose=5)
    RFE_selector.fit(df, targ)
    
    # get the selected features
    selected_features = df.columns[RFE_selector.support_]
    # remove the unselected features
    df = df[selected_features]

    tree_based_model(df, targ)

    return df

def linearModel(df, targ):
    X_train, X_test, y_train, y_test = train_test_split(
        df, targ, shuffle=True, random_state=42, train_size=.8, test_size=.2)
    reg = LinearRegression().fit(X_train, y_train)
    return reg.score(X_test, y_test)


# 7. Use PCA (Principal component Analysis) on the remaining features. Number of PCA would be 10% of the remaining features.
def pca(df):
    # find the number of features to use for PCA
    num_features = int(len(df.columns) * 0.1)
    # perform PCA
    pca = PCA(num_features)
    pca.fit(df)
    # transform the data
    dfa = pca.transform(df)

    return dfa


# 8. Now use any non-linear model SVM, Tree Based Model, NN etc with parameter tuning to get best performance. Show a chart indicating the performance of each. Use model metrics that you learned in the previous assignment.
def tree_based_model(df, targ):
    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        df, targ, shuffle=True, random_state=42, train_size=.8, test_size=.2)
    # create the model
    model = RandomForestRegressor(n_estimators=65, random_state=42)
    # train the model
    model.fit(X_train, y_train)
    # predict the test data
    y_pred = model.predict(X_test)
    # transpose y_test
    # calculate the calculate the score
    y_test = np.array(y_test.astype(float)).T[0]
    print('R2 score', model.score(X_test, y_test))

    # plot the predicted vs actual values
    plt.scatter(y_test, y_pred)


# function to run the program
def main():
    data = loadCSV('houseSalePrices.csv')
    df = pd.DataFrame(data[0], columns=data[3])
    print(df.shape)
    df = fill_missing_data(df)
    df = remove_columns(df, pd.DataFrame(data[1], columns=[data[2]]))
    df = column_transformation(df)
    df = model_based_feature_selection(df, pd.DataFrame(data[1], columns=[data[2]]))
    histograms(df)
    df = pca(df)
    tree_based_model(df, pd.DataFrame(data[1]))  

main()