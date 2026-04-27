"""Unit tests for fibonacci module."""

import unittest
from fibonacci import fibonacci, print_fibonacci, powers_of_two, print_powers_of_two


class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_zero_terms(self):
        """Test Fibonacci with 0 terms."""
        self.assertEqual(fibonacci(0), [])
    
    def test_fibonacci_one_term(self):
        """Test Fibonacci with 1 term."""
        self.assertEqual(fibonacci(1), [0])
    
    def test_fibonacci_two_terms(self):
        """Test Fibonacci with 2 terms."""
        self.assertEqual(fibonacci(2), [0, 1])
    
    def test_fibonacci_five_terms(self):
        """Test Fibonacci with 5 terms."""
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
    
    def test_fibonacci_ten_terms(self):
        """Test Fibonacci with 10 terms."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci(10), expected)
    
    def test_fibonacci_negative(self):
        """Test Fibonacci with negative input."""
        self.assertEqual(fibonacci(-5), [])
    
    def test_print_fibonacci(self):
        """Test that print_fibonacci doesn't raise exceptions."""
        try:
            print_fibonacci(5)
            print_fibonacci(0)
        except Exception as e:
            self.fail(f"print_fibonacci raised an exception: {e}")


class TestPowersOfTwo(unittest.TestCase):
    
    def test_powers_of_two_default_limit(self):
        """Test powers of 2 with default limit (512)."""
        expected = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        self.assertEqual(powers_of_two(), expected)
    
    def test_powers_of_two_custom_limit(self):
        """Test powers of 2 with custom limit."""
        self.assertEqual(powers_of_two(16), [1, 2, 4, 8, 16])
    
    def test_powers_of_two_zero_limit(self):
        """Test powers of 2 with zero limit."""
        self.assertEqual(powers_of_two(0), [])
    
    def test_powers_of_two_one_limit(self):
        """Test powers of 2 with limit of 1."""
        self.assertEqual(powers_of_two(1), [1])
    
    def test_print_powers_of_two(self):
        """Test that print_powers_of_two doesn't raise exceptions."""
        try:
            print_powers_of_two(512)
            print_powers_of_two(0)
        except Exception as e:
            self.fail(f"print_powers_of_two raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
