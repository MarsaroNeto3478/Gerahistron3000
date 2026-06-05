from personagem import Personagem
from antagonista import Antagonista
from ambiente import Ambiente
from narrativa import Narrativa
from historia import Historia





def menu_inicial():
    print("=" * 50)
    print("  BEM VINDO AO CRIADOR DE HISTÓRIAS!")
    print("  AQUI VOCÊ PODERÁ GERAR SUAS HISTÓRIAS")
    print("  COM O MESTRE CRIADOR!")
    print("=" * 50)
    
    while True:
        resposta = input("\nDESEJA COMEÇAR? [Y/N] ").upper()
        if resposta == "Y":
            return True
        elif resposta == "N":
            print("\nENTÃO POR QUE VOCÊ RODOU O CÓDIGO?\n")
            return False
        else:
            print(" Digite Y ou N.")

def coletar_personagem():
    print("\nCrie seu Personagem: ")
    nome = input("Nome: ")
    while True:
        try:
            idade = int(input("Idade: "))
            Personagem.verifica_idade(idade)#chama pela classe, sem criar um objeto!
            break
        except ValueError as erro:
            print(f"{erro}Tente novamente!")
        
    poder= input("Poder: ")
    personalidade = input("Personalidade: ")
    fraqueza = input("Fraqueza: ")
    descricao = input("Descrição: ")
    return Personagem(nome, idade, poder, personalidade, fraqueza, descricao) #faz duas coisas, cria o objeto e retorna ele



def coletar_antagonista(personagem):
    print("\nCrie seu Antagonista: ")
    nome = str(input("Nome: "))
    while True:
        try:
            idade = int(input("Idade: "))
            Personagem.verifica_idade(idade)#chama pela classe, sem criar um objeto!
            break
        except ValueError as erro:
            print(f"{erro}Tente novamente!")
    
    while True:
        try:
            poder= str(input("Poder: "))
            p = Antagonista(nome, idade, poder, "", "", "", "")#criaçao de um objeto provisório para chamar validar_poder()
            p.validar_poder(personagem)#passa o objeto, nao a string
            break
        except ValueError as erro:
            print(f"{erro}Tente novamente!")   

    personalidade = str(input("Personalidade: "))
    fraqueza = str(input("Fraqueza: "))
    descricao = str(input("Descrição: "))
    motivacao = str(input("Motivação: "))
    return Antagonista(nome, idade, poder, personalidade, fraqueza, descricao, motivacao)



def coletar_ambiente():
    print("\nCrie o ambiente: ")
    lugar = str(input("Lugar: "))
    epoca_validos = ["Cyberpunk", "Medieval", "Idade Média", "Pós-Apocaliptico", "Terra Mágica"]
    while True:
        epoca = input(f"Escolha qual será a Época: {", ".join(epoca_validos)}: ")
        if epoca in epoca_validos:
            break
        else: 
            print("Época inválida! Tente novamente.")
    while True:
        ano = input("Ano: ")
        if ano.isdigit():
            break
        else: 
            print("Digite uma resposta válida!")
         
    descricao_chave = str(input("Descrição Chave: "))
    return Ambiente(lugar, epoca, ano, descricao_chave)



def coletar_narrativa():
    while True:
        print("\nDetermine a Narrativa: ")
        heroi = input("Você quer que o personagem principal seja o herói? Y se sim, N se não! [Y/N] ").upper()
        if heroi == "Y":
            heroi = "O personagem Principal é o herói"
            break
        elif heroi == "N":
            heroi = "O personagem Principal não é o herói"
            break
        else:
            print("Favor colocar um valor desejado [Y/N] ")

    generos_validos = ["Comédia", "Terror", "Suspense", "Sci-Fi", "Aventura"]
    while True:
        genero = input(f"Escolha um Gênero: {", ".join(generos_validos)}: ")
        if genero in generos_validos:
            break
        else:
            print(" Gênero inválido! Tente novamente.")
    duracao_validos = ["Curta", "Média", "Longa"]
    while True:
        duracao = input(f"Duracao da história: {", ".join(duracao_validos)}. 200, 350, 600 palavras respectivamente: ")
        if duracao in duracao_validos:
            if duracao == "Curta":
                duracao = "200 palavras"
            elif duracao == "Média":
                duracao = "350 palavras"
            elif duracao == "Longa":
                duracao = "600 palavras"
            break
        else:
            print("Duração inválida! Tente novamente.")

    final_validos = ["Feliz", "Trágico", "Aberto", "Surpresa"]
    while True:
        final = input(f"Escolha como será o Final: {", ".join(final_validos)}: ")
        if final in final_validos:
            break
        else: 
            print("Final inválido! Tente novamente.")
    return Narrativa(heroi, genero, duracao, final)

def main():
    if not menu_inicial():
        return
    
    personagem  = coletar_personagem()
    antagonista = coletar_antagonista(personagem)
    ambiente    = coletar_ambiente()
    narrativa   = coletar_narrativa()

    historia = Historia(personagem, antagonista, ambiente, narrativa, "")

    if historia.Perguntar():
        print("\nGerando história...\n")
        historia.gerar()
    else:
        print("\nRecomeçando...")
        main()

if __name__ == "__main__":
    main()