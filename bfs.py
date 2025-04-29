from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)

    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)

        queue=[]
        queue.append(s)
        visited[s]=True

        while queue:
            s=queue.pop(0)
            print(s,end=' ')

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True

if __name__=='__main__':
    g=Graph()
    g.addedge(0,1)
    g.addedge(0,2)
    g.addedge(2,3)
    g.addedge(1,2)
    g.addedge(2,0)
    g.addedge(3,3)

    g.bfs(1)
        