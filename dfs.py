from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def dfsutil(self,v,visited):
        visited[v]=True
        print(v,end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfsutil(i,visited)

    def dfs(self,v):
        visited=[False]*(max(self.graph)+1)
        self.dfsutil(v,visited)

if __name__=='__main__':
    g=Graph()
    g.addedge(0,1)
    g.addedge(0,2)
    g.addedge(1,2)
    g.addedge(2,3)
    g.addedge(3,3)
    g.addedge(2,0)

    g.dfs(2)