import os

largura = -1
comprimento = -1
#Checar se os valores são válidos.
while (largura<0) and (comprimento<0):
    largura = float(input("Digite o valor da largura do terreno: "))
    comprimento = float(input("Digite o valor do comprimento do terreno: "))
  
    os.system("cls")
  
    if (largura>0) and (comprimento>0):
        print(f"Valor da largura: {largura}")
        print(f"Valor do comprimento: {comprimento}")
        print("")
    else:
        os.system("cls")
        print("Valor/es inválido/s para largura e/ou comprimento. ")
#Calculo da área e perímetro
area = largura * comprimento
perimetro = 2 * (largura + comprimento)
#Menu para que o cliente escolha entre os dois
print("Digite o que deseja saber: ")
print("1 - Área. ")
print("2 - Perímetro. ")
escolha = int(input("Escolha: "))

os.system("cls") 

if (escolha==1):
    print("Área: ", area)
    resposta = input("Deseja saber o Perímetro também? ")
    if (resposta=="sim"):
        print(f"O perímetro é: {perimetro} ")
    else:
        () 
else:
    print("Perímetro: ", perimetro)
    resposta = input("Deseja saber o Área também? ")
    if (resposta=="sim"):
        print(f"A área é: {area}") 
    else:
        ()
print("Obrigado.")
