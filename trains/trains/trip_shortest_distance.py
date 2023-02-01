from trains.exceptions import InvalidRouteError
from trains.route_validator import validate_start_and_end_station_exists_in_route
from trains.trip_distance_calculator import calculate_trip_distance


def shortest_trip_distance(start_station: str = '', end_station: str = '', routes=None):
    no_such_route = 'NO SUCH ROUTE'
    if not routes:
        raise InvalidRouteError(value=routes)

    shortest_path = shortest_trip_route(start_station, end_station, routes)
    if not shortest_path:
        return no_such_route

    trip = '-'.join(shortest_path) if shortest_path else shortest_path
    return calculate_trip_distance(trip, routes)


def shortest_trip_route(start_station: str = '', end_station: str = '', routes=None, path=None):
    """
    Find the shortest trip path between two stations
    :param start_station: Starting station
    :param end_station: Ending station
    :param routes: Routes used to generate the trips
    :param path: Current trip path being explored
    :return: The shortest path
    """
    validate_start_and_end_station_exists_in_route(routes, start_station, end_station)

    if not path:
        path = []

    path = path + [start_station]

    if start_station == end_station and len(path) > 1:
        return path

    shortest = None

    for connection_station in routes.get(start_station):
        station = connection_station[0]
        path_without_starting_station = path[1:]

        if station not in path_without_starting_station:
            new_path = shortest_trip_route(station, end_station, routes, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest
