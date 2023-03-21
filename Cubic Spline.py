import numpy as np
import matplotlib.pyplot as plt

def cubicSpline(x,fun):
    n = len(x)-1
    h = 2/n
    f = fun(x)

    A = np.zeros((n-1,n-1))
    rhs = np.zeros(n-1)
    ct = (6/(h**2))

    for i in np.arange(n-1):
        # (6/h^2) * (f[i] - 2f[i+1] + f[i+2])
        rhs[i] = ct*(f[i]-2*f[i+1]+f[i+2])
        # Matrix A has 3 diagonals with values [1,4,1]
        if i==0:
        # special case for first row [4 1 0 ... 0]
            A[0,0:2]=[4,1]
        elif i==n-2:
        # special case for last row [0 0 ... 1 4]
            A[n-2,n-3:n-1]=[1,4]
        else:
        # general case [0 0 ... 1 4 1 ... 0 0]
            A[i,i-1:i+2]=[1,4,1]
    

    a = np.zeros(n+1)
    
    tmp = np.linalg.solve(A,rhs)
    a[1:n] = tmp
    
    

    for i in range(len(x)-1):

        g = lambda z: (((x[i+1]-z)**3 * a[i]) / (6*h)) + (((z-x[i])**3 * a[i+1]) / (6*h)) + ((x[i+1]-1)*((fun(x[i])/h)-(a[i]*h/6))) + ((z-x[i])*((fun(x[i+1]/h))-(a[i+1]*h/6)))
        if i==0:
            plt.plot(x,g(x),color="orange",label="Splines")
        else:
            plt.plot(x,g(x),color="orange")

f = lambda x: 1 / (1+(10*x)**2)

xeval = np.linspace(-1,1,1000)
xint = np.linspace(-1,1,11)

plt.plot(xeval,f(xeval),color="red",label="f(x)")
cubicSpline(xint,f)
plt.xlim(-1,1)
plt.ylim(0,1)
plt.legend()
plt.show()