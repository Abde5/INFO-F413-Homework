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

def generate_K100(nb):
    """
        Generates 'nb' K_100 subgraphs and puts an edge between those subgraphs.
    """

    graph = nx.Graph()
    graph = nx.disjoint_union(graph,nx.complete_graph(100))
    for i in range(0,nb):
        graph = nx.disjoint_union(graph,nx.complete_graph(100))
        graph.add_edge(i*100, (i+1)*100)
    graph.add_edge(0, nb*100)
    return graph

if __name__ == "__main__":
    """
        Graph ideas:
        - Hypercube graph
        - Zachary's Karate Club
        - Davis Southern Women
    """
    graph = nx.karate_club_graph()

    graph_union = generate_K100(4)

    nx.draw(graph_union)
    plt.show()


    # print actual mincut and karger's found cut
    print(len(nx.minimum_edge_cut(graph_union)))
    print(karger(graph_union))
