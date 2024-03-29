import pulp
import numpy as np
from GameTree import GameTree

def row_player_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix for the row player. (main player)

        - returns (mixedStrategies,optimalSolution)
    """
    #we use the transposed matrix, for neatness in the code
    payrollMatrix = [list(i) for i in zip(*payrollMatrix)]

    Z = pulp.LpVariable('Objective')
    problem = pulp.LpProblem("Nash Equilibrium (p)", pulp.LpMaximize)
    problem.setObjective(Z)

    # vector of mixed strategies
    p = tuple([[pulp.LpVariable("p"+str(i+1),lowBound=0),1] for i in range(len(payrollMatrix[0]))])

    # sum of mixed strategies == 1
    problem += pulp.LpAffineExpression(p) == 1

    #we suppose the matrix is transposed
    for line in payrollMatrix:
        for j in range(len(line)):
            p[j][1] = line[j]
        problem += Z <= pulp.LpAffineExpression(p)

    #print(problem)
    sol = pulp.solvers.GLPK()
    sol.actualSolve(problem)

    return ([i[0].varValue for i in p],Z.varValue)

def column_player_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix for the column player. (opponent)

        - returns (mixedStrategies,optimalSolution)
    """
    Z = pulp.LpVariable('Objective')
    problem = pulp.LpProblem("Nash Equilibrium (q)", pulp.LpMinimize)
    problem.setObjective(Z)

    # vector of mixed strategies
    q = tuple([[pulp.LpVariable("q"+str(i+1),lowBound=0),1] for i in range(len(payrollMatrix[0]))])

    # sum of mixed strategies == 1
    problem += pulp.LpAffineExpression(q) == 1

    for line in payrollMatrix:
        for j in range(len(line)):
            q[j][1] = line[j]
        problem += Z >= pulp.LpAffineExpression(q)

    #print(problem)
    sol = pulp.solvers.GLPK()
    sol.actualSolve(problem)

    return ([i[0].varValue for i in q],Z.varValue)


def nash_equilibrium(payrollMatrix):
    """
        Computes the nash equilibrium of a game based
        in its payroll matrix.

        - returns (p,q,expectedPayoff)
    """

    p_strats,p_sol = row_player_equilibrium(payrollMatrix)
    q_strats,q_sol = column_player_equilibrium(payrollMatrix)

    assert p_sol==q_sol

    return (p_strats,q_strats,p_sol)

if __name__ == "__main__":

    x = GameTree(height=3,_type=True)
    payoff = x.generate_payoff_matrix()
    equilibrium = nash_equilibrium(payoff)

    print("Strategies p:", equilibrium[0])
    print("Strategies q:", equilibrium[1])
    print("Score:", equilibrium[2])

    vector_p = [i for i in zip(x.get_algorithms(),equilibrium[0]) if i[1] > 0]
    print()
    print("ALGORITHM STRATEGIES")
    print()
    for i in vector_p:
        print(i)

    vector_q = [i for i in zip(x.get_inputs(),equilibrium[1]) if i[1] > 0]
    print()
    print("INPUT STRATEGIES")
    print()
    for i in vector_q:
        print(i)
