import numpy as np

def apply_boundary_conditions(K, f, fixed_dofs, values=None):
    if values is None:
        values = np.zeros_like(fixed_dofs, dtype=float)
    free_dofs = np.setdiff1d(np.arange(len(f)), fixed_dofs)
    for dof, val in zip(fixed_dofs, values):
        f -= K[:, dof] * val
    K_ff = K[np.ix_(free_dofs, free_dofs)]
    f_f = f[free_dofs]
    u = np.zeros(len(f))
    u[free_dofs] = np.linalg.solve(K_ff, f_f)
    u[fixed_dofs] = values
    return u
