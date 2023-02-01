import unittest

from trains.data_transformation import create_route_graph


class TestDataTransformation(unittest.TestCase):
    def test_create_graph_representation_from_string(self):
        expected_graph = {'A': ['B_5', 'D_5', 'E_7'],
                          'B': ['C_4'],
                          'C': ['D_8', 'E_2'],
                          'D': ['C_8', 'E_6'],
                          'E': ['B_3']}
        data_string = 'AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7'

        route_graph = create_route_graph(data_string)

        self.assertEqual(expected_graph, route_graph)

    def test_should_raise_value_error_if_data_is_empty(self):
        data_string = ''

        with self.assertRaises(ValueError) as context:
            create_route_graph(data_string)
