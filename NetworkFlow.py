from typing import List

"""
fucking shitshow of an algorithm
"""
class Edge:
    """
    represents a directed edge in network flow
    """
    def __init__(self, u: int, v: int, capacity: int):
        """
        initialize edge in graph
        args:
            u:          starting vertex of edge
            v:          ending vertex of edge
            capacity:   max capacity of edge
        """
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.reverse = None # tbd when reverse edge

def dfs(u:int , t:int , bottleneck: int, visited:List, graph:List[List]):
    """
    dfs to find argumenting path in graph
    args:
        u:  current vertex
        t: target/sink vertex
        bottleneck: min capacity along path
        visited: list of vertices to prevent revisiting
        graph: adjacency list of graph
    returns:
        int: bottleneck flow val for the path
    """
    if u == t:
        return bottleneck
    visited[u] = True
    for edge in graph[u]:
        res = edge.capacity - edge.flow
        if res > 0 and not visited[edge.v]:
            arg = dfs(edge.v, t, min(bottleneck,res), visited, graph)
            if arg > 0:
                edge.flow += arg
                edge.reverse.flow -= arg
                return arg
    return 0

def max_flow(graph: List[List], source: int, target: int):
    """
    calculate max flow from source s to sink t using the Ford Fulkerson algorithm
    Args:
        graph:  Adjacencyt list of graph
        source: source vertex
        target: sink/target vertex
    return:
        int: total max flow from source s to sink t
    """
    n = len(graph)
    flow = 0
    for u in range(n):
        for edge in graph[u]:
            if edge.reverse is None:
                reverseEdge = Edge(edge.v, edge.u, 0)
                edge.reverse = reverseEdge
                graph[edge.v].append(reverseEdge)
    while True:
        visited = [False] * n
        arg = dfs(source, target, float("inf"), visited, graph)
        if arg == 0:
            break
        flow += arg
    return flow


if __name__ == "__main__":
    graph = [[] for _ in range(4)]  # Graph with 4 vertices

    # Add edges to the graph
    graph[0].append(Edge(0, 1, 10))
    graph[1].append(Edge(1, 0, 0))  # Reverse edge for 0 -> 1
    graph[0].append(Edge(0, 2, 5))
    graph[2].append(Edge(2, 0, 0))  # Reverse edge for 0 -> 2
    graph[1].append(Edge(1, 2, 15))
    graph[2].append(Edge(2, 1, 0))  # Reverse edge for 1 -> 2
    graph[1].append(Edge(1, 3, 10))
    graph[3].append(Edge(3, 1, 0))  # Reverse edge for 1 -> 3
    graph[2].append(Edge(2, 3, 10))
    graph[3].append(Edge(3, 2, 0))  # Reverse edge for 2 -> 3

    # Now run Ford-Fulkerson to find the max flow from node 0 (source) to node 3 (sink)
    max_flow_value = max_flow(graph, 0, 3)
    print(f"Maximum Flow: {max_flow_value}")