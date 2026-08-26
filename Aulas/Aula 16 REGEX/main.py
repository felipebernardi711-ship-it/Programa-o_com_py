import re
codigo = input("Digite um codigo!")
if re.fullmatch(r"\d{4}", codigo):
    print("codigo valido!")
else:
    print("codigo invalido!")
    