"""
This module contains the numerical lattice relaxation algorithm
for the twisted bilayer graphene model with strain.
"""

import numpy as np
from .utils import chop, rotational_matrix, pauli_matrix

class Config:
    def __init__(self, a=0.246):
        self.a = a
        self.a_vec_set = np.array([[-1/2, np.sqrt(3)/2], [-1, 0]])

class Input:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Relaxation:
    def __init__(self, config):
        self.config = config

    def relax(self):
        pass

class Result:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)