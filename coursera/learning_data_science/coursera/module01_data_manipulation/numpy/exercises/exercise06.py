"""This archive talks about my sixth exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    # Slicing --> View
    changing_value_to_zero = a[1, :]
    changing_value_to_zero[:] = 0

    print(changing_value_to_zero) # View
    print("=" * 20)

    # Fancy Indexing --> Copy
    changing_value_to_minus_one = a[a > 50]
    changing_value_to_minus_one[:] = -1

    print(changing_value_to_minus_one) # Copy
    print("=" * 20)

    print(a)


if __name__ == "__main__":
    main()
