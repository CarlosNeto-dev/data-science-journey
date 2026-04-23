# Dentro de uma lista de 1 a 10, achar os números pares e ímpares utilizando a função "filter()" e lambda juntos.

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda num: num % 2 == 0, list_of_numbers))
print(even_numbers)

odd_numbers = list(filter(lambda num: num % 2 != 0, list_of_numbers))
print(odd_numbers)

print("<< Program Finished >> ")