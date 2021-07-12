"""
Task about sum and product.

There are two whole numbers:
1 < a,b <100

One scientist("Sum") get provided with sum of numbers,
another  ("Prod") get provided with product of numbers.
Both scientists know that numbers 1 < a,b <100.

Determine the numbers being based on the following dialog:
    Prod: I don't know the numbers;
    Sum: I know it;
    Prod: then I know the numbers;
    Sum: then I know the numbers too.

Solution:
    a + b = Sum
    a * b = Prod
    a = Sum - b
    (Sum - b) * b = Prod
    b^2 - b * Sum + Prod = 0
    The rest is simple quadratic equation.
"""
# Standart library imports
import math
from typing import Tuple

# Thirdparty imports
import click

# in the task there are < sign so I guess these are the min and max values
MIN_NUMBER = 2
MAX_NUMBER = 99


def solve_quadratic_equation(b: int, c: int) -> Tuple[float]:
    """Solve the quadratic equation that we receive in the task solution. Aka a * x ^ 2 + b * x + c = 0.

    Parameters
    ----------
    b : int
        `b` from the quadratic equation.
    c : int
        `c` from the quadratic equation.

    Returns
    -------
    tuple of float
        roots of equation.
    """
    a = 1  # in our case `a` is always = 1

    discriminant = b ** 2 - (4 * c * a)

    return (
        (-b - math.sqrt(discriminant)) / (2 * a),
        (-b + math.sqrt(discriminant)) / (2 * a),
    )


@click.command()
@click.option('--sum', prompt='Enter Sum of numbers', type=int, required=True)
@click.option('--prod', prompt='Enter Product of numbers', type=int, required=True)
def main(sum: int, prod: int) -> Tuple[float]:
    """Find solution to "Task about sum and product".

    Parameters
    ----------
    sum : int
        Provided sum of numbers.
    prod : int
        Provided product of numbers.

    Returns
    -------
    First number : float
    Second number : float

    Raises
    ------
    ValueError
        If the provided values don't match min - max range.
    """
    if sum not in range(MIN_NUMBER * 2, MAX_NUMBER * 2 + 1) or prod not in range(MIN_NUMBER ** 2, MAX_NUMBER ** 2 + 1):
        raise ValueError(f'Numbers should be in range: {MIN_NUMBER} <= a, b <= {MAX_NUMBER}')

    # we need to add minus to sum accroding to solution formula
    possible_second_numbers = solve_quadratic_equation(-sum, prod)

    result = set()

    for number in possible_second_numbers:
        first_number = sum - number
        if number in range(MIN_NUMBER, MAX_NUMBER + 1) and first_number in range(MIN_NUMBER, MAX_NUMBER + 1):
            result.add(tuple(sorted((first_number, number))))

    if not result:
        raise Exception(f'Idk, smth bad happened, {possible_second_numbers = }, {sum = }, {prod = }')

    print(f'The numbers according to your input are: {result}')
    return result


if __name__ == '__main__':
    main()
