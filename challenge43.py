weight = float(input("insert your weight: "))
height = float(input("insert your height: "))

imc = weight / (height ** 2)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <=25:
    print("Peso ideal.")
elif imc > 25 and imc <=30:
    print("sobrepeso")
elif imc > 30 and imc < 40:
    print("Obesidade mórbida")