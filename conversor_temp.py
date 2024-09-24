#temperaturas
celsius = 0
fahrenheit = 32
kelvin = float(273.15)

def converter(conversor, temperatura):
  if conversor == 1:
    return (temperatura * 9/5) + fahrenheit

  elif conversor == 2:
    return temperatura + kelvin

  elif conversor == 3:
    return (temperatura - fahrenheit) * 5/9

  elif conversor == 4:
    return (temperatura - fahrenheit) * 5/9 + kelvin

  elif conversor == 5:
    return temperatura - kelvin

  elif conversor == 6:
    return (temperatura - kelvin) * 9/5 + fahrenheit

temperatura = float(input("Digite uma temperatura: "))
conversor = int(input("Para qual temperatura você quer converter?:\n1-Celsius para Fahrenheit\n2-Celsius para Kelvin\n3-Fahrenheit para Celsius\n4-Fahrenheit para Kelvin\n5-Kelvin para Celsius\n6-Kelvin para Fahrenheit\nDigite um número: "))
resultado = converter(conversor, temperatura)
print(f'Resultado: {resultado:.2f}')

