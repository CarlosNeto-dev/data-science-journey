# Use map() para gerar uma nova lista contendo o quadrado de cada número.

numbers = [2, 4, 6, 8]

square_numbers = list(map(lambda v: v ** 2, numbers))
print(square_numbers)
