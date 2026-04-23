"""This archive talks about my eighth exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.array([10, 15, 20, 25, 30, 35])

    # Boolean Mask --> Copy
    even_values = a[a % 2 == 0]

    print(even_values) # Copy
    print("=" * 20)

    filtered_values = a[a > 25]
    filtered_values[:] = 100

    print(filtered_values) # Copy
    print("=" * 20)

    # Fancy Indexing --> Copy
    chosen_numbers = a[[0, 2, 4]]

    print(chosen_numbers) # Copy
    print("=" * 20)

    print(a)


if __name__ == "__main__":
    main()
