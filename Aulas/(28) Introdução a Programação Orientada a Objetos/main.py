'''class Aluno:
     nome = "Fernado"      #Nome é um atributo
     idade = 15            #Atributo
     cpf = "81911749979"   #Atributo
     cgm = "1239940"       #Atributo
     sexo = "Masculino"    #Atributo
     
aluno1 = aluno()
print(aluno1.nome)
print(aluno1.idade)'''

class Aluno:
    
    def __init__(self, nome, idade, curso, nota):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.nota = nota
        
    #Metodo
    def apresentar(self):
        print(f"Ola! Meu nome é {self.nome} tenho {self.idade}")
        
    #Metodo
    def verificarAprovado(self):
        if self.nota > 60:
            print(f"{self.nome} foi aprovado com a nota de {self.nota}")
        else:
            print(f"{self.nome} foi reprovado com nota de {self.nota}")

# instancia
Aluno1 = Aluno("Fernado", 15, "IA", 100)
Aluno2 = Aluno("Veroneze", 15, "DS", 55)
Aluno1.apresentar()
Aluno2.apresentar()
Aluno1.verificarAprovado()
Aluno2.verificarAprovado()