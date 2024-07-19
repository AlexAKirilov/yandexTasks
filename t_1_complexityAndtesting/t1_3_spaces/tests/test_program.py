import unittest
from unittest.mock import patch
from io import StringIO

from t_1_complexityAndtesting.t1_3_spaces import program


class Test_program(unittest.TestCase):

    @patch('sys.stdin', new_callable=StringIO)
    def test_base_example(self, mock_stdin):
        mock_stdin.write('5\n1\n4\n12\n9\n0')
        mock_stdin.seek(0)

        func_response = program.main()

        self.assertEqual(func_response, 8)
