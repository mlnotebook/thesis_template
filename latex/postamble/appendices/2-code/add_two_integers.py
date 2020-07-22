""" Example Script for Thesis Template

R. Robinson 2020 https://github.com/mlnotebook
"""

import argparse
import numpy as np


def add_two_integers(num1, num2):
    """ Function to add two integers.
    
    Args:
        num1 (int): an integer to add to num2
        num2 (int): an integer to add to num1
    Returns:
        result (unt): the sum of the two integers
    """
    assert ((type(num1) == int) & (type(num2) == int)), \
        f"num1 and num2 should both be integers. Got {type(int1)} and {type(int2)}."

    result = int(num1 + num2)

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Add two integers.')
    parser.add_argument('num1', type=int, help='first integer to add')
    parser.add_argument('num2', type=int, help='second integer to add')

    args = parser.parse_args()

    result = add_two_integers(args.num1, args.num2)

    print(f"{args.num1} + {args.num2} = {result}")
