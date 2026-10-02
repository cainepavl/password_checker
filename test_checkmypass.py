import hashlib
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
        # The mocked API response must contain the real SHA-1 suffix of
        # 'password' for get_password_leaks_count() to find a match --
        # arbitrary placeholder hashes never match and silently returned 0.
        sha1 = hashlib.sha1('password'.encode('utf-8')).hexdigest().upper()
        tail = sha1[5:]
        mock_request_api_data.return_value = MagicMock(text=f'{tail}:5\nHASH2:10\n')

        count = checkmypass.pwned_api_check('password')
        self.assertEqual(count, '5')

    @patch('checkmypass.getpass.getpass')
    @patch('checkmypass.clear_screen')
    @patch('checkmypass.pwned_api_check')
    def test_main_found_password(self, mock_pwned_api_check, mock_clear_screen, mock_getpass):
        # First prompt returns the password under test, second returns ''
        # to end the input loop (same convention the real prompt uses).
        mock_getpass.side_effect = ['password123', '']
        mock_pwned_api_check.return_value = '5'
        with patch('builtins.print') as mock_print:
            checkmypass.main()
            mock_print.assert_any_call(
                f'{checkmypass.Fore.RED}Found in 5 breach(es)... You should change it!{checkmypass.Style.RESET_ALL}')

    @patch('checkmypass.getpass.getpass')
    @patch('checkmypass.clear_screen')
    @patch('checkmypass.pwned_api_check')
    def test_main_good_password(self, mock_pwned_api_check, mock_clear_screen, mock_getpass):
        mock_getpass.side_effect = ['goodpassword', '']
        mock_pwned_api_check.return_value = 0
        with patch('builtins.print') as mock_print:
            checkmypass.main()
            mock_print.assert_any_call(
                f'{checkmypass.Fore.GREEN}Not found in any known breach -- good to go!{checkmypass.Style.RESET_ALL}')


if __name__ == '__main__':
    unittest.main()