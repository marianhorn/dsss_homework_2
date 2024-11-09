import unittest
from math_quiz import random_Integer, random_Operation, calculate


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_Integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operation(self):
        for _ in range(1000):
            operation = random_Operation()
            self.assertIn(operation, ['+', '-', '*'], "The random operation should be one of '+', '-', or '*'.")

    def test_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 5, '-', '10 - 5', 5),
            (3, 4, '*', '3 * 4', 12),
            (0, 5, '+', '0 + 5', 5),
            (7, 0, '-', '7 - 0', 7),
            (6, 3, '*', '6 * 3', 18)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem,
                             f"Expected problem string '{expected_problem}', but got '{problem}'.")
            self.assertEqual(answer, expected_answer, f"Expected answer '{expected_answer}', but got '{answer}'.")


if __name__ == "__main__":
    unittest.main()