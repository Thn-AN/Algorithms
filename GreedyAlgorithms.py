from typing import List, Tuple
from collections import deque
import heapq
class UnionFind:

    def __init__(self, n: int):
        """
        initializes parent and rank

        args:
            n:  number of nodes in graph

        """
        self.parent = list(range(n)) # stores parent of node
        self.rank = [0] * n  # keeps the trees short when p

    def find(self, u: int):
        """
        Finds the root of the set the node belongs to
        uses path compression to flatten tree
        
        args:
            u: node
        returns:
            parent of node
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        """
        Connects  the set of containing u and v
        uses union by rank to attach the smaller tree under the root of larger tree
        
        args:
            u: start node
            v: end node
        return:
            True if union was done
            False if u and v were already same set
        """
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            self.parent[root_v] = root_u
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1
        return True

def kruskal(edges:List[Tuple[int, int, int]]):
    """
    edges: list of tuples (u,v, weight)
    """
    nodes = set()
    for u, v, _ in edges:
        nodes.add(u)
        nodes.add(v)
    n = max(nodes) + 1

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Kruskal's algorithm
    uFind = UnionFind(n)
    mst = []
    for u, v, weight in edges:
        if uFind.union(u, v):
            mst.append((u, v, weight))
    return mst

def dijkstra(graph:List[list], source):
    n = len(graph)
    pred = [-1] * n
    dist = [float("inf")]*n
    visited = [False]*n
    
    
    dist[source] = 0
    q = [(0, source)]
    while q:
        dist, u = heapq.heappop(q)
        visited[u] = True
        for v, weight in graph[u]:
            if not visited[v] and dist[u] + weight < dist[v] and not visited[v]:
                dist[v] = dist[u] + weight
                pred[v] = u
                heapq. heappush(q, (dist[v], v))
    return dist, pred

def prim(graph: List[List], r: int):
    n = len(graph)
    dist = [float("inf")] * n
    parent = [-1] * n
    mst = [False] * n
    dist[r] = 0
    q = [(0, r)]  # (weight, vertex)

    while q:
        d_u, u = heapq.heappop(q)
        if mst[u]:
            continue
        mst[u] = True
        for v, weight in graph[u]:
            if not mst[v] and weight < dist[v]:
                dist[v] = weight
                parent[v] = u
                heapq.heappush(q, (dist[v], v))

    mst_edges = []
    for v in range(n):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, dist[v]))

    return mst_edges

if __name__ == "__main__":
    n = 5
    graph = [[] for _ in range(n)]
    graph[0].extend([(1, 2), (3, 6)])
    graph[1].extend([(0, 2), (2, 3), (3, 8), (4, 5)])
    graph[2].extend([(1, 3), (4, 7)])
    graph[3].extend([(0, 6), (1, 8)])
    graph[4].extend([(1, 5), (2, 7)])

    mst = prim(graph, 0)
    print("MST edges (u, v, weight):", mst)