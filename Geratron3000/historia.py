class historia:




















     def Perguntar(self):
        print(f"\nOlá sou {self.nome}criar uma historia com essas opções?")
        print(self)

        while True:
            resposta = input("\nSe deseja criar a história digite Y, caso queria recomeçar digite N! [Y/N] ")
            resposta = resposta.upper()
            if resposta == "Y":
                return True
            elif resposta == "N":
                return False
            else:
                print("Favor colocar um valor desejado [Y/N] ")