def calcular_imc(peso, altura):
    alturaMetros = altura / 100
    imc = peso / (alturaMetros ** 2)
    return imc

def resultado_imc(imc):
    if imc < 16:
        return "Magreza Grave"
    elif 16 <= imc < 17:
        return "Magreza Moderada"
    elif 17 <= imc < 18.5:
        return "Magreza leve"
    elif 18.5 <= imc < 25:
        return "Saudavel"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade Grau III"

peso = float(input("Digite o peso em Kg: "))
altura = float(input("Digite a sua altura em centimetros: "))  # Mude para centimetros

imc = calcular_imc(peso, altura)
classificacao = resultado_imc(imc)
print("Seu IMC eh: {:.2f}".format(imc))
print("Sua Classificacao eh: {}".format(classificacao))
