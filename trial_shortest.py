from shortestpath import approximate_steiner
import networkx as nx
import time
import pandas as pd

def get_complete_graph():
    graph = nx.complete_graph(10)
    for i in range(10):
        graph.nodes[i]['weight'] = i
    graph.add_edge(5, 11)
    graph.add_edge(2, 10)
    graph.nodes[10]['weight'] = 10
    graph.nodes[11]['weight'] = 11
    # graph.nodes[0]['weight'] = -1
    # graph.nodes[1]['weight'] = -1
    return graph
def get_cycle():
    graph = nx.Graph()
    edge_list= [(0,1), (1,2), (2,3), (3,4), (4,0), (0,3), (0,2), (0,4)]
    graph.add_edges_from(edge_list)
    graph.nodes[0]['weight'] = 5
    graph.nodes[1]['weight'] = 10
    graph.nodes[2]['weight'] = 4
    graph.nodes[3]['weight'] = 10
    graph.nodes[4]['weight'] = 5
    return graph

def get_tree():
    graph = nx.Graph()
    edge_list = [(0,1), (0,2), (0,3), (0, 4), (1,5), (2,6), (3,7), (4,8), (4,9)]
    graph.add_edges_from(edge_list)
    for i in range(10):
        graph.nodes[i]['weight'] = 1
    return graph

def get_karate_club_graph():
    graph = nx.karate_club_graph()
    for i in range(len(list(graph.nodes))):
        graph.nodes[i]['weight'] = i
    graph.nodes[0]['weight'] = 1
    return graph

terminals_list = [10, 11]
graph = get_complete_graph()
start = time.time()
steiner_tree, steiner_cost = approximate_steiner(graph, terminals_list)
end = time.time()
print(f'Steiner_tree: {steiner_tree.nodes}, Steiner_cost: {steiner_cost}\nTime taken:{end-start}s')
