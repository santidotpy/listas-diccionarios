import unittest
from listas_diccionarios import check_occurrences

class Test_Check_Occurrences(unittest.TestCase):
    
    def test_int_list(self):
        given = check_occurrences([1, 2, 3, 1, 2, 3, 4])
        expected = {1: 2, 2: 2, 3: 2, 4: 1}
        self.assertEqual(given, expected)

    def test_int_list_same_value(self):
        given = check_occurrences([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        expected = {1: 10}
        self.assertEqual(given, expected)

    def test_int_list_one_value(self):
        given = check_occurrences([1])
        expected = {1: 1}
        self.assertEqual(given, expected)

    def test_str_list(self):
        given = check_occurrences(['a', 'b', 'c', '1', '2', '3', 'a', '1'])
        expected = {'a': 2, 'b': 1, 'c': 1, '1': 2, '2': 1, '3': 1}
        self.assertEqual(given, expected)

    def test_str_and_int_list(self):
        given = check_occurrences(['a', 'b', 'c', 1, 1, 2])
        expected = {'a': 1, 'b': 1, 'c': 1, 1: 2, 2: 1}
        self.assertEqual(given, expected)

    def test_tuple_str_int_list(self):
        given = check_occurrences([('a', 'b'), 'a', 2, ('c', 3)])
        expected = {('a', 'b'): 1, 'a': 1, 2: 1, ('c', 3): 1}
        self.assertEqual(given, expected)

    def test_not_list(self):
        given = check_occurrences('a')
        self.assertFalse(given)


if __name__ == '__main__':
    unittest.main()
