import Adivinhacao
import Forca

print("*******************************")
print("******Escolha o seu jogo!******")
print("*******************************")


print("(1) Forca (2) Adivinhação")

jogo = int(input("O que deseja jogar?"))


if(jogo ==1):
    print("Jogando forca")
    Forca.jogar()
elif(jogo ==2):
    print("jogando adivinhação")
    Adivinhacao.jogar()