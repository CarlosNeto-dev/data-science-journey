"""This archive talks about my third exercise of numpy library!"""
import numpy as np

def array_inspection(array):
    """
    Print structural metadata of a NumPy array.
    :param array: NumPy array to be inspected
    :type array: np.ndarray
    :return: None
    """

    print(array.ndim)
    print(array.shape)
    print(array.dtype)
    print("+=" * 20)


def print_of_arrays(arrays):
    """
    Print the content of a NumPy array.
    :param arrays: Numpy array to be printed
    :return: None
    """

    print(arrays)
    print("=" * 40)


def main():
    """Main program execution"""

    a = np.arange(0, 21, 2)
    b = np.linspace(0, 1, 5)
    c = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    d = np.full((3, 5), 7)

    arrays = [a, b, c, d]

    for array in arrays:
        print_of_arrays(array)
        array_inspection(array)


if __name__ == "__main__":
    main()
