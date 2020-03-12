from cvxopt import matrix, solvers

c = matrix([ -1000.0, -1200.0, -12000.0 ])

A = matrix(
    [
        [-1.0, 0.0, 0.0],
        [0.0, -1.0, 0.0],
        [0.0, 0.0, -1.0],
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [2.0, 1.0, 3.0],
        [1.0, 1.0, 1.0],

    ]).trans()

b = matrix([ 0.0, 0.0, 0.0, 40.0, 30.0, 20.0, 100.0, 60.0 ])

sol=solvers.lp(c,A,b)

print(sol['x'])