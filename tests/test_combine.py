from src.utils import *


class TestCombineFunction:

    def test_combine_1(self):
        """ Testing with equal length list. """
        assert combine([1, 55, 0, 'a'], [5, 10, 3, 4]) == [1, 5, 55, 10, 0, 3, 'a', 4]

    def test_combine_2(self):
        """ Testing with first list has length more than the second list. """
        assert combine([1, 55, 0, 'a'], [5, 10, 3]) == [1, 5, 55, 10, 0, 3, 'a']

    def test_combine_3(self):
        """ Testing with second list has length more than the first list. """
        assert combine([1, 55, 0], [5, 10, 3, 4]) == [1, 5, 55, 10, 0, 3, 4]

    def test_combine_4(self):
        """ Testing with empty first list. """
        assert combine([], [5, 10, 3, 4]) == [5, 10, 3, 4]

    def test_combine_5(self):
        """ Testing with empty first and second list. """
        assert combine([], []) == []

    def test_combine_6(self):
        """ Testing with complicated first list. """
        assert combine([[1, 2, 3], 'a', {'first': 1}], [1, 2, 3]) == [[1, 2, 3], 1, 'a', 2, {'first': 1}, 3]
