"""This archive talks about my eleventh exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.ones((4, 3))
    b = np.array([1, 2, 3])
    c = np.array([1, 2])

    print(f"a shape: {a.shape}")
    print("=" * 20)
    print(f"b shape: {b.shape}")
    print("=" * 20)
    print(f"c shape: {c.shape}")
    print("=" * 20)

    # Broadcasting Compatível
    print(a + b)

    print("=" * 20)

    # Broadcasting Incompatível
    try:
        print(a + c)

    except ValueError as error:
        print(f"Broadcasting Error: {error}")


if __name__ == "__main__":
    main()
