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

