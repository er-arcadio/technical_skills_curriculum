from graph import root

# class Node():
#     def __init__(self, name):
#         self.name = name
#         self.links = [] # list of Links
        
# class Link():
#     def __init__(self, edge, node):
#         self.edge = edge
#         self.node = node # data type is Node


def shortest_path(root, destination):
    queue = [root]
    shortest_map = {
        root.name: {
            'value': 0,
            'prev_node': None
        },
        destination: {
            'value': float('inf'),
            'prev_node': None
        }
    }
    while queue:
        current_node = queue.pop(0)
        cn_map = shortest_map[current_node.name]

        # conditions
        arrived_at_destination = current_node.name == destination # Have we arrived at the destination?
        already_surpassed_shortest = cn_map.value >= shortest_map[destination].value # Have we already traveled farther than shortest?

        if not arrived_at_destination and not already_surpassed_shortest:
            # for each child of current node
            for link in current_node.links:
                next_node = link.node.name
                total_distance = cn_map.value + link.edge
                # add the child to the queue
                queue.append(link.node)
                # If it's unvisited
                if next_node not in shortest_map:
                    shortest_map[next_node] = {
                        'value': total_distance,
                        'prev_node':current_node.name
                    }
                # If the current path is shorter than previous, replace
                elif total_distance < shortest_map[next_node].value:
                    shortest_map[next_node].value = total_distance
                    shortest_map[next_node].prev_node = current_node.name
        elif arrived_at_destination:
            print(shortest_map[destination])
    
    #synthesize map
    sp = []
    cn = destination
    while cn != root.name:
        sp.insert(0, cn)
        if shortest_map[cn].prev_node:
            cn = shortest_map[cn].prev_node
        else:
            return []
    return {'path':sp, 'distance':shortest_map[destination].value}
            




print( "Shortest Path:", shortest_path(root, 'E'))