import unittest

from tests.test_helpers.test_helper import create_graph_route
from trains.exceptions import InvalidRouteError, InvalidArgumentError
from trains.trip_distance_calculator import calculate_trip_distance, route_distance_from_start_to_end


class TestTripDistance(unittest.TestCase):
    routes = []

    def setUp(self) -> None:
        self.routes = create_graph_route()

    def tearDown(self) -> None:
        self.routes = []

    """test for calculate_trip_distance"""

    def test_calculate_trip_should_calculate_trip_a_b_c_distance_of_nine_units(self):
        expected_trip_distance = 9
        trip_route = 'A-B-C'
        trip_distance = calculate_trip_distance(trip_route=trip_route, routes=self.routes)
        self.assertEqual(expected_trip_distance, trip_distance)

    def test_calculate_trip_should_raise_error_when_no_trip_informed(self):
        trip_route = 'A-B-D'

        with self.assertRaises(InvalidRouteError) as context:
            calculate_trip_distance(trip_route)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_calculate_trip_should_raise_error_with_single_trip_station(self):
        trip_route = 'A'
        with self.assertRaises(InvalidArgumentError) as context:
            calculate_trip_distance(trip_route=trip_route, routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: trip_route | Value: A | Expected value: More than 1 '
                         'station .', context.exception.message)

    def test_calculate_trip_should_raise_error_when_no_trip_is_provided(self):
        with self.assertRaises(InvalidArgumentError) as context:
            calculate_trip_distance(routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: trip_route | Value: Argument is an empty string .',
                         context.exception.message)

    def test_calculate_trip_should_return_no_such_found_when_invalid_route_in_trip(self):
        expected_trip_message = 'NO SUCH ROUTE'
        trip_route = 'A-B-F'
        trip_distance = calculate_trip_distance(trip_route=trip_route, routes=self.routes)
        self.assertEqual(expected_trip_message, trip_distance)

    def test_calculate_trip_should_return_no_such_found_when_starting_and_ending_are_the_same(self):
        expected_trip_message = 'NO SUCH ROUTE'
        trip_route = 'A-A'
        trip_distance = calculate_trip_distance(trip_route=trip_route, routes=self.routes)
        self.assertEqual(expected_trip_message, trip_distance)

    """test for route_distance_from_start_to_end"""

    def test_route_distance_should_return_five_from_a_to_b(self):
        expected_distance = 5
        start_station = 'A'
        end_station = 'B'
        route_distance = route_distance_from_start_to_end(start_station=start_station, end_station=end_station,
                                                          routes=self.routes)

        self.assertEqual(expected_distance, route_distance)

    def test_route_distance_should_return_distance_as_an_integer(self):
        start_station = 'A'
        end_station = 'D'
        route_distance = route_distance_from_start_to_end(start_station=start_station, end_station=end_station,
                                                          routes=self.routes)

        self.assertTrue(type(route_distance) == int)

    def test_route_distance_should_return_zero_if_start_station_does_not_exist(self):
        expected_distance = 0
        start_station = 'X'
        end_station = 'D'
        route_distance = route_distance_from_start_to_end(start_station=start_station, end_station=end_station,
                                                          routes=self.routes)

        self.assertEqual(expected_distance, route_distance)

    def test_route_distance_should_return_zero_if_end_station_does_not_exist(self):
        expected_distance = 0
        start_station = 'A'
        end_station = 'P'
        route_distance = route_distance_from_start_to_end(start_station=start_station, end_station=end_station,
                                                          routes=self.routes)

        self.assertEqual(expected_distance, route_distance)

    def test_route_distance_should_raise_invalid_route_error_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'

        with self.assertRaises(InvalidRouteError) as context:
            route_distance_from_start_to_end(start_station=start_station, end_station=end_station)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_route_distance_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'B'

        with self.assertRaises(InvalidArgumentError) as context:
            route_distance_from_start_to_end(start_station=start_station, end_station=end_station, routes=self.routes)

        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_route_distance_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'D'
        end_station = ''

        with self.assertRaises(InvalidArgumentError) as context:
            route_distance_from_start_to_end(start_station=start_station, end_station=end_station, routes=self.routes)

        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)
