"""This archive talks about my thirteen exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.random.rand(2, 3, 4)
    b = np.random.rand(2, 4, 5)

    print(f"a shape: {a.shape}")
    print("=" * 20)
    print(f"b shape: {b.shape}")
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
