"""This archive talks about my fourteen exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    a = np.random.rand(12, )

    # Reshapes Compatíveis
    print(a.reshape(3, 4))
    print("=" * 60)
    print(a.reshape(2, 2, 3))
    print("=" * 60)

    # Reshape Incompatível
    try:
        print(a.reshape(4, 4))

    except ValueError as error:
        print(f"Incompatible reshape: {error}")


if __name__ == "__main__":
    main()
