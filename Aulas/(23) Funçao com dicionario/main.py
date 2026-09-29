personagens = []

def criar_personagens():
    nome = input("Digite o nome do personagem: ")
    classe = input("Digite  a classe do seu personagem: ")
    nivel = int(input("Digite o nivel do seu personagem: "))
    
    personagem = {
        "nome": nome,
        "classe": classe,
        "nivel": nivel
    }
    personagem.apend(personagem)

    #print("personagem criado")'
    #print("nome: ", personagem["classe"])
    #print("nivel: ", personagem["nivel"])


quantidade = int(input("quantos personagens deseja criar?"))
for i in range(quantidade):
    print(f"criar personagem {i + '}")
    criar_personagens()