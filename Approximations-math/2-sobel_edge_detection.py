#!/usr/bin/env python3
import numpy as np
apply_filter = __import__('1-filter').apply_filter


def rescale(np_arr):
    M = np.max(np_arr)
    m = np.min(np_arr)
    return (np_arr - m) / (M - m)

def sobel_edge_detection(A, threshold):
    # Define the Sobel operators for horizontal and vertical gradients
    s_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    s_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Use the filter function with the Sobel operators for convolution
    partial_x = apply_filter(s_x, 1, 1, A)
    partial_y = apply_filter(s_y, 1, 1, A)

    # Compute the intensity and angle of the gradient
    intensity = np.sqrt(partial_x**2 + partial_y**2)
    angle = np.arctan2(partial_y, partial_x)

    # Rescale the intensity of the gradient
    intensity = rescale(intensity)
    print(intensity)

    # Initialize the output B
    m, n = A.shape[0], A.shape[1]
    B = np.zeros((m, n, 3))

    # Apply the threshold and set B values accordingly
    mask = intensity >= threshold
    B[mask, 0] = (1 + np.cos(angle[mask])) / 2
    B[mask, 1] = 0.7
    B[mask, 2] = (1 + np.sin(angle[mask])) / 2

    return B
