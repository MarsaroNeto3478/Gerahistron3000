class Personagem:
    def __init__(self, nome, idade, poder, personalidade, fraqueza, descricao):#innit é o constutor do phyton
        self.nome = nome#self seria o this do java no phyton, ele cria o atributo ja atribuindo ele
        self.idade = idade
        self.poder = poder
        self.personalidade = personalidade
        self.fraqueza = fraqueza
        self.descricao = descricao


    def verifica_idade(self, idade):
        if idade <= 0:
            raise ValueError("Idade precisa ser maior que 0!")
        else: 
            return idade
        

