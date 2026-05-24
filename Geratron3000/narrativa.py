class Narrativa:
    def __init__(self, heroi, genero, duracao, final):
        self._heroi = heroi
        self._genero = genero
        self._duracao = duracao
        self._final = final

    @property
    def heroi(self):
        return self._heroi
    @property
    def genero(self):
        return self._genero
    @property
    def duracao(self):
        return self._duracao
    @property
    def final(self):
        return self._final


    def __str__(self):
        return f"Herói: {self.heroi} | Gênero: {self.genero} | Duração: {self.duracao} | Final: {self.final}"