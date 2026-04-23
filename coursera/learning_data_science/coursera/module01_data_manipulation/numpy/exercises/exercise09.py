"""This archive talks about my ninth exercise of numpy library!"""
import numpy as np

def basic_array_operations(array_one, array_two):
    """
    Prints basic element-wise arithmetic operations between two NumPy arrays.

    :param array_one: First Numpy array to be used
    :param array_two: Second Numpy array to be used
    :return: None
    """

    print(f"Sum operation: {array_one + array_two}")
    print("=" * 40)

    print(f"Subtraction operation: {array_one - array_two}")
    print("=" * 40)

    print(f"Multiplication operation: {array_one * array_two}")
    print("=" * 40)

    print(f"Division operation: {array_one / array_two}")
    print("=" * 40)

    print(f"Exponentiation operation: {array_one ** array_two}")
    print("=" * 40)


def main():
    """Main program execution"""

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    basic_array_operations(a, b)


if __name__ == "__main__":
    main()
