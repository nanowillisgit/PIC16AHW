import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read data
d = pd.read_csv("fitting_N20.csv", index_col=0, header=None, names = [ "Num" , "cx" , "cy"] )

x = d['cx']
t = d['cy']
#print(d)

### List of polynomial coefficient arrays. Degree 1 thru 20
#polys = [ np.polyfit( d['cx'] , d['cy'] , i) for i in range(0,21) ]

### Compute errors of each degree
#errors = [ 0.5*sum( np.polyval(polys[j],d['cx']) - d['cy'] )**2 for j in range(0,21) ]

interval = np.linspace(min(x),max(x),num=5000)

deg = 5
N = len(x)

def wij_coeff(i,j):
    """ Returns coefficient of w_j in ith row of system
    input i: row number
    input j: jth index
    return: coefficient of w_j on ith row
    """
    summands = [ (x[n]**i)*(x[n]**j) for n in range(1,N+1) ]
    return sum(summands)

### Take in 
def const_val(i):
    """ Returns constant term in ith row (see equation 4)
    input i: row number
    return: constant term of ith row
    """
    summands = [ (x[n]**i)*(t[n]) for n in range(1,N+1)]
    return sum(summands)

def const_vect():
    """ Returns list of constant terms
    return: list of constant terms (terms with no w_j)
    """
    return [const_val(i) for i in range(deg+1) ]

sys = [0] * (deg+1)
for i in range(deg+1):
    cos = [ wij_coeff(i,j) for j in range(deg+1)]
    sys[i] = cos 

### Arrange the constants vector after setting derivatives equal to 0
constants = const_vect()

### Convert lists to arrays
system = np.asarray(sys)
consts = np.asarray(constants)


### Solve system of equations for unique optimal solution
coeffs = np.linalg.solve(system, consts)

### Plot results
plt.plot(x, t , '*', markersize=7)
#plt.plot(interval , np.polyval(np.flip(coeffs),interval) , '-',  color="red", label = "Deg. 4")
plt.plot(interval , np.polyval(polys[6],interval) , '-',  color="red", label = "Deg. 6")
plt.plot(interval , np.polyval(polys[7],interval) , '-',  color="purple", label = "Deg. 7")
plt.legend()
plt.show()
