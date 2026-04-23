# Dada uma lista de números, crie uma nova lista onde:
# - números positivos aparecem como "positivo"
# - números negativos aparecem como "negativo"
# - zeros aparecem como "zero"

list_of_values = [-2, 0, 5, -7, 3]

filter_of_values = ["positive" if v > 0 else "negative" if v < 0 else "zero" for v in list_of_values]
print(filter_of_values)