#(19) Estrutura de dados compostas 2
#Lista de Lista

jogos = [
    ["CS2", "Roblox", "RDR2"], #Jogos de pc
    ["AstroBot", "God of War", "The last of Us"], #Jogos de PS4
    ["Halo", "Forza Horizon", "Gears of War"] #Jogos de Xbox
]
print(len(jogos)) # Quantidade de listas dentro da listas

print("jogos por plataforma:\n")
print("jogos de pc: ")
for JG in jogos[0]:
 print(JG)
 
 
print("\njogos de PS4: ")
for JG in jogos[1]:
 print(JG)
 
 
print("\njogos de Xbox: ")
for JG in jogos[2]:
 print(JG)