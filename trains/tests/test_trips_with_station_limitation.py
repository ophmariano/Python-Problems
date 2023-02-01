import unittest

from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError
from trains.trips_with_station_limitation import number_of_trips_with_max_stops, number_of_trips_with_exactly_stops, \
    find_all_trips_with_less_stations_then, MAX_STATIONS_STOP
from tests.test_helpers.test_helper import create_graph_route


class TestTripsWithStationLimitation(unittest.TestCase):
    routes = []

    def setUp(self) -> None:
        self.routes = create_graph_route()

    def tearDown(self) -> None:
        self.routes = []

    """tests for number_of_trips_with_exactly_stops"""

    def test_exactly_stops_should_return_one_route_from_a_to_c_with_three_stops(self):
        expected_number_of_routes = 1
        start_station = 'A'
        end_station = 'C'
        exactly_stops = 3

        exactly_stops_routes = number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                                                  exactly_stops=exactly_stops, routes=self.routes)

        self.assertEqual(expected_number_of_routes, exactly_stops_routes)

    def test_exactly_stops_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'
        exactly_stops = 4

        with self.assertRaises(InvalidRouteError) as context:
            number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                               exactly_stops=exactly_stops)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_exactly_stops_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'C'
        exactly_stops = 4

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                               exactly_stops=exactly_stops, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_exactly_stops_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'A'
        end_station = ''
        exactly_stops = 1

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                               exactly_stops=exactly_stops, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_exactly_stops_should_return_zero_if_exactly_stops_is_zero(self):
        expected_number_of_routes = 0
        start_station = 'A'
        end_station = 'C'
        exactly_stops = 0

        exactly_stops_routes = number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                                                  exactly_stops=exactly_stops, routes=self.routes)

        self.assertEqual(expected_number_of_routes, exactly_stops_routes)

    def test_exactly_stops_should_return_empty_if_start_station_does_not_exist(self):
        start_station = 'F'
        end_station = 'B'
        exactly_stops = 0

        with self.assertRaises(NoSuchRouteError) as context:
            number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                               exactly_stops=exactly_stops, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    def test_exactly_stops_should_return_empty_if_end_station_does_not_exist(self):
        start_station = 'A'
        end_station = 'V'
        exactly_stops = 0

        with self.assertRaises(NoSuchRouteError) as context:
            number_of_trips_with_exactly_stops(start_station=start_station, end_station=end_station,
                                               exactly_stops=exactly_stops, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    """tests for number_of_trips_with_max_of_stops"""

    def test_max_stops_should_return_three_routes_from_a_to_c_with_three_stops(self):
        expected_number_of_routes = 3
        start_station = 'A'
        end_station = 'C'
        max_stops = 3

        max_stops_routes = number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                                          max_stops=max_stops, routes=self.routes)

        self.assertEqual(expected_number_of_routes, max_stops_routes)

    def test_max_stops_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'
        max_stops = 3

        with self.assertRaises(InvalidRouteError) as context:
            number_of_trips_with_max_stops(start_station=start_station, end_station=end_station, max_stops=max_stops)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_max_stops_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'D'
        max_stops = 4

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                           max_stops=max_stops, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_max_stops_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'B'
        end_station = ''
        max_stops = 1

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                           max_stops=max_stops, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_max_stops_should_return_zero_if_exactly_stops_is_zero(self):
        expected_number_of_routes = 0
        start_station = 'A'
        end_station = 'B'
        max_stops = 0

        max_stops_routes = number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                                          max_stops=max_stops, routes=self.routes)

        self.assertEqual(expected_number_of_routes, max_stops_routes)

    def test_max_stops_should_return_empty_if_start_station_does_not_exist(self):
        start_station = 'F'
        end_station = 'B'
        max_stops = 0

        with self.assertRaises(NoSuchRouteError) as context:
            number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                           max_stops=max_stops, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    def test_max_stops_should_return_empty_if_end_station_does_not_exist(self):
        start_station = 'A'
        end_station = 'V'
        max_stops = 0

        with self.assertRaises(NoSuchRouteError) as context:
            number_of_trips_with_max_stops(start_station=start_station, end_station=end_station,
                                           max_stops=max_stops, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    """tests for find_all_trips_with_less_stations_then"""

    def test_find_all_trips_should_return_six_routes_from_a_to_c_with_four_stops(self):
        expected_route = [['A', 'B', 'C'], ['A', 'B', 'C', 'D', 'C'], ['A', 'D', 'C'], ['A', 'D', 'C', 'D', 'C'],
                          ['A', 'D', 'E', 'B', 'C'], ['A', 'E', 'B', 'C']]
        start_station = 'A'
        end_station = 'C'
        max_number_of_stations = 4

        all_routes_found = find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                                  max_number_of_stations=max_number_of_stations,
                                                                  routes=self.routes)

        self.assertEqual(expected_route, all_routes_found)
        self.assertTrue(len(expected_route) == len(all_routes_found))

    def test_find_all_trips_should_respect_max_stop_limitation(self):
        expected_route = [['A', 'B', 'C'], ['A', 'B', 'C', 'D', 'C'], ['A', 'B', 'C', 'E', 'B', 'C'], ['A', 'D', 'C'],
                          ['A', 'D', 'C', 'D', 'C'], ['A', 'D', 'C', 'E', 'B', 'C'], ['A', 'D', 'E', 'B', 'C'],
                          ['A', 'E', 'B', 'C'], ['A', 'E', 'B', 'C', 'D', 'C']]
        start_station = 'A'
        end_station = 'C'
        max_number_of_stations = 10
        initial_station = 1
        expected_max_len = MAX_STATIONS_STOP + initial_station

        all_routes_found = find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                                  max_number_of_stations=max_number_of_stations,
                                                                  routes=self.routes)
        max_len = max([len(route) for route in all_routes_found])

        self.assertEqual(expected_route, all_routes_found)
        self.assertTrue(len(expected_route) == len(all_routes_found))
        self.assertTrue(max_len == expected_max_len)

    def test_find_all_trips_should_return_empty_when_no_trip_is_found_for_route(self):
        expected_route = []
        start_station = 'A'
        end_station = 'A'
        max_number_of_stations = 4

        all_routes_found = find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                                  max_number_of_stations=max_number_of_stations,
                                                                  routes=self.routes)

        self.assertEqual(expected_route, all_routes_found)
        self.assertTrue(len(expected_route) == len(all_routes_found))

    def test_find_all_trips_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'A'
        max_number_of_stations = 4

        with self.assertRaises(InvalidRouteError) as context:
            find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                   max_number_of_stations=max_number_of_stations)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_find_all_trips_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'E'
        max_number_of_stations = 2

        with self.assertRaises(InvalidArgumentError) as context:
            find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                   max_number_of_stations=max_number_of_stations, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_find_all_trips_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'E'
        end_station = ''
        max_number_of_stations = 12

        with self.assertRaises(InvalidArgumentError) as context:
            find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                   max_number_of_stations=max_number_of_stations, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_find_all_trips_should_return_empty_if_exactly_stops_is_zero(self):
        expected_number_of_routes = []
        start_station = 'A'
        end_station = 'B'
        max_number_of_stations = 0

        all_routes_found = find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                                  max_number_of_stations=max_number_of_stations,
                                                                  routes=self.routes)

        self.assertEqual(expected_number_of_routes, all_routes_found)

    def test_find_all_trips_should_return_empty_if_start_station_does_not_exist(self):
        start_station = 'F'
        end_station = 'B'
        max_number_of_stations = 0

        with self.assertRaises(NoSuchRouteError) as context:
            find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                   max_number_of_stations=max_number_of_stations, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    def test_find_all_trips_should_return_empty_if_end_station_does_not_exist(self):
        start_station = 'A'
        end_station = 'V'
        max_number_of_stations = 0

        with self.assertRaises(NoSuchRouteError) as context:
            find_all_trips_with_less_stations_then(start_station=start_station, end_station=end_station,
                                                   max_number_of_stations=max_number_of_stations, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)


