# Fazer uma calculadora que vai fazer a operação de dois parâmetros. Logo, vai somar parâmetroA + parâmetroB e depois multiplicar por dois.
calculator_of_parameters = lambda a, b: (a + b) * 2

try:
    number1 = float(input("Type a number: ").strip())
    number2 = float(input("Type another number: ").strip())
except(ValueError, TypeError):
    print("\033[1;31mError! This value is invalid! Try again.\033[m ")
except(KeyboardInterrupt):
    print("\033[1;31mError! The User dont prefer to type anything!\033[m ")
else:
    final_result = calculator_of_parameters(number1, number2)
    print(f"The final result of ({number1} + {number2}) * 2 is {final_result} ")
finally:
    print("<< Program Finished >> ")