MAX = 30

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

class EdgeList:
    def __init__(self):
        self.data = [Edge(0, 0, 0) for _ in range(MAX)]
        self.n = 0

elist = EdgeList()

Graph = [[0 for _ in range(MAX)] for _ in range(MAX)]
n = 6

spanlist = EdgeList()

def find(belongs, vertexno):
    return belongs[vertexno]

def apply_union(belongs, c1, c2):
    for i in range(n):
        if belongs[i] == c2:
            belongs[i] = c1

def sort_edges():
    for i in range(1, elist.n):
        for j in range(elist.n - 1):
            if elist.data[j].w > elist.data[j + 1].w:
                elist.data[j], elist.data[j + 1] = elist.data[j + 1], elist.data[j]

def kruskal_algo():
    belongs = list(range(n))
    elist.n = 0

    for i in range(1, n):
        for j in range(i):
            if Graph[i][j] != 0:
                elist.data[elist.n] = Edge(i, j, Graph[i][j])
                elist.n += 1

    sort_edges()

    spanlist.n = 0

    for i in range(elist.n):
        cno1 = find(belongs, elist.data[i].u)
        cno2 = find(belongs, elist.data[i].v)

        if cno1 != cno2:
            spanlist.data[spanlist.n] = elist.data[i]
            spanlist.n += 1
            apply_union(belongs, cno1, cno2)

def print_result():
    cost = 0
    for i in range(spanlist.n):
        print(f"{spanlist.data[i].u} - {spanlist.data[i].v} : {spanlist.data[i].w}")
        cost += spanlist.data[i].w
    print(f"Spanning tree cost: {cost}")

if __name__ == "__main__":
    Graph[0][1] = 4
    Graph[0][2] = 4
    Graph[1][0] = 4
    Graph[1][2] = 2
    Graph[2][0] = 4
    Graph[2][1] = 2
    Graph[2][3] = 3
    Graph[2][4] = 4
    Graph[3][2] = 3
    Graph[3][4] = 3
    Graph[4][2] = 4
    Graph[4][3] = 3
    Graph[5][2] = 2
    Graph[5][4] = 3

    kruskal_algo()
    print_result()
