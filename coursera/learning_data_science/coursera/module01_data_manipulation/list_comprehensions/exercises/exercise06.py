# Deixe a última letra maiúscula dos nomes de uma lista.
list_of_names = ["Carlos", "Maria", "Pedro", "João", "Alex"]
last_letter = [
    name.lower()[:-1] + name.upper()[-1]
    for name in list_of_names
]
print(last_letter)