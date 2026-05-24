from personagem import Personagem
class Antagonista(Personagem):  
    def __init__( self, nome, idade, poder, personalidade, fraqueza, descricao, motivacao):
        super().__init__(nome, idade, poder, personalidade, fraqueza, descricao)  # chama o construtor da classe pai (Personagem), nao obrigando escrever de novo
        self._motivacao = motivacao
    
    @property
    def motivacao(self):
        return self._motivacao

    def __str__(self):#nao precisa aterar pois faz com que passe pelo getter!
        return f"Nome: {self.nome} | Idade: {self.idade} | Poder: {self.poder} | Personalidade: {self.personalidade} | Fraqueza: {self.fraqueza} | Descrição: {self.descricao} | Motivação: {self.motivacao}"