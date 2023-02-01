import unittest

from tests.test_helpers.test_helper import create_graph_route
from trains.exceptions import InvalidRouteError, InvalidArgumentError
from trains.trip_shortest_distance import shortest_trip_distance, shortest_trip_route


class TestTripShortest(unittest.TestCase):
    routes = []

    def setUp(self) -> None:
        self.routes = create_graph_route()

    def tearDown(self) -> None:
        self.routes = []

    """Tests for shortest_trip_distance"""

    def test_trip_distance_should_return_nine_units_as_shortest_route_distance_from_a_to_c(self):
        expected_distance = 9
        start_station = 'A'
        end_station = 'C'

        shortest_route_distance = shortest_trip_distance(start_station=start_station, end_station=end_station,
                                                         routes=self.routes)

        self.assertEqual(expected_distance, shortest_route_distance)

    def test_trip_distance_should_return_no_such_route_as_shortest_route_was_not_found(self):
        expected_no_such_route = 'NO SUCH ROUTE'
        start_station = 'A'
        end_station = 'A'

        shortest_route = shortest_trip_distance(start_station=start_station, end_station=end_station,
                                                routes=self.routes)

        self.assertEqual(expected_no_such_route, shortest_route)

    def test_trip_distance_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'

        with self.assertRaises(InvalidRouteError) as context:
            shortest_trip_distance(start_station=start_station, end_station=end_station)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_trip_distance_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'C'

        with self.assertRaises(InvalidArgumentError) as context:
            shortest_trip_distance(start_station=start_station, end_station=end_station, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_trip_distance_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'A'
        end_station = ''

        with self.assertRaises(InvalidArgumentError) as context:
            shortest_trip_distance(start_station=start_station, end_station=end_station, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    """Tests for shortest_trip_route"""

    def test_should_return_only_one_path_with_two_stations_as_shortest_route_from_a_to_b(self):
        expected_route = ['A', 'B']
        start_station = 'A'
        end_station = 'B'

        shortest_route = shortest_trip_route(start_station=start_station, end_station=end_station,
                                             routes=self.routes)

        self.assertEqual(expected_route, shortest_route)
        self.assertTrue(len(expected_route) == len(shortest_route))
