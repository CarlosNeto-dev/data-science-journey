"""This archive talks about my first exercise of numpy library!"""
import numpy as np

def array_inspection(array):
    """
    Print the structural metadata of a NumPy array.
    :param array: Numpy array to be printed
    :return: None
    """

    print(array.ndim)
    print(array.shape)
    print(array.dtype)
    print("=" * 20)


def main():
    """The main logical of program."""

    a = np.arange(0, 10)
    b = np.ones((3, 3))
    c = np.zeros((2, 2, 3))

    arrays = [a, b, c]

    for array in arrays:
        array_inspection(array)


if __name__ == "__main__":
    main()
