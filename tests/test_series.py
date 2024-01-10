import unittest
from series import fibonacci_recursive, fibonacci_iterative, lucas, sum_series

class TestSeriesFunctions(unittest.TestCase):

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)

    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(2), 1)
        self.assertEqual(fibonacci_iterative(3), 2)
        self.assertEqual(fibonacci_iterative(4), 3)

    def test_lucas(self):
        self.assertEqual(lucas(0), 2)
        self.assertEqual(lucas(1), 1)
        self.assertEqual(lucas(2), 3)
        self.assertEqual(lucas(3), 4)
        self.assertEqual(lucas(4), 7)

    def test_sum_series(self):
        self.assertEqual(sum_series(0), 0)  # Fibonacci series
        self.assertEqual(sum_series(1), 1)  # Fibonacci series
        self.assertEqual(sum_series(2), 1)  # Fibonacci series
        self.assertEqual(sum_series(3), 2)  # Fibonacci series
        self.assertEqual(sum_series(4), 3)  # Fibonacci series

if __name__ == '__main__':
    unittest.main()