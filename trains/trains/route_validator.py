from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError


def validate_start_and_end_station_exists_in_route(routes=None, start_station: str = '', end_station: str = ''):
    if not routes:
        raise InvalidRouteError(value=routes)

    if not start_station:
        raise InvalidArgumentError(key='start_station', value=start_station)

    if routes.get(start_station) is None:
        raise NoSuchRouteError()

    if not end_station:
        raise InvalidArgumentError(key='end_station', value=end_station)

    if routes.get(end_station) is None:
        raise NoSuchRouteError()
