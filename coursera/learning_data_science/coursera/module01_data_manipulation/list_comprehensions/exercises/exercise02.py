# Dada uma lista de palavras, retorne uma nova lista contendo apenas as palavras com mais de 5 caracteres
list_of_words = ["cat", "dog", "elephant", "sun", "sea"]

list_of_words_who_haves_more_than_five_letters = [w for w in list_of_words if len(w) > 5]
print(list_of_words_who_haves_more_than_five_letters)