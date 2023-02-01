from trains.exceptions import InvalidRouteError, InvalidArgumentError


def calculate_trip_distance(trip_route: str = '', routes=None):
    """
    Calculate de total distance of a trip.
    :param routes: Routes to calculate trip.
    :param trip_route: Desired trip to calculate distance from.
    :return: The total distance of a trip.
    """
    if not routes:
        raise InvalidRouteError(value=routes)

    if not trip_route:
        raise InvalidArgumentError(key='trip_route', value=trip_route)

    if len(trip_route) <= 1:
        raise InvalidArgumentError(key='trip_route', value=trip_route, expected='More than 1 station')

    no_such_route = 'NO SUCH ROUTE'

    route_stations = trip_route.upper().split('-')
    total_distance = 0

    for start_station, next_station in zip(route_stations, route_stations[1:]):
        route_distance = route_distance_from_start_to_end(start_station, next_station, routes)

        if not route_distance:
            return no_such_route

        total_distance += route_distance
    return total_distance


def route_distance_from_start_to_end(start_station: str = '', end_station: str = '', routes=None) -> int:
    if not routes:
        raise InvalidRouteError(value=routes)

    if not start_station:
        raise InvalidArgumentError(key='start_station', value=start_station)

    if not end_station:
        raise InvalidArgumentError(key='end_station', value=end_station)

    routes_for_start_station = routes.get(start_station)
    distance = 0

    if not routes_for_start_station:
        return distance

    for end_route in routes_for_start_station:
        end_route_station = end_route[0]
        if end_route_station == end_station:
            distance = int(end_route[-1])
            return distance

    return distance
