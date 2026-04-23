# Fazer o quadrado de um número utilizando a função lambda no Python

try:
    num = float(input("Type a number: ").strip())
    square_number = lambda number: number ** 2
except(ValueError, TypeError, IndexError):
    print("\033[1;31mError! This value is invalid! Try again.\033[m ")
except(KeyboardInterrupt):
    print("\033[1;31mError! The User dont prefer to type anything!\033[m ")
else:
    print(f"The square of {num} is {square_number(num)} ")
finally:
    print("<< Program finished >> ")