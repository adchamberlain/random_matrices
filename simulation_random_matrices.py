# Plot real, imaginary parts of eigenvalues for random 10x10 matrices of -1,1 values. 

import numpy as np
from matplotlib import pyplot as plt

dim = 10
S = 2000

for i in range(S):
    M = (np.random.rand(dim, dim) > 0.5).astype(float)*2 - 1
    eigenvalues,i = np.linalg.eig(M)    
    plt.scatter(np.real(eigenvalues),
                np.imag(eigenvalues),
                color='blue', marker="+")