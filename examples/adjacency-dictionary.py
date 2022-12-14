from collections import defaultdict
from rosmontis import renderGraphDict

# g[i] = [node1, node2], meaning there is a undirected path
# from node1 to node2
g1 = [["A", "B"], ["A", "E"], ["B", "E"], 
      ["B", "C"], ["C", "D"], ["D", "E"], ["D", "F"]]

# g[i] = [node1, node2, weight], where the third value "weight" represents the 
# weight between the edge that connects node1 and node 2
g2 = [["A", "B", 2], ["A", "E", 0.5], ["B", "E", 0.2], 
      ["B", "C", 3], ["C", "D", 7], ["D", "E", 0.15], ["D", "F", 1.6]]

# Create a graph using dictionary as representation
# ------------------------------------------------------------------------------
# Uneighted, Undirect
map1 = defaultdict(list)
for i, e in enumerate(g1):
    map1[g1[i][0]].append(g1[i][1])

# map1 becomes the following
# map1 = {'A': ['B', 'E'], 
#         'B': ['E', 'C'], 
#         'C': ['D'], 
#         'D': ['E', 'F']}

# output a png image representing the graph in the same
# directory of this file.
renderGraphDict(graph=map1, graphName="unweighted-undirect", 
                          weighted=False, directed=False)

# ------------------------------------------------------------------------------
# Uneighted Direct
map2 = map1

# map2 = {'A': ['B', 'E'], 
#         'B': ['E', 'C'], 
#         'C': ['D'], 
#         'D': ['E', 'F']}

renderGraphDict(graph=map2, graphName="unweighted-direct",
                          weighted=False, directed=True)

# ------------------------------------------------------------------------------
# Weighted, Undirect
map3 = defaultdict(list)
for i, e in enumerate(g2):
    map3[g2[i][0]].append([g2[i][1], g2[i][2]])

# map3 = {'A': [['B', 2], ['E', 0.5]], 
#         'B': [['E', 0.2], ['C', 3]], 
#         'C': [['D', 7]], 
#         'D': [['E', 0.15], ['F', 1.6]]}

renderGraphDict(graph=map3, graphName="weighted-undirect", 
                          weighted=True, directed=False)

# ------------------------------------------------------------------------------
# Weighted Direct
map4 = map3

# map4 = {'A': [['B', 2], ['E', 0.5]], 
#         'B': [['E', 0.2], ['C', 3]], 
#         'C': [['D', 7]], 
#         'D': [['E', 0.15], ['F', 1.6]]}

renderGraphDict(graph=map4, graphName="weighted-direct",
                          weighted=True, directed=True)
