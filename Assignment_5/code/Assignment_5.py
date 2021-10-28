# -*- coding: utf-8 -*-
"""EE3900-A-5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YHcGBycBAFbnK4qx8rh6IKpL8OkGrXa2
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

# Generating a Circle of radius 3
x_circ = circ_gen(0,2)

# Plotting the Circle
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circle$')


# Generating the line points
def line_gen(X,Y):
  len =10
  x = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = X + lam_1[i]*(Y-X)
    x[:,i]= temp1.T
  return x

# Generating points on the circle
O = np.array([0,0])
A = np.array([0,2])
B = np.array([-2,0])
C = np.array([0,-2])
D = np.array([2,0])



# Generating the lines AB, X axis, Y axis
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)
x_BD = line_gen(B,D)

# Plotting all the lines AB, X axis, Y axis
plt.plot(x_AB[0,:],x_AB[1,:],label='$Line$')
plt.plot(x_AC[0,:],x_AC[1,:])
plt.plot(x_BD[0,:],x_BD[1,:])

# Labelling Points
plt.plot(O[0], O[1], 'o')
plt.text(O[0] - (0.3), O[1] - (0.2) , 'O')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] + (0.2), A[1] + (0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] - (0.2), B[1] - (0.2) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right', fontsize = 9)
plt.grid()
plt.axis('equal')
plt.show()