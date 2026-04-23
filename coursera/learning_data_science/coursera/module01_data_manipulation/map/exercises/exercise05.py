# Use map() para gerar uma nova lista onde cada valor deve ser transformado em: (valor * 10) + 5

values = [1, 2, 3, 4, 5]

transformed_values = list(map(lambda v: (v * 10) + 5, values))
print(transformed_values)