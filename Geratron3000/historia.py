from personagem import Personagem
from antagonista import Antagonista
from ambiente import Ambiente
from narrativa import Narrativa

class Historia:
    def __init__(self, personagem, antagonista, ambiente, narrativa, texto):
        self._personagem = personagem
        self._antagonista = antagonista
        self._ambiente = ambiente
        self._narrativa = narrativa
        self._texto = " "

    @property
    def personagem(self):
        return self._personagem
    @property
    def antagonista(self):
        return self._antagonista
    @property
    def ambiente(self):
        return self._ambiente
    @property
    def narrativa(self):
        return self._narrativa
    @property
    def texto(self):
        return self._texto
    @texto.setter#setter pois o valor será inserido depois da geraçao da história!
    def texto(self, valor):
        self._texto = valor

    def __str__(self):#subsitituição
        return (
        f"{self.personagem}\n"    # chama __str__ do Personagem
        f"{self.antagonista}\n"   # chama __str__ do Antagonista
        f"{self.ambiente}\n"      # chama __str__ do Ambiente
        f"{self.narrativa}"       # chama __str__ da Narrativa
    )


    def Perguntar(self):
        print(f"\nOlá sou {self.personagem.nome} deseja criar uma historia com essas opções?")
        print(self)

        while True:
            resposta = input("\nSe desejar criar a história digite Y, caso queria recomeçar digite N! [Y/N] ").upper()
            if resposta == "Y":
                return True
            elif resposta == "N":
                return False
            else:
                print("Favor colocar um valor desejado [Y/N] ")






