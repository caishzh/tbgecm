"""
This module contains the numerical lattice relaxation algorithm
for the twisted bilayer graphene model with strain.
"""

import numpy as np
from .utils import chop, rotational_matrix, pauli_matrix

class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Input:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Relaxation:
    def __init__(self, config, input):
        self.config = config
        self.input = input

    def relax(self):
        pass

class Result:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)