"""This archive talks about my tenth exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.ones((3, 3))
    b = np.array([1, 2, 3])

    print(f"a shape: {a.shape}")
    print(f"b shape: {b.shape}") # Entenderá (1, 3) para o broadcasting.

    print("=" * 20)

    print(a + b)


if __name__ == "__main__":
    main()
