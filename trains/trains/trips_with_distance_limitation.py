from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError
from trains.route_validator import validate_start_and_end_station_exists_in_route

TRIP_MAX_DISTANCE = 32


def number_of_trips_within_max_distance(start_station: str = '', end_station: str = '', max_distance=0, routes=None):
    """
    Find all possible trips with a total travelled distance
    :param start_station: The starting station
    :param end_station: The ending station
    :param max_distance: The max distance of the trip. Max values of TRIP_MAX_DISTANCE to safeguard in case of too many recursive calls
    :param routes: The routes used to find the trips
    :return: all possible paths within the distance
    """
    if not routes:
        raise InvalidRouteError(value=routes)

    possible_trips = find_all_trips_within_max_distance(start_station, end_station, max_distance, routes)
    valid_trips = [trip for trip in possible_trips if trip[-1] == end_station]
    return len(valid_trips)


def find_all_trips_within_max_distance(start_station: str = '', end_station: str = '',
                                       max_distance: int = 0, routes=None, current_distance=0,
                                       path=None, all_paths=None):
    """
    Find all possible trips with a total travelled distance
    :param start_station: The starting station
    :param end_station: The ending station
    :param max_distance: The max distance of the trip. Max values of TRIP_MAX_DISTANCE to safeguard in case of too many recursive calls
    :param routes: The routes used to find the trips
    :param current_distance: Control the distance of the path when looking for subpaths
    :param path: Current path being explored
    :param all_paths: List of all found paths
    :return: all possible paths within the distance
    """
    validate_start_and_end_station_exists_in_route(routes, start_station, end_station)

    if max_distance > TRIP_MAX_DISTANCE:
        max_distance = TRIP_MAX_DISTANCE

    if not all_paths:
        all_paths = []

    if not path:
        path = []
    path = path + [start_station]

    if start_station == end_station and len(path) > 1:
        all_paths.append(path)
        main_path_without_end_station = path[:-1]
        new_sub_paths = find_all_trips_within_max_distance(start_station, end_station, max_distance,
                                                           routes, current_distance)
        for new_sub_path in new_sub_paths:
            all_paths.append(main_path_without_end_station + new_sub_path)
        return all_paths

    for connection_station in routes[start_station]:
        station, distance = connection_station.split('_')
        current_distance += int(distance)
        if current_distance >= max_distance:
            current_distance -= int(distance)
            continue

        path_without_starting_station = path[1:]
        if station not in path_without_starting_station:
            new_found_paths = find_all_trips_within_max_distance(station, end_station, max_distance,
                                                                 routes, current_distance, path)
            current_distance -= int(distance)
            for new_path in new_found_paths:
                if new_path not in all_paths:
                    all_paths.append(new_path)
    return all_paths
