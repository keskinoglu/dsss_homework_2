import random


def generate_random_number(min, max):
    """
    Generate a random integer from a given range.

    Args:
        min (int): The lower bound of the range.
        max (int): The upper bound of the range.

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(min, max)


def generate_random_arithmetic_operator():
    """
    Generate a random arithmetic operator from the following list: +, -, *.

    Returns:
        str: A random operator ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])


def generate_math_problem(first_operand, second_operand, operator):
    """
    Generate a math problem and calculate the answer.

    Args:
        first_operand (int): The first operand in the problem.
        second_operand (int): The second operand in the problem.
        operator (str): The operator in the problem.

    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    problem = f"{first_operand} {operator} {second_operand}"

    if operator == '+': answer = first_operand + second_operand
    elif operator == '-': answer = first_operand - second_operand
    else: answer = first_operand * second_operand

    return problem, answer

def math_quiz():
    """
    Run a math quiz game.

    The game generates a series of math problems and prompts the user for their answers.
    It keeps track of the user's score and prints it at the end.

    Returns:
        None
    """
    score = 0
    number_of_questions = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(number_of_questions):
        first_operand = generate_random_number(1, 10)
        second_operand = generate_random_number(1, 5)
        operator = generate_random_arithmetic_operator()

        problem, answer = generate_math_problem(first_operand, second_operand, operator)

        print(f"\nQuestion: {problem}")

        # Prompt the user for their answer.
        user_answer = input("Your answer: ")

        # Check if the user entered a valid integer.
        while not user_answer.isdigit():
            print("Please enter a valid integer.")
            user_answer = input("Your answer: ")

        # Convert the user's answer to an integer.
        user_answer = int(user_answer)

        if user_answer == answer:
            print("Correct! You earned a point.")

            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{number_of_questions}")
    
def main():
    math_quiz()

if __name__ == "__main__":
    math_quiz()
