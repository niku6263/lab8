import numpy as np


xeval = np.linspace(0,10,1000)
xint = np.linspace(0,10,11)

int1 = np.where((xeval<xint[1]) & (xeval>xint[0]))
int2 = np.where((xeval<xint[2]) & (xeval>xint[1]))
int3 = np.where((xeval<xint[3]) & (xeval>xint[2]))
int4 = np.where((xeval<xint[4]) & (xeval>xint[3]))
int5 = np.where((xeval<xint[5]) & (xeval>xint[4]))
int6 = np.where((xeval<xint[6]) & (xeval>xint[5]))
int7 = np.where((xeval<xint[7]) & (xeval>xint[6]))
int8 = np.where((xeval<xint[8]) & (xeval>xint[7]))
int9 = np.where((xeval<xint[9]) & (xeval>xint[8]))
int10 = np.where((xeval<xint[10]) & (xeval>xint[9]))

def createLine(x,f):
    slope = (f(x[1]) - f(x[0])) / (x[1] - x[0])

    g = lambda z: slope*(z-x[0]) + f(x[0])
    return g

f = lambda x: x**2
x = [0,2]

g = createLine(x,f)

print(g(1))
