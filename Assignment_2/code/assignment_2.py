# -*- coding: utf-8 -*-
"""Assignment_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/118I-cmLyez-5c4AiIb5oAG6BZLpJDO0x
"""

import numpy as np

# Given Matrix
A = np.array([[3,5],[1,-1]])

# Printing Given Matrix
print("A :",A)

# Creating Symmetric Matrix
B = np.multiply(np.add(A,A.T),1/2)

# Creating Skew Symmetric Matrix
C = np.multiply(np.add(A,-A.T),1/2)

# Printing the Symmetric and Skew Symmetric Matrix and their Transpose
print("\nB :",B)
print("\nB^T :",B.T)
# B^T = B

print("\nC :",C)
print("\nC^T :",C.T)
# C^T = -C^T

# Verifying Sum of B and C gives A
print("\nB + C = ",np.add(B,C))
# B + C = A