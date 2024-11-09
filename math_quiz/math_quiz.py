import random

#Generates an random integer for usage in the math quiz
def random_Integer(minValue, maxValue):
    """
    Generate a random integer between minValue and maxValue, inclusive.

    Args:
        minValue (int): The minimum value of the range.
        maxValue (int): The maximum value of the range.

    Returns:
        int: A random integer between minValue and maxValue.
    """
    return random.randint(minValue, maxValue)

#Generates a random arithmetic operation (+,-,*) for usage in the math quiz
def random_Operation():
    """
    Select a random arithmetic operation.

    Returns:
        str: A random arithmetic operation ('+', '-', or '*').
    """
    return random.choice(['+', '-', '*'])

#Performs the calculation for 2 numbers and a specified arithmetic operation
def calculate(firstNumber,secondNumber , operation):
    """
       Calculate the result of an arithmetic operation between two numbers.

       Args:
           firstNumber (int or float): The first number in the operation.
           secondNumber (int or float): The second number in the operation.
           operation (str): The arithmetic operation ('+', '-', or '*').

       Returns:
           tuple: A tuple containing the problem as a string and the answer.
       """
    problem = f"{firstNumber} {operation} {secondNumber}"
    if operation == '+': answer = firstNumber + secondNumber
    elif operation == '-': answer = firstNumber - secondNumber
    else: answer = firstNumber * secondNumber
    return problem, answer

#Prompts the user for math questions and validates correctness of answers
def math_quiz():
    """
    Run a math quiz game that presents users with arithmetic problems to solve.

    The user will be given a series of math questions, and their answers will be evaluated.
    The final score is displayed at the end of the quiz.
    """
    streak= 0
    numberOfQuestions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(numberOfQuestions):
        firstNumber = random_Integer(1, 10); secondNumber = random_Integer(1, 5); operation = random_Operation()

        PROBLEM, ANSWER = calculate(firstNumber, secondNumber, operation)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            streak +=1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {streak}/{numberOfQuestions}")

if __name__ == "__main__":
    math_quiz()
