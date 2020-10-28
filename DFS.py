from succ import Succ
Root = {'value': 1, 'depth':1}

def DFS_Tree(node):
    nodes = [node]
    visited_nodes = []

    while len(nodes) > 0:
        current_node = nodes.pop()
        visited_nodes.append(current_node)
        nodes.extend(Succ(current_node))

    return visited_nodes

print(DFS_Tree(Root))
