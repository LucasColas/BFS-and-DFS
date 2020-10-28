Root = {'value': 1, 'depth':1}

def Succ(node):
    if node['value'] == 5:
        return []

    elif node['value'] == 4:
        return [{'value':5, 'depth': node['depth']+1}]

    else:
        return [{'value': node['value']+1, \
                 'depth':node['depth']+1}, \
                 {'value':node['value']+2, \
                 'depth':node['depth']+1}]
