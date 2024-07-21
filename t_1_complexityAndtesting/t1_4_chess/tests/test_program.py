import unittest
from unittest.mock import patch
from io import StringIO

from t_1_complexityAndtesting.t1_4_chess import program


class TestProgram(unittest.TestCase):

    @patch('sys.stdin', new_callable=StringIO)
    def test_base_example_1(self, mock_stdin):
        mock_stdin.write('********\n********\n*R******\n********\n********\n********\n********\n********')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 49)

    @patch('sys.stdin', new_callable=StringIO)
    def test_base_example_2(self, mock_stdin):
        mock_stdin.write('********\n********\n******B*\n********\n********\n********\n********\n********')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 54)

    @patch('sys.stdin', new_callable=StringIO)
    def test_base_example_3(self, mock_stdin):
        mock_stdin.write('********\n*R******\n********\n*****B**\n********\n********\n********\n********')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 40)

    @patch('sys.stdin', new_callable=StringIO)
    def test_many_figures(self, mock_stdin):
        mock_stdin.write('*******R\n********\n**B*****\n********\n****B***\n**R*****\n********\n*******R')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 22)

    @patch('sys.stdin', new_callable=StringIO)
    def test_edge_Bs(self, mock_stdin):
        mock_stdin.write('B******B\n********\n********\n********\n********\n********\n********\nB******B')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 48)

    @patch('sys.stdin', new_callable=StringIO)
    def test_edge_Rs(self, mock_stdin):
        mock_stdin.write('R******R\n********\n********\n********\n********\n********\n********\nR******R')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 36)