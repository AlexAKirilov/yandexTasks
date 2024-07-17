import unittest
from unittest.mock import patch
from io import StringIO
from t_1_complexityAndtesting.t1_1_trees_coloring import program


class TestProgram(unittest.TestCase):
    @patch('sys.stdin', new_callable=StringIO)
    def test_correct_process_empty_input(self, mock_stdin):
        mock_stdin.write('')
        mock_stdin.seek(0)  # Сбросить курсор в начало строки

        response = program.main()

        self.assertEqual(response, 0)

    @patch('sys.stdin', new_callable=StringIO)
    def test_standart_edge_intersection(self, mock_stdin):
        mock_stdin.write('0 7\n12 5')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 25)

    @patch('sys.stdin', new_callable=StringIO)
    def test_neg_standart_edge_intersection(self, mock_stdin):
        mock_stdin.write('-0 7\n-12 5')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 25)

    @patch('sys.stdin', new_callable=StringIO)
    def test_edge_intersection(self, mock_stdin):
        mock_stdin.write('0 7\n11 5')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 24)

    @patch('sys.stdin', new_callable=StringIO)
    def test_edge_intersection_reverse(self, mock_stdin):
        mock_stdin.write('0 7\n11 5')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 24)

    @patch('sys.stdin', new_callable=StringIO)
    def test_one_segment_in_another(self, mock_stdin):
        mock_stdin.write('0 7\n0 5')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 15)

    @patch('sys.stdin', new_callable=StringIO)
    def test_one_segment_in_another_reverse(self, mock_stdin):
        mock_stdin.write('0 5\n0 7')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 15)

    @patch('sys.stdin', new_callable=StringIO)
    def test_one_painter(self, mock_stdin):
        mock_stdin.write('0 8')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 17)

    @patch('sys.stdin', new_callable=StringIO)
    def test_one_painter_negative(self, mock_stdin):
        mock_stdin.write('-6 8')
        mock_stdin.seek(0)

        response = program.main()

        self.assertEqual(response, 17)


if __name__ == '__main__':
    unittest.main()
