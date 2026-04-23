"""This archive talks about my fifth exercise of numpy library!"""
import numpy as np

def main():
    """The main logical of program"""

    a = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    founding_value_fifteen = a[1, 1]

    print(founding_value_fifteen)
    print("=" * 20)

    first_row_of_array = a[0, :]

    print(first_row_of_array)
    print("=" * 20)

    last_column_of_array = a[:, -1]

    print(last_column_of_array)
    print("=" * 20)

    submatrix_of_array = a[0:2, 0:2]

    print(submatrix_of_array)
    print("=" * 20)


if __name__ == "__main__":
    main()
