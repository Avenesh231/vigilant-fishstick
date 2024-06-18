class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            (dist, node) = heapq.heappop(queue)
            if dist > distances[node]:
                continue
            for neighbor in self.graph[node]:
                old_dist = distances[neighbor]
                new_dist = distances[node] + 1
                if new_dist < old_dist:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
        return distances

    def bellman_ford(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        for _ in range(len(self.graph) - 1):
            for node in self.graph:
                for neighbor in self.graph[node]:
                    if distances[node] + 1 < distances[neighbor]:
                        distances[neighbor] = distances[node] + 1
        for node in self.graph:
            for neighbor in self.graph[node]:
                if distances[node] + 1 < distances[neighbor]:
                    return "Negative cycle detected"
        return distances

    def kruskal(self):
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((1, node, neighbor))
        edges.sort()
        mst = []
        parent = {}
        rank = {}
        for node in self.graph:
            parent[node] = node
            rank[node] = 0
        for edge in edges:
            weight, node1, node2 = edge
            if parent[node1] != parent[node2]:
                mst.append(edge)
                parent[node2] = parent[node1]
                rank[parent[node1]] += 1
        return mst

    def prim(self):
        mst = []
        parent = {}
        rank = {}
        for node in self.graph:
            parent[node] = node
            rank[node] = 0
        edges = []
        for node in self.graph:
            for neighbor in self.graph[node]:
                edges.append((1, node, neighbor))
        edges.sort()
        for edge in edges:
            weight, node1, node2 = edge
            if parent[node1] != parent[node2]:
                mst.append(edge)
                parent[node2] = parent[node1]
                rank[parent[node1]] += 1
        return mst

# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)

print("DFS:")
g.dfs(1)
print("\nBFS:")
g.bfs(1)
print("\nDijkstra's Algorithm:")
print(g.dijkstra(1))
print("\nBellman-Ford Algorithm:")
print(g.bellman_ford(1))
print("\nKruskal's Algorithm:")
print(g.kruskal())
print("\nPrim's Algorithm:")
print(g.prim())
