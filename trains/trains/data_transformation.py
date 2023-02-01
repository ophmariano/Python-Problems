from collections import defaultdict


def create_route_graph(routes):
    route_graph = defaultdict(list)
    for route in routes.split(','):
        start, end, distance = [*route]
        route_graph[start].append(f'{end}_{distance}')
    return route_graph
