import numpy as np
from fem_core.shape_functions import shape_Q4

def element_stiffness(coords, D):
    gp = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])
    Ke = np.zeros((8, 8))
    for xi in gp:
        for eta in gp:
            N, dN = shape_Q4(xi, eta)
            J = dN.T @ coords
            detJ = np.linalg.det(J)
            dN_dx = dN @ np.linalg.inv(J)
            B = np.zeros((3, 8))
            B[0, 0::2] = dN_dx[:, 0]
            B[1, 1::2] = dN_dx[:, 1]
            B[2, 0::2] = dN_dx[:, 1]
            B[2, 1::2] = dN_dx[:, 0]
            Ke += B.T @ D @ B * detJ
    return Ke

def assemble_global(nodes, elements, D):
    ndof = len(nodes) * 2
    K = np.zeros((ndof, ndof))
    for el in elements:
        coords = nodes[el]
        Ke = element_stiffness(coords, D)
        dof = np.ravel([[2*i, 2*i+1] for i in el])
        for i in range(8):
            for j in range(8):
                K[dof[i], dof[j]] += Ke[i, j]
    return K
