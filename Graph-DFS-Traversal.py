# Add a vertex to the dictionary
def add_vertex(v):
  global graph
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    graph[v] = []

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    graph[v1].append(v2)
    graph[v2].append(v1)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0])

def DFS(node, visited):
    global graph
    if node not in visited:
        print(node)
        visited.add(node)

        for i in graph[node]:
            DFS(i,visited)

# driver code
visited = set()
graph = {}
add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')
add_vertex('E')

# Add the edges between the vertices by specifying the from and to vertex
add_edge('A', 'B')
add_edge('A', 'C')
add_edge('A', 'D')
add_edge('B', 'E')
add_edge('B', 'D')
add_edge('C', 'D')
add_edge('E', 'D')
print_graph()
# Reminder: the second element of each list inside the dictionary denotes the edges.
print ("Internal representation of graph:", graph)
print("DFS Traversal:\n")

DFS("A",visited)
