import unittest

from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError
from trains.trips_with_distance_limitation import number_of_trips_within_max_distance, \
    find_all_trips_within_max_distance, TRIP_MAX_DISTANCE
from tests.test_helpers.test_helper import create_graph_route


class TestTripWithinDistanceLimitation(unittest.TestCase):
    routes = []

    def setUp(self) -> None:
        self.routes = create_graph_route()

    def tearDown(self) -> None:
        self.routes = []

    """test for number_of_trips_within_max_distance"""

    def test_number_of_trips_should_return_one_route_from_a_to_c_with_ten_units_of_distance(self):
        expected_size = 1
        start_station = 'A'
        end_station = 'C'
        max_distance = 10

        max_distance_routes = number_of_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                                  max_distance=max_distance, routes=self.routes)

        self.assertTrue(expected_size == max_distance_routes)

    def test_number_of_trips_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'
        max_distance = 4

        with self.assertRaises(InvalidRouteError) as context:
            number_of_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                max_distance=max_distance)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_number_of_trips_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'C'
        max_distance = 4

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                max_distance=max_distance, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_number_of_trips_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'A'
        end_station = ''
        max_distance = 1

        with self.assertRaises(InvalidArgumentError) as context:
            number_of_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                max_distance=max_distance, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_number_of_trips_should_return_zero_if_exactly_stops_is_zero(self):
        expected_number_of_routes = 0
        start_station = 'A'
        end_station = 'C'
        max_distance = 0

        routes_within_max_distance = number_of_trips_within_max_distance(start_station=start_station,
                                                                         end_station=end_station,
                                                                         max_distance=max_distance,
                                                                         routes=self.routes)

        self.assertEqual(expected_number_of_routes, routes_within_max_distance)

    """test for number_of_trips_within_max_distance"""

    def test_find_all_should_return_three_routes_from_a_to_c_with_three_stops(self):
        expected_route = [['A', 'B', 'C'], ['A', 'B', 'C', 'E', 'B', 'C'], ['A', 'D', 'C'],
                          ['A', 'D', 'C', 'E', 'B', 'C'], ['A', 'D', 'E', 'B', 'C'], ['A', 'E', 'B', 'C'],
                          ['A', 'E', 'B', 'C', 'E', 'B', 'C']]
        start_station = 'A'
        end_station = 'C'
        max_distance = 25

        max_distance_routes = find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                                 max_distance=max_distance, routes=self.routes)

        self.assertEqual(expected_route, max_distance_routes)

    def test_find_all_should_respect_max_stop_limitation(self):
        expected_routes = 9
        start_station = 'C'
        end_station = 'C'
        max_distance_limit = TRIP_MAX_DISTANCE
        max_distance_double_limit = TRIP_MAX_DISTANCE * 2

        routes_with_limit = find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                               max_distance=max_distance_limit, routes=self.routes)
        routes_with_double_limit = find_all_trips_within_max_distance(start_station=start_station,
                                                                      end_station=end_station,
                                                                      max_distance=max_distance_double_limit,
                                                                      routes=self.routes)

        self.assertEqual(routes_with_limit, routes_with_double_limit)
        self.assertTrue(expected_routes == len(routes_with_limit))
        self.assertTrue(expected_routes == len(routes_with_double_limit))

    def test_find_all_should_return_empty_when_no_trip_is_found_for_route(self):
        expected_route = []
        start_station = 'A'
        end_station = 'A'
        max_distance = 32

        max_distance_routes = find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                                 max_distance=max_distance, routes=self.routes)

        self.assertEqual(expected_route, max_distance_routes)
        self.assertTrue(len(expected_route) == len(max_distance_routes))

    def test_find_all_should_return_start_station_if_exactly_stops_is_zero(self):
        expected_number_of_routes = []
        start_station = 'A'
        end_station = 'C'
        max_distance = 0

        all_possible_trips = find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                                                max_distance=max_distance, routes=self.routes)

        self.assertEqual(expected_number_of_routes, all_possible_trips)

    def test_find_all_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'
        max_distance = 4

        with self.assertRaises(InvalidRouteError) as context:
            find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                               max_distance=max_distance)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_find_all_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'C'
        max_distance = 4

        with self.assertRaises(InvalidArgumentError) as context:
            find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                               max_distance=max_distance, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_find_all_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'A'
        end_station = ''
        max_distance = 1

        with self.assertRaises(InvalidArgumentError) as context:
            find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                               max_distance=max_distance, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_find_all_should_raise_invalid_argument_if_start_station_does_not_exist(self):
        start_station = 'F'
        end_station = 'B'
        max_distance = 1

        with self.assertRaises(NoSuchRouteError) as context:
            find_all_trips_within_max_distance(start_station=start_station, end_station=end_station,
                                               max_distance=max_distance, routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)
