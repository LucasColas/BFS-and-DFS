from succ import Succ
Root = {'value': 1, 'depth':1}
def BFS_Tree(node):
    nodes = [node]
    print(nodes)
    visited_nodes = []
    i = 0

    while len(node) > 0:
        print(i)
        i += 1
        current_node = nodes.pop(0)
        visited_nodes.append(current_node)
        nodes.extend(Succ(current_node))
    return nodes

print(BFS_Tree(Root))
