#Dominic Woodruff
import matplotlib  
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets




def step_func(z):
    return 1.0 if (z > 0) else 0.0

def perceptron(x, y, lr, epochs):
    
    #x -> inputs
    #y -> labels/target
    #lr -> learning rate
    #epochs -> Number of iterations

    #m-> number of training examples
    #n-> number of features 
    m, n = x.shape

    #initialize theta as an array of zeros
    theta = np.zeros((n+1,1))

    #stores missclassified
    n_miss_list = []

    #training
    for _ in range(epochs):
        n_miss = 0

        for idx, x_i in enumerate(x):

            #inserting 1 for bias, x0 = 1
            x_i = np.insert(x_i, 0, 1).reshape(-1,1)

            #calculating prediction/hypothesis
            y_hat = step_func(np.dot(x_i.T, theta)) #dot product of an x sample transposed and theta

            #updating if the example is misclassified
            if (np.squeeze(y_hat) - y[idx]) != 0:
                theta += lr*((y[idx] - y_hat)*x_i)

                n_miss += 1

        #appending number of misclassified examples
        #at every iteration
        n_miss_list.append(n_miss)

    return theta, n_miss_list #n_miss_list could be used for seeing how well the data preforms after training

def plot_decision_boundary(x, theta):
    
    #x -> Inputs
    #theta -> parameters
    
    #the Line is y=mx+c
    #so, Equate mx+c = theta0.x0 + theta1.x1 + theta2.x2
    #Solving we find m and c
    x1 = [min(x[:,0]), max(x[:,0])]
    m = -theta[1]/theta[2]
    c = -theta[0]/theta[2]
    x2 = m*x1 + c
    
    #plotting
    fig = plt.figure(figsize=(10,8))
    plt.plot(x[:, 0][y==0], x[:, 1][y==0], "r^")#r^ = red triangles
    plt.plot(x[:, 0][y==1], x[:, 1][y==1], "bs")#bs = blue squares
    plt.xlabel("feature 1")
    plt.ylabel("feature 2")
    plt.title("Perceptron Algorithm")
    
    plt.plot(x1, x2, 'y-')

###This dataset import can be exchanged with any other input data
x, y = datasets.make_blobs(n_samples=150,n_features=2,
                           centers=2,cluster_std=1.1,
                           random_state=2)
#Plotting
fig = plt.figure(figsize=(10,8))
plt.plot(x[:, 0][y == 0], x[:, 1][y == 0], 'r^')#r^ = red triangles
plt.plot(x[:, 0][y == 1], x[:, 1][y == 1], 'bs')#bs = blue squares
plt.xlabel("feature 1")
plt.ylabel("feature 2")
plt.title('Random Classification Data with 2 classes')

theta, miss_l = perceptron(x, y, 0.5, 100) ##.5 = learning rate, 100 = epochs
plot_decision_boundary(x, theta)
plt.show()