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



    def montar_prompt(self):
            return (
            f"Escreva uma história de {self.narrativa.genero} "
            f"com aproximadamente {self.narrativa.duracao}.\n\n"
            f"Cenário: {self.ambiente.lugar}, época {self.ambiente.epoca}, "
            f"ano {self.ambiente.ano}. {self.ambiente.descricao_chave}\n\n"
            f"NÃO mude os poderes, personalidades ou motivações dos personagens"
            f"Siga EXATAMENTE as características dos personagens e cenário fornecidos."
            f"Evite repetição de palavras, então use sinônimos"
            f"E SEMPRE corrija quaisquer erros de ortografia."
            f"Protragonista: {self.personagem.nome}, {self.personagem.idade} anos. "
            f"Poder: {self.personagem.poder}. "
            f"Personalidade: {self.personagem.personalidade}. "
            f"Fraqueza: {self.personagem.fraqueza}. "
            f"{self.narrativa.heroi}.\n\n"
            f"Antagonista: {self.antagonista.nome}, {self.antagonista.idade} anos. "
            f"Poder: {self.antagonista.poder}. "
            f"Motivação: {self.antagonista.motivacao}.\n\n"
            f"Final: {self.narrativa.final}.\n"
            f"Escreva em português do Brasil de forma criativa e envolvente.")
    

    def gerar(self):
            from groq import Groq
            import os
            from dotenv import load_dotenv
            load_dotenv()

            cliente = Groq(api_key=os.environ.get("GROQ_API_KEY"))

            stream = cliente.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um escritor literário brasileiro extremamente criativo e talentoso. "
                    "Utilize sinônimos da lingua portuguesa, evite repetições de palavras."
                    "Sua missão é criar histórias envolventes, imersivas e bem estruturadas em português do Brasil. "
                    "Sempre crie um título criativo e chamativo para a história. "
                    "Use descrições ricas, diálogos naturais e construa uma narrativa com introdução, desenvolvimento e conclusão que façam sentido. "
                    "Respeite rigorosamente o gênero, o cenário, os personagens e o tipo de final fornecidos. "
                    "Siga EXATAMENTE as características dos personagens e cenário fornecidos."
                    "Nunca quebre o estilo narrativo e nunca responda fora do formato de história."},
                    {"role": "user", "content": self.montar_prompt()}
                ],
                stream=True
            )

            self._texto = ""
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    self._texto += chunk.choices[0].delta.content
            print()


