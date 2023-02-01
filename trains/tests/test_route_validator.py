import unittest

from tests.test_helpers.test_helper import create_graph_route
from trains.exceptions import InvalidRouteError, InvalidArgumentError, NoSuchRouteError
from trains.route_validator import validate_start_and_end_station_exists_in_route


class TestTripDistance(unittest.TestCase):
    routes = []

    def setUp(self) -> None:
        self.routes = create_graph_route()

    def tearDown(self) -> None:
        self.routes = []

    def test_validate_should_raise_no_error_for_valid_inputs(self):
        start_station = 'A'
        end_station = 'C'
        try:
            validate_start_and_end_station_exists_in_route(start_station=start_station,
                                                           end_station=end_station,
                                                           routes=self.routes)
        except InvalidRouteError:
            self.fail()
        except InvalidArgumentError:
            self.fail()
        except NoSuchRouteError:
            self.fail()

    def test_validate_should_raise_invalid_route_if_no_route_is_provided(self):
        start_station = 'A'
        end_station = 'C'

        with self.assertRaises(InvalidRouteError) as context:
            validate_start_and_end_station_exists_in_route(start_station=start_station, end_station=end_station)
        self.assertEqual('Invalid route was informed. Value: None .', context.exception.message)

    def test_validate_should_raise_invalid_argument_if_no_start_station_informed(self):
        start_station = ''
        end_station = 'C'

        with self.assertRaises(InvalidArgumentError) as context:
            validate_start_and_end_station_exists_in_route(start_station=start_station, end_station=end_station,
                                                           routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: start_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_validate_should_raise_invalid_argument_if_no_end_station_informed(self):
        start_station = 'D'
        end_station = ''

        with self.assertRaises(InvalidArgumentError) as context:
            validate_start_and_end_station_exists_in_route(start_station=start_station, end_station=end_station,
                                                           routes=self.routes)
        self.assertEqual('Argument is incorrect. Argument: end_station | Value: Argument is an empty string .',
                         context.exception.message)

    def test_validate_should_raise_no_such_route_if_start_station_does_not_exist_in_route(self):
        start_station = 'X'
        end_station = 'C'

        with self.assertRaises(NoSuchRouteError) as context:
            validate_start_and_end_station_exists_in_route(start_station=start_station, end_station=end_station,
                                                           routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)

    def test_validate_should_raise_no_such_route_if_end_station_does_not_exist_in_route(self):
        start_station = 'E'
        end_station = 'K'

        with self.assertRaises(NoSuchRouteError) as context:
            validate_start_and_end_station_exists_in_route(start_station=start_station, end_station=end_station,
                                                           routes=self.routes)
        self.assertEqual('NO SUCH ROUTE', context.exception.message)
