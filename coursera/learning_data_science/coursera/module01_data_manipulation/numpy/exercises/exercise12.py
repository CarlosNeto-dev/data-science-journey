"""This archive talks about my twelfth exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    b = np.array([1, 0, 1])

    print(f"a shape: {a.shape}")
    print("=" * 20)
    print(f"b shape: {b.shape}") # Para o Dot Product, entenderá (1, 3)
    print("=" * 20)

    # Dot Product Compatível
    print(a @ b)

    print("=" * 20)

    # Dot Product Incompatível
    try:
        print(b @ a)

    except ValueError as error:
        print(f"Dot Product Incompatibility: {error}")


if __name__ == "__main__":
    main()
