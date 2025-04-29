class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def find(self,parent,i):
        if parent[i]!=i:
            parent[i]=self.find(parent,parent[i])
        return parent[i]

    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)

        if rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        elif rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
            
    def kruskalMST(self):
        result=[]
        self.graph.sort()

        parent=[i for i in range(self.V)]
        rank=[0]*self.V

        e=0
        i=0

        while e<self.V-1:
            w,u,v=self.graph[i]
            i=i+1

            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:
                e=e+1
                result.append((u,v,w))
                self.union(parent,rank,x,y)

        self.printMST(result)

    def printMST(self,result):
        print("edges \tWeight")
        for u,v,weight in result:
            print(f"{u} - {v} \t{weight}")
            
if __name__=='__main__':
    g=Graph(5) 
    g.graph=[(2, 0, 1),
        (3, 1, 2),
        (6, 0, 3),
        (8, 1, 3),
        (5, 1, 4),
        (7, 2, 4),
        (9, 3, 4)]
    print("Kruskals edges: ---")
    g.kruskalMST()
            
        