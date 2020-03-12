from cvxopt import matrix, solvers

c = matrix([ -1.0, -1.5 ])

A = matrix(
    [
        [-1.0, 0.0],
        [0.0, -1.0],
        [-1.0, 2.0],
        [1.0, 1.0]

    ]).trans()

b = matrix([ 0.0, 0.0, 0.0, 3000.0 ])

sol=solvers.lp(c,A,b)

print(sol['x'])