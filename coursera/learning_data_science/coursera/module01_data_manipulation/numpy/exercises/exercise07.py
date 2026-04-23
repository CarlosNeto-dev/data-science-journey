"""This archive talks about my ninth exercise of NumPy library."""
import numpy as np

def main():
    """Main program execution."""

    # Example with slicing (creates a view)
    a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    slice_a = a[0:6]   # view
    slice_a[:] = 0    # modifies original array

    print(slice_a)
    print(a)

    print("+=" * 20)

    # Example with fancy indexing (creates a copy)
    b = np.array([0, 1, 2, 3, 4, 5])

    fancy_array = b[[1, 0, 4, 2]]  # copy
    c = fancy_array[:]

    print(fancy_array)
    print(c)


if __name__ == "__main__":
    main()
