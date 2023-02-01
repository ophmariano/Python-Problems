from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError
from trains.route_validator import validate_start_and_end_station_exists_in_route

MAX_STATIONS_STOP = 5


def number_of_trips_with_max_stops(start_station: str = '', end_station: str = '', max_stops=0, routes=None):
    if not routes:
        raise InvalidRouteError(value=routes)

    possible_trips = find_all_trips_with_less_stations_then(start_station, end_station, max_stops, routes)
    valid_trips = [trip for trip in possible_trips if trip[-1] == end_station]
    return len(valid_trips)


def number_of_trips_with_exactly_stops(start_station: str = '', end_station: str = '', exactly_stops=0, routes=None):
    if not routes:
        raise InvalidRouteError(value=routes)

    possible_trips = find_all_trips_with_less_stations_then(start_station, end_station, exactly_stops, routes)
    valid_trips = [trip for trip in possible_trips if len(trip) - 1 == exactly_stops]
    return len(valid_trips)


def find_all_trips_with_less_stations_then(start_station: str = '', end_station: str = '',
                                           max_number_of_stations: int = 0, routes=None,
                                           current_number_of_stations=0, path=None, all_paths=None):
    """

    :param start_station: Starting station
    :param end_station: Ending station
    :param max_number_of_stations: Maximum number of stops that this trip will have. Limited for recursive limit.
    :param routes: Routes used to generate the trips
    :param current_number_of_stations: Control the number of stations already visited in path
    :param path: Current trip path being explored
    :param all_paths: All found paths within the maximum number of stations
    :return: A list with all found solutions
    """
    validate_start_and_end_station_exists_in_route(routes, start_station, end_station)

    if max_number_of_stations > MAX_STATIONS_STOP:
        max_number_of_stations = MAX_STATIONS_STOP

    if not all_paths:
        all_paths = []

    if not path:
        path = []
    path = path + [start_station]

    not_fist_station = len(path) > 1
    if not_fist_station and start_station == end_station:
        all_paths.append(path)
        main_path_without_end_station = path[:-1]
        new_sub_paths = find_all_trips_with_less_stations_then(start_station, end_station, max_number_of_stations,
                                                               routes, current_number_of_stations)
        for new_sub_path in new_sub_paths:
            all_paths.append(main_path_without_end_station + new_sub_path)
        return all_paths

    for connection_station in routes.get(start_station):
        station = connection_station[0]
        current_number_of_stations += 1
        if current_number_of_stations > max_number_of_stations:
            return all_paths

        path_without_starting_station = path[1:]
        if station not in path_without_starting_station:
            new_found_paths = find_all_trips_with_less_stations_then(station, end_station, max_number_of_stations,
                                                                     routes, current_number_of_stations, path)
            current_number_of_stations -= 1
            for new_path in new_found_paths:
                if new_path not in all_paths:
                    all_paths.append(new_path)

    return all_paths
