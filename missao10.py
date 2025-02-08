# Missão 10: Contando Letras 🔄
nome = str(input("Digite um nome: "))

def contaLetras(nome):
    espacos = nome.replace(" ","")
    quantidade = len(espacos)
    resposta = print(f"O nome {espacos} tem {quantidade} letras")
    return resposta

contaLetras(nome)