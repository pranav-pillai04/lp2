import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for _ in range(vertices)] for _ in range(vertices)]

    def minkey(self,key,mstSet):
        min_val=sys.maxsize
        min_index=-1

        for v in range(self.V):
            if key[v]<min_val and not mstSet[v]:
                min_val=key[v]
                min_index=v
        return min_index

    def primMST(self):
        key=[sys.maxsize]*self.V
        parent=[None]*self.V
        key[0]=0
        mstSet=[False]*self.V
        parent[0]=-1

        for _ in range(self.V):
            u=self.minkey(key,mstSet)
            mstSet[u]=True

            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u

        self.printMST(parent)

    def printMST(self,parent):
        print("EDGE \tWeight")
        for i in range(1,self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")

if __name__=='__main__':
    g=Graph(5)
    g.graph=[[0,2,1,0,4],
             [2,0,3,1,0],
             [0,1,4,8,0],
             [1,0,2,9,6],
             [2,0,0,3,7]]
    g.primMST()
    