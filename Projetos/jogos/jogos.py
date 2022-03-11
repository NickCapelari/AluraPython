import forca
import adivinhacao
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha seu jopgo!********")
    print("*********************************")

    print("(1) Foca (2) Adivinhação")

    jogo = int (input("qual jogo: "))

    if jogo == 1:
        print("jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("jogando Adivinhação")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()