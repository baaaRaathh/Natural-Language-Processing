class graph:
    def __init__(self,size):
        self.size = size
        self.adj = [[0]* size for i in range(size)]
        self.vertices = [''] * size
        
    def add_edge(self,u,v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj[u][v] = 1
            self.adj[v][u] = 1
            
    def  add_vertices(self,u,data):
        if 0 <= u <  self.size:
            self.vertices[u] = data
            
    def print_graph(self):
        for i in self.adj:
            print(' '.join(map(str,i)))
            
        for i,j in enumerate(self.vertices):
            print(i,j)        
    
    def dfs_u(self,v,visite):
        visite[v] = True
        print(self.vertices[v],end=' ')
        
        for i in range(self.size):
            if self.adj[v][i] == 1 and not visite[i]:
                self.dfs_u(i,visite)
                        
    def dfs(self,start):
        visite = [False] * self.size
        start_in = self.vertices.index(start)
        self.dfs_u(start_in,visite)
        
   
                
g = graph(7)
g.add_vertices(0,'A')
g.add_vertices(1,'B')
g.add_vertices(2,'C')
g.add_vertices(3,'D')
g.add_vertices(4,'E')
g.add_vertices(5,'F')
g.add_vertices(6,'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

print("\nDepth First Search starting from vertex D:")
g.dfs('D')
