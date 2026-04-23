# Fazer todos as letras iniciais de nomes serem maiúsculas utilizando a função lambda e map().

list_of_names = ["carlos", "pedro", "gustavo", "joão"]

inicial_letter = list(map(lambda name: name.capitalize(), list_of_names))
print(inicial_letter)
print("<< Program Finished >> ")
