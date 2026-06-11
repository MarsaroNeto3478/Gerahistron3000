# GIRAHISTRON 3000
## CRIADORES: Alberto Luiz Marsaro Neto (188388) e Wesley Triches (210057) - Alunos da UPF

## O  QUE É?
É um projeto para a matéria de Programação Orientada a Objetos (POO) do Terceiro semestre do curso de Ciencia da Computação UPF.
Problema: O bloqueio de criatividade na hora de escrita de uma história.
O projeto consiste em um programa que gera um prompt para o Groq usando uma API, que retorna uma história de acorodo com as especificações do usuário.


## COMO USAR???

Primeiramente, você precisará abrir um novo terminal, e escrever "pip install -r requirements.txt" que irá instalar algumas bibliotecas que usamos (dotenv, groq).

Após isso, vá em main e execute! Siga as instruções do programa criando um personagem, antagonista, ambiente, narrativa e após isso gere uma história!

## EXEMPLO DE INPUTS:
```
Personagem:
Nome: Kael
Idade: 23
Poder: Controle do tempo
Personalidade: Impulsivo e determinado
Fraqueza: Não consegue controlar emoções sob pressão
Descrição: Um jovem rebelde que descobriu seus poderes por acidente
Antagonista:
Nome: Vordak
Idade: 45
Poder: Manipulação da sombra
Personalidade: Frio e calculista
Fraqueza: Arrogância excessiva
Descrição: Um ex-cientista corrompido pela busca do poder absoluto
Motivação: Reescrever a história apagando os fracos
Ambiente:
Lugar: Cidade subterrânea abandonada
Época: Cyberpunk
Ano: 2187
Descrição chave: Neon, fumaça e ruínas de uma civilização esquecida
Narrativa:
Herói: Sim
Gênero: Sci-Fi
Duração: Média 
Final: Surpresa
```

## Python:

É uma linguagem popular por sua sintaxe limpa, aplicabilidade(web, ciência de dados, jogos, automação, Inteligênica Artificial), tendo uma grande comunidade ativa, um leque gigante de bibliotecas, sendo fácil de escrever e de ler.


## POO:



Nesse trabalho, abordamos os seguintes conceitos de POO:

Herança:
A classe Antagonista herda os atributos de personagem e e tem um atributo exclusivo
```python
from personagem import Personagem #extends do java
class Antagonista(Personagem):  #a classe Antagonista herda os atributos de Personagem
    def __init__( self, nome, idade, poder, personalidade, fraqueza, descricao, motivacao):
        super().__init__(nome, idade, poder, personalidade, fraqueza, descricao)  # chama o construtor da classe pai (Personagem)
        self._motivacao = motivacao#atributo exclusivo de Antagonista
    
```

Agregação:
A classe história contém os demais objetos das outras classes, eles são independentes, são criados antes na main() e depois passados para história, eles existem antes e fora dela, então se não existisse a classe historia eles continuariam existindo, diferente de composição, que seriam destruídos.
```python
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

```
5 classes de domínio, todas relacionadas entre si:
```
Temos as classes: 
Personagem: que é a base herdade por Antagonista e está agregada a História;
Antagonista: herda atributos de persongaem e está agregada a historia;
Ambiente: agregada a história;
Narrativa: agregada a história;
Historia: Agrega as demais classes;
```

Métodos com regras de negócio implementados:

Temos dois:
Um metodo que é @staticmethod que significa que não precisa de um objeto para funcionar, apenas chama pela classe:
```python
@staticmethod 
    def verifica_idade(idade):
        if idade <= 0:
            raise ValueError("Idade precisa ser maior que 0!")
        else: 
            return idade
```
O outro verifica se uma string é igual a outra:

```python
    def validar_poder(self, personagem):
        if self._poder.strip().lower() == personagem.poder.strip().lower():#segundo nao precisa pois esse pois o getter ja acessa o _poder
            raise ValueError("Que sem graça! O antagonsita não pode ter o mesmo poder que o personagem principal!")   
        else:
            return self._poder  
```

Encapsulamento, Construtores, Getters e Setters:
Encapsulamento:

```python
self.motivacao = motivacao#public
self._motivacao = motivacao#privado por convenção: sinaliza que não deve ser acessado diretamente
```
Construtores:
O python não suporta mais de um construtor como no java!
```python
class Personagem:
    def __init__(self, nome, idade, poder, personalidade, fraqueza, descricao):#innit é o constutor do phyton
        self._nome = nome #self seria o this do java no phyton, ele cria o atributo ja atribuindo ele
        self._idade = idade
        self._poder = poder
        self._personalidade = personalidade
        self._fraqueza = fraqueza
        self._descricao = descricao
```

Getters:
```python
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
```

Setters:
```python
    @texto.setter #setter pois o valor será inserido depois da geraçao da história!
    def texto(self, valor):
        self._texto = valor
```

Substituição:
```python
def __str__(self):#substitui o str da classe personagem, adicionando o atributo motivação
        return f"Nome: {self.nome} | Idade: {self.idade} | Poder: {self.poder} | Personalidade: {self.personalidade} | Fraqueza: {self.fraqueza} | Descrição: {self.descricao} | Motivação: {self.motivacao}"
```
Sem essa substituição, o Python retornaria algo como <object at ...>
```python
   def __str__(self):
        return f"Lugar: {self.lugar} | Época: {self.epoca} | Ano: {self.ano} | Descricao Chave: {self.descricao_chave}"
```


## API: 
Explicando como usamos a API do groq: Primeiro instalamos: pip install groq e pip install python-dotenv


```python
 def gerar(self):
        from groq import Groq#importação do groq
        import os#importação do sistema para ler arquivos
        from dotenv import load_dotenv#impostação para carregar um arq.env
        load_dotenv()#no .env do projeto temos a GROQ_API_KEY=blablabla, pois a chave não deve ser compartilhada

        cliente = Groq(api_key=os.environ.get("GROQ_API_KEY"))#definição da chave

        stream = cliente.chat.completions.create(
            model="llama-3.3-70b-versatile",#modelo
            messages=[# a primeira mensagem é uma mensagem onde o sistema manda antes do prompt gerado pelo código
                {"role": "system", "content": "Você é um escritor literário brasileiro extremamente criativo e talentoso. "
                "Utilize sinônimos da lingua portuguesa, evite repetições de palavras."
                "Sua missão é criar histórias envolventes, imersivas e bem estruturadas em português do Brasil. "
                "Sempre crie um título criativo e chamativo para a história. "
                "Use descrições ricas, diálogos naturais e construa uma narrativa com introdução, desenvolvimento e conclusão. "
                "Respeite rigorosamente o gênero, o cenário, os personagens e o tipo de final fornecidos. "
                "Siga EXATAMENTE as características dos personagens e cenário fornecidos."
                "Nunca quebre o estilo narrativo e nunca responda fora do formato de história."},
                {"role": "user", "content": self.montar_prompt()}#mensagem onde o usuário manda, ou seja o prompt.
            ],
            stream=True#Jeito de aparecer as linhas conforme forem sendo criadas, ao invés de printar tudo de uma vez
        )

        self._texto = ""
        for chunk in stream: #para cada pedaço que for retornando da API colocar no texto (atributo da Historia que inicialmente estava vazio)
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
                self._texto += chunk.choices[0].delta.content
        print()
```
## MÉTODOS DE STRING USADOS:

```python
resposta = input("\nSe desejar criar a história digite Y, caso queria recomeçar digite N! [Y/N] ").upper()#.upper() deixa tudo em letra maiuscula
if self._poder.strip().lower() == personagem.poder.strip().lower():#.strip() tira os espaços e .lower() deixa tudo em minusculo
if ano.isdigit():#.isdigit retorna true se conter apenas numeros
```

## MÉTODO DE LISTA:
```python
epoca = input(f"Escolha qual será a Época: {", ".join(epoca_validos)}: ")#", ".join() junta os itens da lista por uma virgula e um espaço
```

