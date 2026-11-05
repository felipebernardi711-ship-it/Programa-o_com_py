#assert

#print("inicio")
#assert 1 < 0, "O deve ser menor do que 1"
#print("Fim")

try:
    idade = int(input("Digite sua idade: "))
except:
    print("Digite somente numeros inteiros: ")
    
try:
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite um numero"))
    resutado = n1/n2
    print("O resultado é:", resultado)
except ZalueErro:
    print("Digite somente numeros inteiros")
except ZeroDivisionErro:
    print("Nao é possivel dividir por zero")
    