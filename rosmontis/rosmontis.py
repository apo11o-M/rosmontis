import graphviz as gz
from typing import Any

def renderGraphDict(graph: dict, 
                    graphName: str="default", 
                    weighted: bool=False,
                    directed: bool=False,
                    engine: str="neato",
                    outputFormat: str="png") -> str:
    """
    Create a graph image from an adjacency dictionary.

    Args:
        `graph`: The adjacency dictionary
        `graphName`: The name of the graph. (defaults to `default.png`)
        `weighted`: Whether the graph is weighted. (defaults to `False`)
        `directed`: Whether the graph is directed. (defaults to `False`)
        `engine`: Layout engine for rendering. (defaults to `neato`)
        `outputFormat`: The output file format. (defaults to `png`)

    Returns:
        The (possibly relative) path to the rendered image.
    """
    
    g = []
    for e in graph.items():
        g.append(list(e))

    return renderGraphList(graph=g, graphName=graphName, 
                                weighted=weighted, directed=directed, 
                                engine=engine, outputFormat=outputFormat)

def renderGraphList(graph: list,
                    graphName: str="default",
                    weighted: bool=False,
                    directed: bool=False,
                    engine: str="neato",
                    outputFormat: str="png") -> str:
    """
    Create a graph image from an adjacency dictionary.

    Args:
        `graph`: The adjacency list
        `graphName`: The name of the graph. (defaults to `default.png`)
        `weighted`: Whether the graph is weighted. (defaults to `False`)
        `directed`: Whether the graph is directed. (defaults to `False`)
        `engine`: Layout engine for rendering. (defaults to `neato`)
        `outputFormat`: The output file format. (defaults to `png`)

    Returns:
        The (possibly relative) path to the rendered image.

    Example:
        >>> import rosmontis
        >>> g = 
        >>> renderGraphMatrix(g, weighted="False", directed="False")
    """

    if len(graphName) == 0:
        graphName = "default"
    g = gz.Digraph(graphName) if directed else gz.Graph(graphName)
    g.attr("node", shape="circle")
    nodes = set()
    if (weighted):
        # Loop through the graph to find all the nodes that has appeared
        # O(n + v) time complexity 
        for n, e in graph:
            nodes.add(str(n))
            for edges in e:
                nodes.add(str(edges[0]))

        # Sort the nodes set, this is to ensure the .dot file output is the same
        # across different runs.
        nodes = sorted(nodes)
        
        # Create the nodes for graphviz
        for n in nodes:
            g.node(name=str(n), label=str(n[0]))            
        
        # Loop through the graph and create edges
        # O(n + v) time complexity 
        for n, e in graph:
            for edge in e:
                g.edge(tail_name=str(n), head_name=str(edge[0]), 
                    label=str(edge[1]))
    else:
        for n, e in graph:
            nodes.add(str(n))
            for edges in e:
                nodes.add(str(edges))
        
        nodes = sorted(nodes)

        for n in nodes:
            g.node(name=str(n), label=str(n))

        for n, e in graph:
            for edge in e:
                g.edge(tail_name=str(n), head_name=str(edge))
        
    # Render the graph to a png file
    return g.render(graphName, format=outputFormat, engine=engine)

def renderGraphMatrix(graph: list[list[Any]],
                      graphName: str="default",
                      weighted: bool=False,
                      directed: bool=False,
                      engine: str="neato",
                      outputFormat: str="png") -> str:
    """
    Create a graph image from an adjacency matrix.

    Args:
        `graph`: The adjacency dictionary
        `graphName`: The name of the graph. (defaults to `default.png`)
        `weighted`: Whether the graph is weighted. (defaults to `False`)
        `directed`: Whether the graph is directed. (defaults to `False`)
        `engine`: Layout engine for rendering. (defaults to `neato`)
        `outputFormat`: The output file format. (defaults to `png`)

    Returns:
        The (possibly relative) path to the rendered image.
    
    Example:
        >>> import rosmontis
        >>> g = [[None, "A", "B", "C", "D", "E", "F"],
                ["A",   0,   1,   0,   0,   1,   0 ],
                ["B",   1,   0,   1,   0,   1,   0 ],
                ["C",   0,   1,   0,   1,   0,   0 ],
                ["D",   0,   0,   1,   0,   1,   1 ],
                ["E",   1,   1,   0,   1,   0,   0 ],
                ["F",   0,   0,   0,   1,   0,   0 ]]
        >>> renderGraphMatrix(g, weighted="False", directed="False")
    """

    if len(graphName) == 0:
        graphName = "default"
    g = gz.Digraph(graphName) if directed else gz.Graph(graphName)
    g.attr("node", shape="circle")

    # Create the nodes for graphviz
    for i in range(1, len(graph)):
        g.node(name=str(graph[0][i]), label=str(graph[0][i]))

    # Go through every edge in this graph. O(v^2) time complexity
    for i in range(1, len(graph)):
        for j in range((1 if directed else i), len(graph[i])):
            if (graph[i][j] != 0):
                if (weighted):
                    g.edge(tail_name=str(graph[i][0]), 
                        head_name=str(graph[0][j]), 
                        label=str(graph[i][j]))
                else:
                    g.edge(tail_name=str(graph[i][0]), 
                        head_name=str(graph[0][j]))

    return g.render(graphName, format=outputFormat, engine=engine)
