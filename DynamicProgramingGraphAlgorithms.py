from typing import List
from GreedyAlgorithms import topologicalSort_DFS
"""
    Graph algorithm problems using DP
"""

def bellmanFord(graph:List[List], source):
    """
    find shortest paths from a source, even with negative weights
    Args:
        adjacency list

    """
    n = len(graph)
    dist = [float("int")] * n
    dist[source] = 0
    # relax edges |v| - 1 times
    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # check negative weight cycles
    for u in range(n):
        for v, weight in graph[u]:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                raise ValueError("graph contains negative weight cycle")

    return dist

def floydWarshall(graph:list[List]):
    """
    Floyd Warshall algorithm is an algorithm for finding shortest paths in a directed weighted graph
    Args:
        adjacency list

    """
    n = len(graph)
    dist = [[float("inf")] * n for _ in range(n)]

    for u in range(n):
        dist[u][u] = 0
        for v, weight in graph:
            dist[u][v] = weight

    
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if dist[u][k] + dist[k][v] < dist[u][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]
    return dist

def transitiveClosure(graph:List[list]):
    """
    Process that adds edges to represent all paths between nodes (or elements)
    Args:
        Adjacency list
    Returns:
        2d List connected where connected[u][v] is True if there's a path from u to v
    """
    n = len(graph)
    connected = [[False] * n for _ in range(n)]

    # Each vertex is reachable from itself
    for v in range(n):
        connected[v][v] = True

    # Set direct connections from adjacency list
    for u in range(n):
        for v in graph[u]:
            connected[u][v] = True

    # Floyd-Warshall-style update for transitive closure
    for k in range(n):
        for u in range(n):
            for v in range(n):
                if connected[u][k] and connected[k][v]:
                    connected[u][v] = True

    return connected

def criticalPath(graph:List[List]):
    """
    longest path in a DAG using bottom-up dynamic programming.
    Args:
        Adjacecny list
    Returns:
        longesst Path for all verticies
    """

    n = len(graph)
    longest = [0] * n
    order = topologicalSort_DFS(graph)

    for u in order:
        for v, weight in graph:
            longest[u] = max(longest[u], weight + longest[v])

    return longest


