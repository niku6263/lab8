import numpy as np
import matplotlib.pyplot as plt

def createLine(x,f):
    for i in range(len(x)-1):
        slope = (f(x[i+1]) - f(x[i])) / (x[i+1] - x[i])
        g = lambda z: slope*(z-x[i]) + f(x[i])
        if i==0:
            plt.plot(x,f(x),color="orange",label="Splines")
        else:
            plt.plot(x,f(x),color="orange")

f = lambda x: 1 / (1+(10*x)**2)

xeval = np.linspace(-1,1,1000)
xint = np.linspace(-1,1,11)

plt.plot(xeval,f(xeval),color="red",label="f(x)")
createLine(xint,f)
plt.legend()
plt.show()