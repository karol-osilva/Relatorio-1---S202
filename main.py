class Animal:
    def __init__(self,nome,idade,especie,cor,som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print("Som do Animal: ", self.som)

    def mudar_cor(self,nova_cor):
        self.cor = nova_cor

class Elefante(Animal):
    def __init__(self,nome,idade,especie,cor,som,tamanho):
        super().__init__(nome,idade,especie,cor,som)
        self.tamanho = tamanho

    def trombar(self):
        print(self.nome + " faz " + self.som + " com sua tromba")

    def mudar_tamanho(self,novo_tamanho):
        self.tamanho = novo_tamanho


nome = input("digite o nome do elefante: ")
idade = input("digite a idade do elefante: ")
especie = input("digite a espécie do elefante: ")
cor = input("digite a cor do elefante: ")
som = input("digite o som do elefante: ")
tamanho = input("digite a tamanho do elefante: ")

elefante1 = Elefante(nome,idade,especie,cor,som,tamanho)

if elefante1.especie == "Africano":
    if int(elefante1.idade) < 10:
        elefante1.mudar_tamanho("pequeno")
        elefante1.som = "Paaah"
    else:
        elefante1.mudar_tamanho("grande")
        elefante1.som = "PAHHHHHHH"


elefante1.trombar()
print(elefante1.nome + " esta " + elefante1.tamanho)
