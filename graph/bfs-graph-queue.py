

from collections import defaultdict

 #This class represents a directed graph using adjacency list representation 
class Graph: 
    visited = [] # List to keep track of visited nodes.
    queue = []     #Initialize a queue
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
       
     # Use BFS to check path between s and d 
    def isReachable(self, s, d): 
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
   
        # Create a queue for BFS 
        queue=[] 
   
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
   
        while queue: 
  
            #Dequeue a vertex from queue  
            n = queue.pop(0) 
              
            # If this adjacent node is the destination node, 
            # then return true 
            if n == d: 
                 return True
  
            #  Else, continue to do BFS 
            for i in self.graph[n]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
         # If BFS is complete without visited d 
        return False

    # First, move horizontally and visit all the nodes of the current layer  
    # Move to the next layer  
    # visited- List to keep track of visited nodes. 
    def bfs(self, visited, graph, node): 
        visited.append(node) 
        self.queue.append(node) 
        while self.queue: 
            s = self.queue.pop(0) # removed element  
            print (s, end = " ") 
            for neighbour in graph[s]: 
                if neighbour not in visited: 
                    visited.append(neighbour) 
                    self.queue.append(neighbour)
  
# Create a graph
g = Graph(4) # 4 vertices
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
u =0; v = 3
  
if g.isReachable(u, v): 
    print("There is a path from %d to %d" % (u,v)) 
else : 
    print("There is no path from %d to %d" % (u,v)) 
  
graph = { 
  'A' : ['B','C'], 
  'B' : ['D', 'E'], 
  'C' : ['F'], 
  'D' : [], 
  'E' : ['F'], 
  'F' : [] 
}

# To avoid processing a node more than once,
# g.bfs(g.visited, graph, 'A')  # A B C D E F
g.bfs(g.visited, graph, 'C') # C F 






