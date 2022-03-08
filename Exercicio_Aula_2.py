#O código foi compilado no VSCode com interpretador Python 3.10.0rc2, estando tudo funcional. Basta indicar o número da questão e irá iniciar o programa.

#Exercicio 1 (Sucessor e Antecessor)
def exercicio1():
    n1=int(input("Insira o nº: "))
    if n1>20:
        n=n1/2
        print("A metade do valor é %s"%n)
    else:
        print("O número é menor que 20")
    

#Exercicio 2 (calculo media)
def exercicio2():
    np=int(input("Insira o nº: "))
    if (np%2) == 0:
        print("O número %s é par"%np)
    else:
        print("O número %s é ímpar"%np)
    

#Exercicio 3 (concatenação)
def exercicio3():
    npn=int(input("Insira o nº: "))
    if (npn>0):
        print("O número %s é positivo"%npn)
    elif npn<0:
        print("O número %s é negativo"%npn)
    else:
        print("O número %s é igual a zero"%npn)


#Exercicio 4 (Preço produto)
def exercicio4():
    nota=int(input("Insira a nota do aluno (1 a 5): "))
    if nota == 1:
        print("O resultado é %s é Mau"%nota)
    elif nota == 2:
        print("O resultado é %s é Insuficiente"%nota)
    elif nota == 3:
        print("O resultado é %s é Suficiente"%nota)
    elif nota == 4:
        print("O resultado é %s é Bom"%nota)
    elif nota == 5:
        print("O resultado é %s é Muito Bom"%nota)
    else:
        print("O valor introduzido está incorreto")

#Exercicio 5 (Area Retangulo)
def exercicio5():
    vcompra=int(input("Insira o valor de compra do produto: "))
    if vcompra<20:
        vvenda= vcompra+5
        print("O Valor de compra é %s€ e o valor de venda é %s€ sendo lucro 5€"%(vcompra,vvenda))
    elif vcompra>=20:
        vvenda= vcompra+10
        print("O Valor de compra é %s€ e o valor de venda é %s€ sendo lucro 10€"%(vcompra,vvenda))
    

#Exercicio 6 (Salario Liquido)
def exercicio6():
    licenciado=str(input("É licenciado? (S ou N): "))
    idade=int(input("Qual a sua idade? : "))
    if licenciado  == "S" or licenciado  == "s" and idade > 30:
        print("ACEITE")
    else:
        print("NÃO ACEITE")
    

#Exercicio 7 (Litros Gastos)
def exercicio7():
    n1=float(input("Insira o nº1: "))
    symbol=str(input("Insira a operação (+/-/*//): "))
    n2=float(input("Insira o nº2: "))
    if symbol == "+":
        print("O resultado é: ", n1 + n2)
    elif symbol == "-":
        print("O resultado é: ", n1 - n2)
    elif symbol == "*":
        print("O resultado é: ", n1 * n2)
    elif symbol == "/":
        print("O resultado é: ", n1 / n2)
    else:
        print("Operação errada")

#Exercicio 8 (Conversor Dollar-Euro)
def exercicio8():
    n1=int(input("Insira a sua idade: "))
    if n1 < 16:
        print("Não é elegível para votar. ")
    elif n1 >= 18 and n1<=65:
        print("O eleitor é obrigado a votar. ")
    elif n1 >= 16 and n1<18 or n1>65:
        print("O eleitor é pode votar (facultativo). ")
    else :
        print("A idade é inválida. ")

'''
from forex_python.converter import CurrencyRates
c= CurrencyRates()


'''
# map the inputs to the function blocks
options = {1 : exercicio1,
           2 : exercicio2,
           3 : exercicio3,
           4 : exercicio4,
           5 : exercicio5,
           6 : exercicio6,
           7 : exercicio7,
           8 : exercicio8,
}

num=int(input("Insira o número de exercicio que pretende: "))
options[num]()