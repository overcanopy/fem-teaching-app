import numpy as np

def generate_mesh(nx, ny, lx=1.0, ly=1.0):
    x = np.linspace(0, lx, nx + 1)
    y = np.linspace(0, ly, ny + 1)
    X, Y = np.meshgrid(x, y)
    nodes = np.column_stack([X.flatten(), Y.flatten()])
    elements = []
    for j in range(ny):
        for i in range(nx):
            n1 = j * (nx + 1) + i
            n2 = n1 + 1
            n3 = n1 + nx + 2
            n4 = n1 + nx + 1
            elements.append([n1, n2, n3, n4])
    return np.array(nodes), np.array(elements)
