"""
This module provide some utility functions to use in the algorithm.
"""

import numpy as np

def chop(arr, tol=1e-10):
    """
    Element-wise chop function that sets small values to zero based on a threshold.

    Parameters:
    - arr (ndarray): The input array (can be real or complex)
    - tol (float): The tolerance level, below which values are set to zero (default 1e-10)

    Returns:
    - ndarray: The chopped array with small values replaced by zero.
    """

    # If arr is complex, handle real and imaginary parts separately
    result = np.copy(arr)
    if np.iscomplexobj(arr):
        result.real = np.where(np.abs(arr.real) < tol, 0, arr.real)
        result.imag = np.where(np.abs(arr.imag) < tol, 0, arr.imag)

    # If arr is real, just compare the absolute value to tol
    else:
        result = np.where(np.abs(arr) < tol, 0, arr)

    return result


def rotational_matrix(angle: float) -> np.ndarray:
    """
    Create a 2D rotational matrix for a given angle.

    Parameters:
    - angle (float): The angle of rotation in radians.

    Returns:
    - ndarray: The 2x2 rotational matrix.
    """

    return np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)]])


def pauli_matrix(idx: int) -> np.ndarray:
    """
    Create a 2x2 Pauli matrix for a given index.

    Parameters:
    - idx (int): The index of the Pauli matrix (0, 1, 2, or 3).

    Returns:
    - ndarray: The 2x2 Pauli matrix.
    """

    if idx == 0:
        return np.array([[1, 0], [0, 1]])
    elif idx == 1:
        return np.array([[0, 1], [1, 0]])
    elif idx == 2:
        return np.array([[0, -1j], [1j, 0]])
    elif idx == 3:
        return np.array([[1, 0], [0, -1]])
    else:
        raise ValueError("Invalid Pauli matrix index")


def test():
    pass