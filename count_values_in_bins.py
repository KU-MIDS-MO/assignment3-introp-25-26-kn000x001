import numpy as np

def count_values_in_bins(data, bin_edges):
    ### Replace with your own code (begin) ###
    data = np.asarray(data)
    edges = np.asarray(bin_edges)

    B = len(edges) - 1
    counts = np.zeros(B, dtype=int)

    for x in data:
        if x < edges[0] or x > edges[-1]:
            continue
        placed = False
        for i in range(B - 1):
            if edges[i] <= x < edges[i + 1]:
                counts[i] += 1
                placed = True
                break
        if not placed:
            if edges[B - 1] <= x <= edges[B]:
                counts[B - 1] += 1

    return counts
    pass
    ### Replace with your own code (end)   ###

