import unittest
from math_quiz import generate_random_number
from math_quiz import generate_random_arithmetic_operator
from math_quiz import generate_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_arithmetic_operator(self):
        """
        Test if random arithmetic operators generated are valid.
        """
        for _ in range(1000):
            rand_op = generate_random_arithmetic_operator()
            self.assertTrue(rand_op in ['+', '-', '*'])

    def test_generate_math_problem(self):
            """
            Test if math problems and answers generated are correct.
            """
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (-5, 2, '+', '-5 + 2', -3),
                (-5, 2, '-', '-5 - 2', -7),
                (-5, 2, '*', '-5 * 2', -10),
                (5, -2, '+', '5 + -2', 3),
                (5, -2, '-', '5 - -2', 7),
                (5, -2, '*', '5 * -2', -10),
                (-5, -2, '+', '-5 + -2', -7),
                (-5, -2, '-', '-5 - -2', -3),
                (-5, -2, '*', '-5 * -2', 10),
            ]

            for first_operand, second_operand, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_math_problem(first_operand, second_operand, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
