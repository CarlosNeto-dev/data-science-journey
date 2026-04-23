# Dada uma lista de números, gere uma nova lista contendo apenas os números pares elevados ao quadrado.

list_of_numbers = [1, 2, 3, 4, 5, 6]

square_numbers = [n * n for n in list_of_numbers if n % 2 == 0]
print(square_numbers)