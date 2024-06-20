class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u][v] = w

    def shortestPath(self, src):
        dist = [float('Inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = min(range(self.V), key=lambda i: dist[i])
            visited[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print("Shortest distances from source vertex %d:" % src)
        for i in range(self.V):
            print("Vertex %d: %d" % (i, dist[i]))

if __name__ == "__main__":
    V = 7
    g = Graph(V)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 2, 6)
    g.addEdge(1, 3, 5)
    g.addEdge(2, 3, 8)
    g.addEdge(3, 4, 10)
    g.addEdge(3, 5, 15)
    g.addEdge(4, 6, 2)
    g.addEdge(5, 6, 6)
    g.shortestPath(0)
