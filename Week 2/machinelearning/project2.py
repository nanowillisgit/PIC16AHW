import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

df = pd.read_csv("winequality-red.csv",sep=";",header=0)

#################################################### ##           Closed-form solution                 ##
####################################################

# Place data in design matrix
X =  np.array( df.iloc[:, :11] )

# Complete linear basis function model
X = np.insert(X , 0, 1,axis=1)
#print(X)
# Target vector
t = np.array( df['quality'])

# Compute Moore-Penrose pseudoinverse of design matrix
pinv = np.linalg.pinv( X )

# Compute w_star according to closed form solution 
w_star = np.matmul( pinv , t)


print("First 5 entries of w_star:\n[")
for i in range(0,5):
    print (w_star[i],",")
print("   ]")

# Compute and print average error of closed form
normed = np.subtract( np.matmul( X , w_star ) , t )
error = (np.linalg.norm(normed)**2 ) / 1599
print("Optimal error from closed form:" ,error,"\n")


###################################################
##            Algorithmic Implementation         ##
###################################################


# Number of algorithm iterations to run
iters = 100_000

w_k = np.zeros(12,float)
errors = np.zeros(iters,float)

# Initial error is just norm of optimal
errors[0] = np.linalg.norm(w_star )

# Iterate algorithm
for i in range(1,iters+1):

    # Sample data randomly
    n = randint(0,len(X)-1)

    # Compute coefficients of x_n in equation (1)
    eta_term = 1 / ( ( np.linalg.norm( X[n] ))**2 )
    num_coeff = t[n] - np.dot( w_k , X[n])
    coeff = num_coeff * eta_term

    # Update w_k
    w_k = np.add(w_k , (X[n] * coeff) )

    # Load error term
    errors[i] = np.linalg.norm( np.subtract( w_star , w_k))

# Compute and print average error for algorithm run
normed_alg = np.subtract( np.matmul( X , w_k ) , t )
error_alg = ( np.linalg.norm(normed_alg)**2 ) / (len(X))
print("Average error of algorithm:",error_alg)


# Plot distance over iterates
itvl = np.linspace(0,iters,num=len(errors))
plt.plot(itvl,errors)
plt.xlabel('iterations')
plt.ylabel('||w* - w_k||')

plt.show()
