from scipy.integrate import quad
import scipy.stats as stats
import pandas as pd
import numpy as np


def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0) )

x=float(input("enter value"))
z=np.round(x,2)
value=quad(normalProbabilityDensity, np.NINF, z)
print(np.round(value[0],5))
