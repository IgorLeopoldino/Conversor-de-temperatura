#temperaturas
celsius = 0
fahrenheit = 32
kelvin = float(273.15)

#pergunta qual a temperatura
temperatura = float(input("Digite uma temperatura: "))

#Celsius para Fahrenheit
celsius_fahrenheit = (temperatura * 9/5) + fahrenheit

#Celsius para Kelvin
celsius_kelvin = temperatura + kelvin

#Fahrenheit para Celsius
fahrenheit_celsius = (temperatura - fahrenheit) * 5/9

#Fahrenheit para Kelvin
fahrenheit_kelvin = (temperatura - fahrenheit) * 5/9 + kelvin

#Kelvin para Celsius
kelvin_celsius = temperatura - kelvin

#Kelvin para Fahrenheit
kelvin_fahrenheit = (temperatura - kelvin) * 9/5 + fahrenheit

conversor = int(input("Para qual temperatura você quer converter?:\n1-Celsius para Fahrenheit\n2-Celsius para Kelvin\n3-Fahrenheit para Celsius\n4-Fahrenheit para Kelvin\n5-Kelvin para Celsius\n6-Kelvin para Fahrenheit\nDigite um número: "))

if conversor == 1:
  print(celsius_fahrenheit)

elif conversor == 2:
  print(celsius_kelvin)

elif conversor == 3:
  print(f'{fahrenheit_celsius:.2f}')

elif conversor == 4:
  print(f'{fahrenheit_kelvin:.2f}')

elif conversor == 5:
  print(f'{kelvin_celsius:.2f}')

elif conversor == 6:
  print(f'{kelvin_fahrenheit:.2f}')