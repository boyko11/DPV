from cvxopt import matrix, solvers

c = matrix([ -1.6, -1.4 ])

A = matrix(
    [
        [-1.0, 0.0],
        [0.0, -1.0],
        [1.0, 0.0],
        [1.0, 2.0],
        [1.5, 1.0]

    ]).trans()

b = matrix([ 0.0, 0.0, 110000.0, 240000.0, 180000.0 ])

sol=solvers.lp(c,A,b)

print(sol['x'])