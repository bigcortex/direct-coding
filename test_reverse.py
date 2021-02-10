import unittest
from reverse import reverse_list


class TestReverse(unittest.TestCase):

    def test_reverse(self):

        my_list = [1, 2, 3, 4, 5]

        assert reverse_list(my_list) == [5, 4, 3, 2, 1]


if __name__ == '__main__':
    unittest.main()

