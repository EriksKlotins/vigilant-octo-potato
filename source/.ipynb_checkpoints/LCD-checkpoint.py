def LCD(num1, num2):
    """
    Calculate the largest common divisor (LCD) of two numbers.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    int: The largest common divisor of num1 and num2.
    """
    while num2:
        num1, num2 = num2, num1 % num2
    return num1