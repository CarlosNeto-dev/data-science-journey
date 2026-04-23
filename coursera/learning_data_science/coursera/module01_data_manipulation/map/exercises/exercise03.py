# Use map() para retornar uma lista contendo o tamanho de cada palavra.

words = ["python", "map", "lambda", "exercise"]

len_of_words = list(map(lambda w: len(w), words))
print(len_of_words)