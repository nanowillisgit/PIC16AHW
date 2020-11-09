#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
from numpy import random

def get_X_tilde(class1data,class2data):
    """
    Takes in class 1 and class 2 points and returns X_tilde matrix
    """
    class1_tilde = np.insert(class1data , 0, 1,axis=1)
    class2_tilde = np.insert(class2data , 0, 1,axis=1)
    X_tilde = np.concatenate((class1_tilde , class2_tilde),axis=0)
    return X_tilde

def get_T(Class1N,Class2N):
    """
    Return T matrix according to number of each class elements
    """
    T = np.array(
        [ np.concatenate( (np.ones(Class1N), np.zeros(Class2N) ) ),
              np.concatenate( (np.zeros(Class2N), np.ones(Class1N) )  )])
    T = np.transpose(T)
    return T


def least_squares_closed_form( class1data,class2data, Class1N, Class2N):
    """
    Computes w weight vector using closed form solution to least squares discriminant
    """
    X_tilde = get_X_tilde(class1data,class2data)
    T = get_T(Class1N,Class2N)
    W_tilde = np.matmul(linalg.pinv(X_tilde), T)
    w_dev = W_tilde[...,0] - W_tilde[...,1]
    return w_dev

def inner_prods(w,X_tilde,Class1N,Class2N):
    """
    Returns array of inner products between w and data vectors
    """
    class1innerprods = np.zeros(Class1n)
    class2innerprods = np.zeros(Class2n)
    for i in range(0,Class1n):
        class1innerprods[i] = np.inner(w_dec , X_tilde[i])

    for i in range(0,Class2n):
        class2innerprods[i] = np.inner(w_dec , X_tilde[i+Class1n])

    return np.concatenate((class1innerprods,class2innerprods))

# We will generate 100 points per class
Class1n = 100
Class2n = 100

# Set mean and covariance for class 1
C1Mean = [1, 3]
C1cov = [[3, 1.9 ],[1.9,1.3]]

# Generate acutal points for class 1
C1points = np.random.multivariate_normal(C1Mean, C1cov, Class1n)

# Set mean and covariance for class 2
C2Mean = [1, -3]
C2cov = [[3, 1.9 ],[1.9,1.3]]

# Generate acutal points for class 2
C2points = np.random.multivariate_normal(C2Mean, C2cov, Class2n)

# Plot the toy data
plt.scatter(C1points[...,0],C1points[...,1], c="r")
plt.scatter(C2points[...,0],C2points[...,1], c="b")
plt.title("Plot of toy data")
plt.show(block=False)
plt.pause(5)
plt.close()

w_dec = least_squares_closed_form(C1points,C2points,Class1n,Class2n)

# Save X_tilde for later
X_tilde = get_X_tilde(C1points,C2points)

# Compute inner products of weight and data
innerprods = inner_prods(w_dec,X_tilde,Class1n,Class2n)

plt.close()
plt.eventplot(innerprods[0:Class1n-1],linewidths=0.2,color="r")
plt.eventplot(innerprods[Class1n:len(innerprods) -1],linewidths=0.2,color="b")
plt.title("Inner product of weight and toy data")
plt.show(block=False)
plt.pause(5)
plt.close()

###########################################################
##  Demo of points where one class has lots of outliers  ##
###########################################################


# We will generate 100 points per class
Class1n = 100
Class2n = 100

# Set mean and covariance for class 1
C1Mean = [1, 2]
C1cov = [[3, 1.5 ],[1.5,1]]

# Generate acutal points for class 1
C1points = np.random.multivariate_normal(C1Mean, C1cov, Class1n)

# Set mean and covariance for class 2
C2Mean = [1, -1]
C2cov = [[3, 1.5 ],[1.5,1]]

# Generate acutal points for class 2
C21points = np.random.multivariate_normal(C2Mean, C2cov, (Class2n // 2) )

# Generate outliers...
C3Mean = [6 , -5]
C3cov = [[0.9,0],[0,0.7]]
C22points = np.random.multivariate_normal(C3Mean, C3cov, (Class2n // 2) )

# Put outliers with usual points together
C2points = np.concatenate((C21points,C22points))

# Plot new points
plt.scatter(C1points[...,0],C1points[...,1], c="r")
plt.scatter(C2points[...,0],C2points[...,1], c="b")
plt.title("Outlier-ed toy data")
plt.show(block=False)
plt.pause(5)
plt.close()

# Compute optimal weight vector
w_dec = least_squares_closed_form(C1points,C2points,Class1n,Class2n)

# Save X_tilde for later
X_tilde = get_X_tilde(C1points,C2points)

# Compute inner products of weight and data
innerprods = inner_prods(w_dec,X_tilde,Class1n,Class2n)

# Plot inner products for outlier data
plt.eventplot(innerprods[0:Class1n-1],linewidths=0.2,color="r")
plt.eventplot(innerprods[Class1n:len(innerprods) -1],linewidths=0.2,color="b")
plt.title("Inner products of outlier-ed data")
plt.show()
