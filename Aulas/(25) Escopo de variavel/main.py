
#def cadastrar_usuario(nome, idade, cidade="Não informado"):
#    print(f"Cadastro: {nome}, {idade}, {cidade}")

#cadastrar_usuario(idade = 30, cidade = "SJS", nome = "Carlos")

def mostar_nome():
    nome = "Joao"
    return nome
    
print(mostar_nome())

numero = 10
def calculo():
    global numero
    numero = 20
calculo()
print(numero)