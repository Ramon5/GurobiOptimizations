from optmizations import Bootmaker, ProductFactory, TVProgram, BeltFactory, Company

def menu():
    choice = -1
    model = None
    while(choice != 0):
        print("\n1 - Problema do Sapateiro\n2 - Problema dos produtos P1 e P2\n3 - Problema da rede de TV\n4 - Problema da fabrica de cintos\n5 - Problema  da racionalização de produção")
        choice = int(input("\nEscolha um problema para solucionar: "))
        if choice == 1:
            model = Bootmaker("sapateiro")
            model.message("\nQtd. de sapato e cinto que maximizam os lucros")
        elif choice == 2:
            model = ProductFactory("produto")
            model.message("\nQtd. do produto P1 e P2 que maximizam os lucros")
        elif choice ==3:
            model = TVProgram("TV")
            model.message("\nQtd. de exibições semanais dos programas A e B")
        elif choice == 4:
            model = BeltFactory("cinto")
            model.message("\nQtd. de cinto M1 e M2")
        elif choice == 5:
            model = Company("empresa")
            model.message("\nQtd. de P1 e P2 mensal que maximizam os lucros")

        model.optimize()


if __name__ == "__main__":
    menu()