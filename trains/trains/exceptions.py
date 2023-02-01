class InvalidRouteError(Exception):
    """Raised when invalid route is detected."""
    def __init__(self, value):
        super().__init__()
        self.message = f'Invalid route was informed. Value: { value } .'


class InvalidArgumentError(Exception):
    """Raised when invalid Argument is detected."""

    def __init__(self, key, value, expected=''):
        super().__init__()
        expected_message = ''
        if expected:
            expected_message = f' | Expected value: { expected }'
        if value == '':
            value = 'Argument is an empty string'
        self.message = f'Argument is incorrect. Argument: { key } | Value: { value }{ expected_message } .'


class NoSuchRouteError(Exception):
    def __init__(self):
        super().__init__()
        self.message = 'NO SUCH ROUTE'
