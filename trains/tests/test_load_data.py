import unittest
from unittest.mock import patch

from trains.load_data import load_data_from_user_interface


class TestLoadData(unittest.TestCase):
    @patch('builtins.input', return_value='AB5  ,BC4   ,CD8   ,DC8,  DE6,  AD5,  CE2,  EB3,  AE7')
    def test_load_data_returns_data_without_white_spaces(self, input):
        expected_loaded_data = 'AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7'
        loaded_data = load_data_from_user_interface()
        self.assertEqual(expected_loaded_data, loaded_data)

    @patch('builtins.input', return_value='')
    def test_should_return_empty_if_nothing_no_data_is_send(self, input):
        expected_loaded_data = ''
        loaded_data = load_data_from_user_interface()
        self.assertEqual(expected_loaded_data, loaded_data)
