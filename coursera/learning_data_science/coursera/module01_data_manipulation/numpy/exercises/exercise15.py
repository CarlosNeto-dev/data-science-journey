"""This archive talks about my fifteen exercise of numpy library!"""
import numpy as np

def main():
    """Main program execution"""

    archive_data = np.genfromtxt("exercise_archive", delimiter=",", skip_header=1)

    print(archive_data)
    print("=" * 25)

    # Delimiter Incompatível
    print(np.genfromtxt("exercise_archive", delimiter=";", skip_header=1))
    print("=" * 25)

    # Sem skip_header
    print(np.genfromtxt("exercise_archive", delimiter=","))
    print("=" * 25)


if __name__ == "__main__":
    main()
