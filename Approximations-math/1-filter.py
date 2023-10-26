#!/usr/bin/env python3
import numpy as np

def apply_filter(F, i_c, j_c, A):
    k, l = F.shape  # Dimensions of the filter F
    m, n = A.shape  # Dimensions of the input array A

    result = np.zeros_like(A)  # Initialize the result with zeros

    for k_index in range(k):
        for l_index in range(l):
            k_offset = k_index - i_c  # Offset from the center i_c
            l_offset = l_index - j_c  # Offset from the center j_c

            # Loop over the dimensions of A is avoided as per the constraint
            # Instead, compute the valid indices within A directly
            i_indices = np.arange(m) + k_offset
            j_indices = np.arange(n) + l_offset

            # Find the indices that are within the bounds of A
            valid_i_indices = (i_indices >= 0) & (i_indices < m)
            valid_j_indices = (j_indices >= 0) & (j_indices < n)

            # Compute the valid indices in both dimensions
            valid_i_indices = i_indices[valid_i_indices]
            valid_j_indices = j_indices[valid_j_indices]

            # Use the valid indices to update the result
            result[valid_i_indices, valid_j_indices] += F[k_index, l_index] * A[valid_i_indices - k_offset, valid_j_indices - l_offset]

    return result
