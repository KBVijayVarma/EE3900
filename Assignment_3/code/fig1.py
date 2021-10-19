# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FA3G-Eu7YLgsiHGygxS_qcexQm3YYBA9
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
x_circ = circ_gen(0,3)

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
A = np.array([1,2*(math.sqrt(2))])
B = np.array([-1,-2*(math.sqrt(2))])
C = np.array([-3*(1/(math.sqrt(2))),3*(1/(math.sqrt(2)))])
D = np.array([3*(1/(math.sqrt(2))),-3*(1/(math.sqrt(2)))])

# AB, CD are Diagonals which are not perpendicular
# AC, CB, BD, DA are sides of the Quadrilateral ACBD
# Generating the lines AB, CD, AC, CB, BD, DA
x_AB = line_gen(A,B)
x_CD = line_gen(C,D)
x_AC = line_gen(A,C)
x_CB = line_gen(C,B)
x_BD = line_gen(B,D)
x_DA = line_gen(D,A)

# Plotting all the lines AB, CD, AC, CB, BD, DA
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')
plt.plot(x_BD[0,:],x_BD[1,:],label='$BD$')
plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')

# Labelling Points
plt.plot(O[0], O[1], 'o')
plt.text(O[0] - (0.5), O[1] - (0.1) , 'O')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] + (0.1), A[1] + (0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] - (0.3), B[1] - (0.3) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] - (0.3), C[1] + (0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] + (0.1), D[1] - (0.3) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right', fontsize = 9)
plt.grid()
plt.axis('equal')
plt.show()

# Since the Diagonals(AB and CD) of the Quadrilateral ACBD are of equal length and bisecting each other, hence it is a Rectangle which can be verified from the figure
# Hence, the Quadrilateral ACBD is a Rectangle when the Diameters(AB and CD) are not perpendicular.