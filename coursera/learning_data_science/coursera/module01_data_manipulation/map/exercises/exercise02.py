# Use map() para converter cada temperatura de Celsius para Fahrenheit usando a fórmula: F = C * 1.8 + 32

temperatures = [0, 20, 30, 40]

fahrenheit_temperature = list(map(lambda c: c * 1.8 + 32, temperatures))
print(fahrenheit_temperature)