from numpy import *
import matplotlib.pyplot as plt

theta = linspace(0,2*pi,1000)
r = 1+0.5*sin(8*theta)
x = r*cos(theta)
y = r*sin(theta)
plt.figure()
x1 = 0.5*cos(theta)
y1 = 0.5*sin(theta)
plt.plot(x,y,x1,y1)
plt.show()
