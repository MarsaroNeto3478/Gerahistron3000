class Ambiente:
    def __init__(self, lugar, epoca, ano, descricao_chave):
        self._lugar = lugar
        self._epoca = epoca
        self._ano = ano
        self._descricao_chave = descricao_chave
        
    
    @property
    def lugar(self):
        return self._lugar
    @property
    def epoca(self):
        return self._epoca
    @property
    def ano(self):
        return self._ano
    @property
    def descricao_chave(self):
        return self._descricao_chave


    def __str__(self):
        return f"Lugar: {self.lugar} | Época: {self.epoca} | Ano: {self.ano} | Descricao Chave: {self.descricao_chave}"

