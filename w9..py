class Graph:
    def init(self, N):
        # Initialize the graph with a number of vertices
        self.N = N
        # Create a N x N matrix initialized with 0
        self.adj_matrix = [[0 for _ in range(N)] for _ in range(N)]

    def add_edge(self, u, v):
        # Add edge from u to v
        if u >= self.N or v >= self.N or u < 0 or v < 0:
            print("Invalid edge!")
        else:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1  # If undirected graph

    def remove_edge(self, u, v):
        # Remove edge from u to v
        if u >= self.N or u < 0:
            print("Vertex", u, "does not exist!")
        if v >= self.N or v < 0:
            print("Vertex", v, "does not exist!")
        if u==v:
            print("Same Vertext!")
        else:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0  # If undirected graph

    def display_matrix(self):
        # Display adjacency matrix
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)
g1 = Graph()
g1.init(6)
g1.add_edge(0,1)
g1.add_edge(0,2)
g1.add_edge(0,3)
g1.add_edge(0,4)
g1.add_edge(1,3)
g1.add_edge(4,2)
g1.add_edge(2,3)
g1.add_edge(2,5)
g1.add_edge(3,5)
g1.display_matrix()
g1.remove_edge(2,3)
g1.display_matrix()