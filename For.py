import random

print("***********")
print("Bem vindo!")
print("***********")


numero_secreto = round(random.randrange(1, 101)) #A função round() faz com que o numero seja arredondado
total_de_tentativas = 0
rodada = 1


print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível:"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



print(numero_secreto)

for rodada in range(1, total_de_tentativas +1):
    print("Tentativa {} de {} ".format( rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 a 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue #diferente do break, ele continua com a próxima interação



    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break #aqui ele encerra o laço de repetição.
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto!")



    rodada = rodada +1


