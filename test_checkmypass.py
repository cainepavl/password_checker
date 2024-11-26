import unittest
from unittest.mock import patch, MagicMock
import checkmypass


class TestCheckMyPass(unittest.TestCase):

    @patch('checkmypass.requests.get')
    def test_request_api_data_success(self, mock_get):
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = checkmypass.request_api_data('abcde')
        self.assertEqual(result, mock_response)

    @patch('checkmypass.requests.get')
    def test_request_api_data_failure(self, mock_get):
        # Mock a failed response
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(RuntimeError) as context:
            checkmypass.request_api_data('abcde')
        self.assertIn('Error fetching', str(context.exception))

    def test_get_password_leaks_count_found(self):
        # Mocked response data
        mock_response = MagicMock()
        mock_response.text = 'HASH1:5\nHASH2:10\nHASH3:0\n'

        count = checkmypass.get_password_leaks_count(mock_response, 'HASH1')
        self.assertEqual(count, '5')

    def test_get_password_leaks_count_not_found(self):
        mock_response = MagicMock()
        mock_response.text = 'HASH1:5\nHASH2:10\nHASH3:0\n'

        count = checkmypass.get_password_leaks_count(mock_response, 'HASH4')
        self.assertEqual(count, 0)

    @patch('checkmypass.request_api_data')
    def test_pwned_api_check(self, mock_request_api_data):
        # Mock the request_api_data function
        mock_request_api_data.return_value = MagicMock(text='HASH1:5\nHASH2:10\n')

        count = checkmypass.pwned_api_check('password')
        self.assertEqual(count, '5')

    @patch('checkmypass.clear_screen')
    @patch('checkmypass.pwned_api_check')
    def test_main_found_password(self, mock_pwned_api_check, mock_clear_screen):
        mock_pwned_api_check.return_value = '5'
        with patch('builtins.print') as mock_print:
            checkmypass.main(['password123'])
            mock_print.assert_called_with(
                f'{checkmypass.Fore.RED}password123 was found 5 times...\nYou should change it!{checkmypass.Style.RESET_ALL}')

    @patch('checkmypass.clear_screen')
    @patch('checkmypass.pwned_api_check')
    def test_main_good_password(self, mock_pwned_api_check, mock_clear_screen):
        mock_pwned_api_check.return_value = 0
        with patch('builtins.print') as mock_print:
            checkmypass.main(['goodpassword'])
            mock_print.assert_called_with(
                f'{checkmypass.Fore.GREEN}goodpassword is good to go!{checkmypass.Style.RESET_ALL}')


if __name__ == '__main__':
    unittest.main()