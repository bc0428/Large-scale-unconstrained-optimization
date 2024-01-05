import numpy as np
from matplotlib import pyplot as plt
import time

# objective function
n = 5
alpha = np.array([80] * n)
x0 = np.array([20] * n)
# alpha[0:n//2] = 1

# convergence
convergence_tolerance = 1e-1

# backtracking parameters
backtracking_alpha = 0.4
backtracking_beta = 0.5
backtracking_t0 = 1

