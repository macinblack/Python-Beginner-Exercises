#O código foi compilado no VSCode com interpretador Python 3.10.0rc2, estando tudo funcional. Basta indicar o número da questão e irá iniciar o programa.

#Exercicio 1 (Sucessor e Antecessor)
def exercicio1():
    n0=int(input("Insira o numero: "))
    n1=n0+1
    n2=n0-1
    print("Sucessor: %s  Antecessor: %s "%(n1,n2))
    

#Exercicio 2 (calculo media)
def exercicio2():
    n0=int(input("Insira o primeiro numero: "))
    n1=int(input("Insira o segundo numero: "))
    soma=n0+n1
    media= soma/2
    print("A soma os dois valores é %s e a média é: %s" %(soma,media))
    

#Exercicio 3 (concatenação)
def exercicio3():
    nome=input("Insira o nome: ")
    apelido=input("Insira o apelido: ")
    idade=int(input("Insira a idade: "))
    print("O seu nome é", nome + " " + apelido, "e tem %d anos de idade" %idade)
    

#Exercicio 4 (Preço produto)
def exercicio4():
    price=float(input("Insira o preço em €: "))
    p_discount=float(price*0.9)
    desconto=0.10
    percentagem="{:.0%}".format(desconto)
    print("O desconto aplicado é: ", percentagem + " e o preço final é %.2f€" %p_discount)
    

#Exercicio 5 (Area Retangulo)
def exercicio5():
    altura=float(input("Insira a altura "))
    largura=float(input("Insira a largura: "))
    area=altura*largura
    print("A área do retangulo é: %.2f" %area)
    

#Exercicio 6 (Salario Liquido)
def exercicio6():
    DESCONTO=1-0.14
    salario=float(input("Insira a valor hora em € "))
    hora=float(input("Insira as horas de trabalho: "))
    salario_liquido=salario*hora*DESCONTO
    print("O valor do salário líquido é: %.2f €" %salario_liquido)
    

#Exercicio 7 (Litros Gastos)
def exercicio7():
    litros=float(input("Insira o nº de litros: "))
    kms=float(input("Insira os kms percorridos: "))
    kms_litros=kms/litros
    print("O consumo médio do carro é %.2f km/l" %kms_litros)
    

#Exercicio 8 (Conversor Dollar-Euro)
def exercicio8():
    exchange=float(input("Insira o valor da cotação atual Dólares-Euro: "))
    dollar=float(input("Insira o valor em Dólares: "))
    euro=dollar*exchange
    print("O valor da conversão Dólar(es) ($%.2f) é de %.2f Euro(s) " %(dollar,euro))
    
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