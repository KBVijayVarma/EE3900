# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1goK_VmktlyvwgJoBiz_SKeQhXeuqyLfy
"""

import numpy as np
import matplotlib.pyplot as plt

# Input Points
A = np.array([-1,0])
B = np.array([0,3])
C = np.array([3,2])
D = np.array([2,-1])

# Printing Input Points
print("A :",A)
print("\nB :",B)
print("\nC :",C)
print("\nD :",D)

# Printing the Dimensional Vectors of AB, BC, CD, DA
print("\nA-B = ",A-B)
print("C-D = ",C-D)
print("B-C = ",B-C)
print("D-A = ",D-A)
print("A-C = ",A-C)
print("B-D = ",B-D)

# Checking Orthogonality of Sides AB and BC
print("\n(A-B).(B-C) = ", np.dot(A-B,B-C))

# Checking Orthogonality of Sides BC and CD
print("\n(B-C).(C-D) = ", np.dot(B-C,C-D))

# Checking Orthogonality of Sides CD and DA
print("\n(C-D).(D-A) = ", np.dot(C-D,D-A))

# Checking Orthogonality of Sides DA and AB
print("\n(D-A).(A-B) = ", np.dot(D-A,A-B))
print("Since all the dot products are zero, all the sides are perpendicular to each other")
print("From above, since all sides of \nQuadrilateral  ABCD  are  perpendicular  to  each  other, ABCD is a Rectangle.")

# Checking Orthogonality of Diagonals AC and BD
print("\n(A-C).(B-D) = ", np.dot(A-C,B-D))

print("\nSince the above dot product is 0, the diagonals AC and BD are perpendicular")

print("Diagonals of Rectangle ABCD are perpendicular, therefore ABCD is a Square")

#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

# Creating the Lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

# Plotting all the Lines
plt.plot(x_AB[0,:],x_AB[1,:],label = '$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label = '$BC$')
plt.plot(x_CD[0,:],x_CD[1,:],label = '$CD$')
plt.plot(x_DA[0,:],x_DA[1,:],label = '$DA$')

# Plotting Points
plt.plot(A[0],A[1],'o')
plt.text(A[0] - 0.8,A[1],'A(-1,0)')
plt.plot(B[0],B[1],'o')
plt.text(B[0],B[1] - 0.3,'B(0,3)')
plt.plot(C[0],C[1],'o')
plt.text(C[0] + 0.1,C[1],'C(3,2)')
plt.plot(D[0],D[1],'o')
plt.text(D[0] + 0.2,D[1],'D(2,-1)')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')


plt.legend(loc='upper left')
plt.grid()
plt.axis('equal')
plt.show()


print("Since the Rectangle ABCD has perpendicular diagonals,\nHence it is a Square.")