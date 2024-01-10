def fibonacci_recursive(n):
    """
    Return the nth value in the Fibonacci series using recursion.

    Parameters:
    - n (int): The position of the desired value in the series.

    Returns:
    - int: The nth value in the Fibonacci series.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    """
    Return the nth value in the Fibonacci series using iteration.

    Parameters:
    - n (int): The position of the desired value in the series.

    Returns:
    - int: The nth value in the Fibonacci series.
    """
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b


def lucas(n):
    """
    Return the nth value in the Lucas numbers series using recursion.

    Parameters:
    - n (int): The position of the desired value in the series.

    Returns:
    - int: The nth value in the Lucas numbers series.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, a=0, b=1):
    """
    Return the nth value in a series based on the given optional parameters.

    Parameters:
    - n (int): The position of the desired value in the series.
    - a (int): The first value in the series (default: 0).
    - b (int): The second value in the series (default: 1).

    Returns:
    - int: The nth value in the specified series.
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)