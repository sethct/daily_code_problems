#| Given an undirected graph represented as an adjacency matrix and an integer k,
#| write a function to determine whether each vertex in the graph can be colored
#| such that no two adjacent vertices share the same color using at most k colors.

#------------------#
# Define Functions #
#------------------#

def is_safe(node, graph, colors, c):
    """
    Check if it's safe to assign color c to node.
    :param node: The current node to color.
    :param graph: Graph represented as an adjacency matrix.
    :param colors: Assigned colors for the nodes.
    :param c: The color to check.
    :return: True if no adjacent node has color c, False otherwise.
    """
    for i in range(len(graph)):
        if graph[node][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(graph, m, colors, v):
    """
    Utilize backtracking to determine if the graph can be colored with m colors.
    :param graph: Graph represented as an adjacency matrix.
    :param m: The maximum number of colors.
    :param colors: Assigned colors for the nodes.
    :param v: The current vertex.
    :return: True if the graph can be colored with m or fewer colors, False otherwise.
    """
    #| If all vertices are assigned a color then return true
    if v == len(graph):
        return True

    #| Try different colors for vertex v
    for c in range(1, m + 1):
        #| Check if assignment of color c to v is fine
        if is_safe(v, graph, colors, c):
            colors[v] = c
            #| Recur to assign colors to the rest of the vertices
            if graph_coloring(graph, m, colors, v + 1):
                return True
            #| If assigning color c doesn't lead to a solution, remove it
            colors[v] = 0

    return False

def can_color_graph(graph, k):
    """
    Determine if the graph can be colored with at most k colors such that
    no two adjacent vertices share the same color.
    
    :param graph: Graph represented as an adjacency matrix.
    :param k: The maximum number of colors.
    :return: True if the graph can be colored with k or fewer colors, False otherwise.
    """
    #| Initialise all vertices as unassigned
    colors = [0] * len(graph)
    #| Start from the first vertex
    if graph_coloring(graph, k, colors, 0):
        return True
    else:
        return False

#------------------#
# Test Application #
#------------------#

if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    k = 3  # Number of colors
    print(can_color_graph(graph, k))  # Output: True
