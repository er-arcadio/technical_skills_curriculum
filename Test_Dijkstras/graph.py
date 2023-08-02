graph = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 3, 2, 1, 0],
    [0, 0, 0, 1, 4, 0],
    [2, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 3],
    [0, 0, 0, 1, 0, 0]
]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

graph_map = {alphabet[idx]:ls for idx, ls in enumerate(graph)}


class Node():
    def __init__(self, name):
        self.name = name
        self.links = []
        
class Link():
    def __init__(self, edge, node):
        self.edge = edge
        self.node = node
        

node_mapping = {name:Node(name) for name in graph_map}
for name in node_mapping:
    for next_idx, next_edge in enumerate(graph_map[name]):
        if next_edge:
            link = Link(edge=next_edge, node=node_mapping[alphabet[next_idx]])
            node_mapping[name].links.append(link)

root = node_mapping['B']