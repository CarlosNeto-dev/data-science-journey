# Dada uma lista contendo outras listas dentro, transforme tudo em uma única lista.

list_of_lists = [[1, 2], [3, 4, 5], [6]]

unique_list = [item for sublist in list_of_lists for item in sublist]
print(unique_list)

