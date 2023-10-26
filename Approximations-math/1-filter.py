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

            for i in range(m):
                for j in range(n):
                    i_offset = i + k_offset
                    j_offset = j + l_offset

                    if 0 <= i_offset < m and 0 <= j_offset < n:
                        result[i, j] += F[k_index, l_index] * A[i_offset, j_offset]

    return result
