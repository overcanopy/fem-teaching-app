import numpy as np
from fem_core.mesh import generate_mesh
from fem_core.assembly import assemble_global
from fem_core.solver import apply_boundary_conditions

def run_linear_elasticity(E, nu, nx=10, ny=2, lx=1.0, ly=0.2, F=-1000.0):
    D = (E / (1 - nu**2)) * np.array([
        [1, nu, 0],
        [nu, 1, 0],
        [0, 0, (1 - nu) / 2]
    ]) * 0.01  # thickness multiplier

    nodes, elements = generate_mesh(nx, ny, lx, ly)
    K = assemble_global(nodes, elements, D)
    f = np.zeros(len(nodes) * 2)

    right_nodes = np.where(nodes[:, 0] > lx - 1e-6)[0]
    for n in right_nodes:
        f[2*n + 1] = F / len(right_nodes)

    left_nodes = np.where(nodes[:, 0] < 1e-6)[0]
    fixed_dofs = np.ravel([[2*n, 2*n+1] for n in left_nodes])

    u = apply_boundary_conditions(K, f, fixed_dofs)
    max_disp = np.min(u[1::2])

    return {"max_displacement": float(max_disp), "num_nodes": len(nodes), "num_elems": len(elements)}
