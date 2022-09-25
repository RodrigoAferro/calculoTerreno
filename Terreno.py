import os
import math

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

#Funções para os calculos das variáveis
resultados = []
area = largura * comprimento
perimetro = 2 * (largura + comprimento)
diagonal = math.sqrt(largura**2 + comprimento**2)

def opc1():
    print(f"A área do seu terreno é: {area}.")
    if area not in resultados:
        resultados.append(area)
    os.system("pause")

def opc2():
    print(f"O perímetro do seu terreno é: {perimetro}.")
    if perimetro not in resultados:
        resultados.append(perimetro)
    os.system("pause")

def opc3():
    print(f"A diagonal do seu terreno é: {diagonal}.")
    if diagonal not in resultados:
        resultados.append(diagonal)
    os.system("pause")

def opc4():
    print("Área: " + str(resultados[0]) + "\nPerímetro: ", str(resultados[1]) + "\nDiagonal: ", str(resultados[2]))

#Menu de escolha
opc = 0
while (opc != 5):    
    os.system("cls")
    print("Digite o que deseja saber: ")
    print("[ 1 ] - Área. ")
    print("[ 2 ] - Perímetro. ")
    print("[ 3 ] - Diagonal. ")
    print("[ 4 ] - Resultados Calculados. ")
    print("[ 5 ] - Sair. ")
    opc = int(input("Escolha: "))

    if (opc == 1): opc1()
    elif (opc == 2): opc2()
    elif (opc == 3): opc3()
    elif (opc == 4): 
        opc4()        
        os.system("pause")
    else: print("Obrigado.")