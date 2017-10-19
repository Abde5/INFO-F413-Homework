import networkx as nx
import matplotlib.pyplot as plt
import random

def karger(graph):
    """
        Implementation of Karger's Algorithm:
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
        graph = nx.contracted_nodes(graph,first_node,second_node,False)

    return len(graph.edges)

def generate_connected_K(nb):
    """
        2 connected complete subgraph (nb-connected) joined by nb-2 edges (this
        will be the only minimum cut)
    """

    graph = nx.Graph()
    graph = nx.disjoint_union(graph,nx.complete_graph(nb))
    graph = nx.disjoint_union(graph,nx.complete_graph(nb))

    for i in range(nb-2):
        graph.add_edge(i, nb+i)
    return graph


def generate_KX(X,nb):
    """
        Generates 'nb' K_X subgraphs and puts an edge between those subgraphs.
    """

    NODES = X
    graph = nx.Graph()
    graph = nx.disjoint_union(graph,nx.complete_graph(NODES))
    for i in range(0,nb):
        graph = nx.disjoint_union(graph,nx.complete_graph(NODES))
        graph.add_edge(i*NODES, (i+1)*NODES)
    graph.add_edge(0, nb*NODES)
    return graph

def checkBound(graph):
    """
        Return minimal cut of n^2/n repetitions of karger
    """
    minimal_cut = graph.number_of_edges() +1
    graph_size = graph.number_of_nodes()
    for i in range((graph_size*graph_size)//2):
        cut = karger(graph)
        if cut < minimal_cut:
            minimal_cut = cut

    return minimal_cut

if __name__ == "__main__":
    """
        Graph ideas:
        - Zachary's Karate Club

        # check if 100 repetitions = error of 1/e
    """
    #graph_union = nx.karate_club_graph()
    graph_union = generate_KX(10,3)
    #graph_union = generate_connected_K(10)

    print(len(nx.minimum_edge_cut(graph_union)))
    print(checkBound(graph_union))

    nx.draw(graph_union)
    plt.show()

    results = {}
    mincut = 0
    for i in range(100):
        mincut = checkBound(graph_union)
        if mincut in results:
            results[mincut] += 1
        else:
            results[mincut] = 1
        print(mincut)
    print(results)
