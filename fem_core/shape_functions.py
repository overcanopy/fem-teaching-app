import numpy as np

def shape_Q4(xi, eta):
    N = 0.25 * np.array([
        (1 - xi)*(1 - eta),
        (1 + xi)*(1 - eta),
        (1 + xi)*(1 + eta),
        (1 - xi)*(1 + eta)
    ])
    dN_dxi = 0.25 * np.array([
        [-(1 - eta), -(1 - xi)],
        [ (1 - eta), -(1 + xi)],
        [ (1 + eta),  (1 + xi)],
        [-(1 + eta),  (1 - xi)]
    ])
    return N, dN_dxi
