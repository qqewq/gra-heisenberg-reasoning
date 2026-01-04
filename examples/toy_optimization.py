
import numpy as np

def f(x, y):
    return (x**2 + y**2 - 1)**2

def g(x, y, alpha):
    return alpha * x**2

def total_loss(x, y, alpha=0.0):
    return f(x, y) + g(x, y, alpha)
