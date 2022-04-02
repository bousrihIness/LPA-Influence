"""Tools to calculate edge scores."""

import networkx as nx
from tqdm import tqdm


def normalized_overlap(g, node_1, node_2):
    """
    Calculating the normalized neighbourhood overlap.
    :param g: NetworkX graph.
    :param node_1: First end node of edge.
    :param node_2: Second end node of edge.
    """
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    unio = len(set(nx.neighbors(g, node_1)).union(set(nx.neighbors(g, node_2))))
    return float(inter) / float(unio)


def overlap(g, node_1, node_2):
    """
    Calculating the neighbourhood overlap.
    :param g: NetworkX graph.
    :param node_1: First end node of edge.
    :param node_2: Second end node of edge.
    """
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    return float(inter)


def unit(g, node_1, node_2):
    """
    Creating unit weights for edge.
    :param g: NetworkX graph.
    :param node_1: First end node of edge.
    :param node_2: Second end node of edge.
    """
    return 1


def min_norm(g, node_1, node_2):
    """
    Calculating the min normalized neighbourhood overlap.
    :param g: NetworkX graph.
    :param node_1: First end node of edge.
    :param node_2: Second end node of edge.
    """
    inter = len(set(nx.neighbors(g, node_1)).intersection(set(nx.neighbors(g, node_2))))
    min_norm = min(len(set(nx.neighbors(g, node_1))), len(set(nx.neighbors(g, node_2))))
    return float(inter) / float(min_norm)


def overlap_generator(metric, graph):
    """
    Calculating the overlap for each edge.
    :param metric: Weight metric.
    :param graph: NetworkX object.
    :return : Edge weight hash table.
    """
    edges = [(edge[0], edge[1]) for edge in nx.edges(graph)]
    edges = edges + [(edge[1], edge[0]) for edge in nx.edges(graph)]
    return {edge: metric(graph, edge[0], edge[1]) for edge in tqdm(edges)}


def s_shell_init(g, node):
    s = 0
    neighbors = set(nx.neighbors(g, node))
    for edge in nx.edges(g):
        if (edge[0] == node and edge[1] in neighbors) or (edge[0] in neighbors and edge[1] == node):
            r = nx.degree(g, edge[0]) + nx.degree(g, edge[1])
            s = s + r
    return s


def calculate_shell(originalGraph , node, nodeDelete, dic_valuf_shell):
    res = 0
    neighbors = set(nx.neighbors(originalGraph, node))
    for noeud in nodeDelete:
        if int(noeud) in neighbors:
            for edge in nx.edges(originalGraph):
                if (edge[0] == node and edge[1] == int(noeud)) or (edge[0] == int(noeud) and edge[1] == node):
                    res = dic_valuf_shell[int(node)] - (
                                (nx.degree(originalGraph, edge[0]) + nx.degree(originalGraph, edge[1])) * 0.5)
                    dic_valuf_shell[int(node)] = res
        else:
            res = dic_valuf_shell[int(node)]
    return res
