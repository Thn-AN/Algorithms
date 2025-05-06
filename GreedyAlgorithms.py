from typing import List
from collections import deque

def topological_sort_kahn(adj_list):
    """
    Perform a topological sort on a DAG using Kahn's algorithm (BFS approach).
    Returns a list of vertices in topological order.
    """
    n = len(adj_list)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in adj_list[u]:
            in_degree[v] += 1

    ready = deque([u for u in range(n) if in_degree[u] == 0])
    order = []

    while ready:
        u = ready.popleft()
        order.append(u)

        for v, _ in adj_list[u]:
            in_degree[v] -= 1

            if in_degree[v] == 0:
                ready.append(v)
    return order

def topologicalSort_DFS(graph:List[List]):
    """
    Perform a topological sort on the DAG using DFS.
    Returns a list of vertices in reverse topological order.
    """
    n = len(graph)
    visited = [False] * n 
    order = []

    def dfs(u):
        visited[u] = True 
        for v, _ in graph[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return order[::-1]