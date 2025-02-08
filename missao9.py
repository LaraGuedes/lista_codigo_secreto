# Missão 9: Calculando Dobro de um Número 🛠️
numero = int(input("Informe um número: "))

def dobro(numero):
    dobro = numero *2
    respostar = print("O dobro de ",numero, "é", dobro)
    return respostar

dobro(numero)