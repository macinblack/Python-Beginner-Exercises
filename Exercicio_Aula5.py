import math

def exercicio1(): #calculo da circunferencia
    def circulo_area(r):
        return math.pi * r**2

    def perimetro_circulo(r):
        return 2*math.pi*r

    def diametro_circulo(r):
        return 2*r

    print("O programa pretende calcular")
    print("****************************")
    print("1- Área do círculo")
    print("2- Perímetro do Círculo")
    print("3- Diâmetro do círculo")
    print("****************************")

    raio=int(input("Qual o raio do círculo:"))
    opcao=int(input("Que informação do círculo pretende obter:"))
    if opcao==1:
        print("Valor da área:",circulo_area(raio))
    elif opcao==2:
        print("Valor do perimetro:",perimetro_circulo(raio))
    elif opcao==3:
        print("Valor do diâmtreo:",diametro_circulo(raio))
    else:
        print("Entrada Inválida!")

def exercicio2(): #comparar 2 valores e indicar o maior
    def maior(x,y):
        if x>y:
            print("O maior valor inserido foi o primeiro:",x)
        else:
            print("O maior valor inserido foi o segundo:",y)

    maior(int(input("Insira o primeiro valor:")),int(input("Insira o primeiro valor:")))

def exercicio3(): #funçao de desenhar uma linha
    def linha(n):
        for x in range(n):
            print(end="_")

    linha(int(input("Insira o tamanho da linha:")))

def exercicio4(): #media com função
    def media(l,cycles):
        med=0
        for x in range(cycles):
            med=l[x]+med
        med=med/cycles
        return med

    lista=[]
    n=int(input("Indique o número de elementos:"))
    for x in range(n):
        num=int(input("Insira o número:"))
        lista.append(num)

    print("O valor da média é: ", media(lista,n))

def exercicio5():  #desenho de asteriscos com funçao
    def desenha(n):
        for x in range(n):
            print(end="*")
        print("")

    desenha(3)
    desenha(5)
    desenha(7)
    desenha(5)
    desenha(3)

def exercicio6(): #pesquisa de valores
    def pesquisar(l,valor):
        if valor in l:
            return True
        else:
            return False

    lista=[1,2,3,4]
    n=int(input("Insira o valor a pesquisar na lista:"))
    if pesquisar(lista,n) == True:
        print("O valor %s está presente na lista!"%n)
    else:
        print("O valor %s não está presente na lista!"%n)


# map the inputs to the function blocks
options = {1 : exercicio1,
           2 : exercicio2,
           3 : exercicio3,
           4 : exercicio4,
           5 : exercicio5,
           6 : exercicio6,
}

num=int(input("Insira o número de exercicio que pretende: "))
options[num]()