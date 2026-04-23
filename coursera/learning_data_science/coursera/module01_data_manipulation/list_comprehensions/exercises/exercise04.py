# Dada uma matriz (lista de listas), extraia a diagonal principal usando list comprehension.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

diagonal_numbers_of_matriz = [matriz[i][i] for i in range(3)]
print(diagonal_numbers_of_matriz)