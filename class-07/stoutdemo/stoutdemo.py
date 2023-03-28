def greet(name):
    print('Hello ', name)

from unittest.mock import patch

@patch('builtins.print')
def test_greet(mock_print):
    # The actual test
    greet('John')
    mock_print.assert_called_with('Hello ', 'John')
    greet('Eric')
    mock_print.assert_called_with('Hello ', 'Eric')

    # Showing what is in mock
    import sys
    sys.stdout.write(str( mock_print.call_args ) + '\n')
    sys.stdout.write(str( mock_print.call_args_list ) + '\n')

if __name__ == '__main__':
    test_greet()
