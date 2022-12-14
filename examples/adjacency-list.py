from collections import defaultdict
from rosmontis import renderGraphList

# g[i] = [node1, node2], meaning there is a undirected path
# from node1 to node2
g1 = [["A", "B"], ["A", "E"], ["B", "E"], 
      ["B", "C"], ["C", "D"], ["D", "E"], ["D", "F"]]

g2 = [["A", "B", 2], ["A", "E", 0.5], ["B", "E", 0.2], 
      ["B", "C", 3], ["C", "D", 7], ["D", "E", 0.15], ["D", "F", 1.6]]

# ------------------------------------------------------------------------------
# Uneighted, Undirect
# Create a graph using adjacency list as representation
adjList1 = []
map1 = defaultdict(list)
for i, e in enumerate(g1):
    map1[g1[i][0]].append(g1[i][1])

for key, edges in map1.items():
    adjList1.append([key, edges])

# adjList1 becomes the following
# adjList1 = [['A', ['B', 'E']], 
#             ['B', ['E', 'C']], 
#             ['C', ['D']], 
#             ['D', ['E', 'F']]]

# output a png image representing the graph in the same
# directory of this file.
renderGraphList(graph=adjList1, graphName="unweighted-undirect", 
                          weighted=False, directed=False)

# ------------------------------------------------------------------------------
# Unweighted, Direct
adjList2 = adjList1

# adjList2= [['A', ['B', 'E']], 
#             ['B', ['E', 'C']], 
#             ['C', ['D']], 
#             ['D', ['E', 'F']]]

renderGraphList(graph=adjList2, graphName="unweighted-direct",
                          weighted=False, directed=True)

# ------------------------------------------------------------------------------
# Weighted, Undirect
adjList3 = []
map2 = defaultdict(list)
for i, e in enumerate(g2):
    map2[g2[i][0]].append([g2[i][1], g2[i][2]])

for key, edges in map2.items():
    adjList3.append([key, edges])

# adjList3 = [['A', [['B', 2], ['E', 0.5]]], 
#             ['B', [['E', 0.2], ['C', 3]]], 
#             ['C', [['D', 7]]], 
#             ['D', [['E', 0.15], ['F', 1.6]]]]

renderGraphList(graph=adjList3, graphName="weighted-undirect", 
                          weighted=True, directed=False)

# ------------------------------------------------------------------------------
# Weighted, Direct
adjList4 = adjList3
# adjList4 = [['A', [['B', 2], ['E', 0.5]]], 
#             ['B', [['E', 0.2], ['C', 3]]], 
#             ['C', [['D', 7]]], 
#             ['D', [['E', 0.15], ['F', 1.6]]]]

renderGraphList(graph=adjList4, graphName="weighted-direct",
                          weighted=True, directed=True)
