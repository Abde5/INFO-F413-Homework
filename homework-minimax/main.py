import pulp
import numpy as np

def row_player_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix for the row player. (main player)

        - returns (mixedStrategies,expectedPayroll)
    """
    #we use the transposed matrix, for neatness in the code
    payrollMatrix = [list(i) for i in zip(*payrollMatrix)]

    Z = pulp.LpVariable('Objective')
    problem = pulp.LpProblem("Nash Equilibrium (p)", pulp.LpMaximize)
    problem.setObjective(Z)

    # vector of mixed strategies
    p = tuple([[pulp.LpVariable("p"+str(i+1),lowBound=0),1] for i in range(len(payrollMatrix))])

    # sum of mixed strategies == 1
    problem += pulp.LpAffineExpression(p) == 1

    #we suppose the matrix is transposed
    for line in payrollMatrix:
        for j in range(len(line)):
            p[j][1] = line[j]
        problem += Z <= pulp.LpAffineExpression(p)

    print(problem)
    sol = pulp.solvers.GLPK()
    sol.actualSolve(problem)

    print(str(Z)+" = "+str(Z.varValue))

def column_player_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix for the column player. (opponent)

        - returns (mixedStrategies,expectedPayroll)
    """
    Z = pulp.LpVariable('Objective')
    problem = pulp.LpProblem("Nash Equilibrium (p)", pulp.LpMaximize)
    problem.setObjective(Z)

    # vector p (column player)
    p = ()


def nash_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix.

        - returns (p,q,expectedPayroll)
    """

    row_player_equilibrium(payrollMatrix)



if __name__ == "__main__":
    nash_equilibrium([[3,-1],[-2,1]])
