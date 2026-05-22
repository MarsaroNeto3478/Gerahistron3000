from Personagem import Personagem
class Antagonista(Personagem):  
    def __init__( self, nome, idade, poder, personalidade, fraqueza, descricao, motivacao):
        super().__init__(nome, idade, poder, personalidade, fraqueza, descricao)  # chama o construtor da classe pai (Personagem), nao obrigando escrever de novo
        self.motivacao = motivacao



    def validar_poder(self, Personagem):
        if self.poder == Personagem.poder:
            raise ValueError("Que sem graça! O antagonsita não pode ter o mesmo poder que o personagem principal!")   
        else:
            return self.poder  