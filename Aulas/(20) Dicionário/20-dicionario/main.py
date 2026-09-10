# Lista de dicionario ou dict

personagens = [
    {"nome": "BOB", "idade": 96},
    {"nome": "Thanos", "idade": 999}
]

# print(personagens[0]["nome"])
# print(personagens[1]["nome"])
for personagem in personagens:
    print("nome: ", personagem["nome"])
    print("idade: ", personagem["idade"])
    print("----------------")