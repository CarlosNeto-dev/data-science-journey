# Use map() para retornar uma lista com todos os nomes em maiúsculas.

names = ["carlos", "joão", "maria"]

uppercase_names = list(map(lambda n: n.upper(), names))
print(uppercase_names)