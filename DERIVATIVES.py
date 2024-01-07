import numpy as np
from CONSTANTS import *

def f(x, j=None) -> float:
    """
    objective function at x
    :param x:
    :return:
    """
    try:
        len(x)
        exp = x / alpha
        return sum(np.exp(exp) + np.exp(-exp))

    except:
        exp = x / alpha[j]
        return np.exp(exp) + np.exp(-exp)

def gradient(x, j=None) -> np.ndarray:
    """
    gradient of objective function at x
    :param x:
    :return:
    """
    try:
        len(x)
        a = alpha
        exp = x / a

    except:
        a = alpha[j]
        exp = x / a

    return (np.exp(exp) - np.exp(-exp))/a

def hessian(x, j=None)-> np.ndarray:
    """
    hessian of objective function at x
    :param x:
    :param j:
    :return:
    """
    try:
        len(x)
        exp = x / alpha
        return np.diag((np.exp(exp) + np.exp(-exp)) / alpha ** 2)
    except:
        a = alpha[j]
        exp = x / a

        return (np.exp(exp) + np.exp(-exp)) / a ** 2


