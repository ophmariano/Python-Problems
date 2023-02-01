def create_graph_route():
    route_graph = {'A': ['B_5', 'D_5', 'E_7'],
                   'B': ['C_4'],
                   'C': ['D_8', 'E_2'],
                   'D': ['C_8', 'E_6'],
                   'E': ['B_3']}
    return route_graph

