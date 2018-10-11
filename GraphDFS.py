from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    #u and v are vertices forming the edge uv
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def dfs_check(self, v, visited):
        print(v)
        visited[v] = True

        for i in self.graph[v]:
            if(visited[i] == False):
                self.dfs_check(i, visited)

    def DFS(self, v):
        visited = [False] * len(self.graph)

        self.dfs_check(v, visited)

    def print(self):
        for i in self.graph:
            print(i)

g = Graph()
g.add_edge(0,5)
g.add_edge(0,4)
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(3,4)
g.add_edge(2,3)

g.print()
#g.DFS(0)