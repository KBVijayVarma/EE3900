# -*- coding: utf-8 -*-
"""EE3900-A-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vtpAXZvxLyliXg9N8DhuDX27MJ5xg4hX
"""

import numpy as np
import matplotlib.pyplot as plt
import math

print("The figure is drawn by taking value of m = infinity\n")

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

A = np.array([1,3])
B = np.array([1,1])
C = np.array([-4,1])


# Generating the lines AB, AC, CB
x_AB = line_gen(A,B)
x_AC = line_gen(A,C)
x_CB = line_gen(C,B)

# Plotting all the lines AB, CD, AC, CB, BD, DA
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')

# Labelling Points
plt.plot(A[0], A[1], 'o')
plt.text(A[0] - (0.5), A[1] + (0.1) , 'A (1,3)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] - (0.3), B[1] - (0.3) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] - (0.2), C[1] + (0.2) , 'C (-4,1)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper left', fontsize = 9)
plt.grid()
plt.axis('equal')
plt.show()

print("\nEquation of line AB is x = 1")
print("Equation of line BC is y = 1")