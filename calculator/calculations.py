"""Provide several math calculations.

This module allows calculations to be made.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(6, 9)
    15.0
    >>> calculations.multiply(6.0, 8.0)
    48.0

The module contains the following functions:

- `add(a, b)` - Add two numbers.
- `subtract(a, b)` - Subtract two numbers.
- `multiply(a, b)` - Multiply two numbers.
- `divide(a, b)` - Divide two numbers.
"""

def add(a: float | int, b: float | int) -> float:
    """Add two numbers.

    Examples:
        >>> add(5.0, 7.0)
        12.0
        >>> add(5, 7)
        12.0

    Args:
        a: The first addend.
        b: The second addend.
    Returns:
        A number representing the sum of a and b.
    """
    return float(a) + float(b)


def subtract(a: float | int, b: float | int) -> float:
    """Subtract two numbers.

    Examples:
        >>> subtract(5.0, 7.0)
        -2.0
        >>> subtract(5, 7)
        -2.0

    Args:
        a: The first number.
        b: The second number.
    Returns:
        A number representing the difference of a and b.
    """
    return float(a) - float(b)


def multiply(a: float | int, b: float | int) -> float:
    """Multiply two numbers.

    Examples:
        >>> multiply(5.0, 7.0)
        35.0
        >>> multiply(5, 7)
        35.0

    Args:
        a: The first number.
        b: The second number.
    Returns:
        A number representing the product of a and b.
    """
    return float(a) * float(b)


def divide(a: float | int, b: float | int | None = None) -> float:
    """Divide two numbers.

    Examples:
        >>> divide(7.0, 2.0)
        3.5
        >>> divide(7, 2)
        3.5

    Args:
        a: The first number.
        b: The second number.
    Returns:
        A number representing the ratio of `a` and `b`.
    Raises:
        ZeroDivisionError: An error occurs when the divisor `b` is 0.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")

    return float(a) / float(b)
