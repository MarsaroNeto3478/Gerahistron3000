class Personagem:
    def __init__(self, nome, idade, poder, personalidade, fraqueza, descricao):#innit é o constutor do phyton
        self._nome = nome#self seria o this do java no phyton, ele cria o atributo ja atribuindo ele
        self._idade = idade
        self._poder = poder
        self._personalidade = personalidade
        self._fraqueza = fraqueza
        self._descricao = descricao

    #getters
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
    @property
    def poder(self):
        return self._poder
    @property
    def personalidade(self):
        return self._personalidade
    @property
    def fraqueza(self):
        return self._fraqueza
    @property
    def descricao(self):
        return self._descricao


    def __str__(self):#substituição e não precisa aterar (self._...) pois faz com que passe pelo getter!
        return f"Nome: {self.nome} | Idade: {self.idade} | Poder: {self.poder} | Personalidade: {self.personalidade} | Fraqueza: {self.fraqueza} | Descrição: {self.descricao}"
        

    def __str__(self):#substituição e não precisa aterar (self._...) pois faz com que passe pelo getter!
        return f"Nome: {self.nome} | Idade: {self.idade} | Poder: {self.poder} | Personalidade: {self.personalidade} | Fraqueza: {self.fraqueza} | Descrição: {self.descricao}"
    
    @staticmethod #Pode ser usado fora da classe, mas faz mais sentido usar nela
    def verifica_idade(idade):
        if idade <= 0:
            raise ValueError("Idade precisa ser maior que 0!")
        else: 
            return idade
        