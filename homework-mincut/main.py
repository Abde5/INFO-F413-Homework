import networkx as nx
import matplotlib.pyplot as plt
import random

def karger(graph):
    """ Implementation of Karger's Algorithm:
        For a given graph with n nodes:

        for i in {1,...,n-2}:
            pick edge e in E(G)
            contract edge e

        Returns:
            int: size of random cut
    """

    graph = nx.MultiGraph(graph)

    for i in range(1,graph.number_of_nodes()-1):

        chosen_edge = random.choice([e for e in graph.edges])
        first_node = chosen_edge[0]
        second_node = chosen_edge[1]

        # generate a minor graph with the contracted edge
        graph = nx.contracted_nodes(graph,first_node,second_node,False)

    return len(graph.edges)


if __name__ == "__main__":
    graph = nx.tutte_graph()
    print(krager(graph))
