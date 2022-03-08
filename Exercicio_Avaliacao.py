# Desenvolvido por: Daniel Costa
# Basta correr o ficheiro e escolher o exercício (ex: Exercicio 1 inserir "1")

import math

def exercicio1(): #calculo da área do sombreado
    def circulo_area(r):
        return math.pi * r**2

    def quadrado_area(l):
        return l**2

    print("O programa pretende calcular")
    print("****************************")
    print("1- Área do círculo")
    print("2- Área do quadrado")
    print("3- área do Sombreado")
    print("****************************")

    l=int(input("Qual o valor do lado do quadrado (comprimento):"))
    raio=l/2
    
    area_c=circulo_area(raio)
    area_q=quadrado_area(l)
    area_s=area_q-area_c
    print("Valor da área do círculo: %.2f"%area_c)
    print("Valor da área do quadrado: %.2f"%area_q)
    print("Valor da área do sombreado: %.2f"%area_s)
    
def exercicio2(): #Assassino
    cont=0

    vit1=str(input("Telefonou para a vítima? (s/n):"))
    if vit1 == "s":
        cont=cont+1
    vit2=str(input("Esteve no local do crime? (s/n):"))
    if vit2 == "s":
        cont=cont+1
    vit3=str(input("Mora perto da vítima? (s/n):"))
    if vit3 == "s":
        cont+=1
    vit4=str(input("Devia para a vítima? (s/n):"))
    if vit4 == "s":
        cont+=1
    vit5=str(input("Já trabalhou com a vítima? (s/n):"))
    if vit5 == "s":
        cont+=1
   
    if cont == 2:
        print("A pessoa é supeita")
    elif cont == 3:
        print("A pessoa é cúmplice")
    elif cont == 4:
        print("A pessoa é cúmplice")
    elif cont == 5:
        print("A pessoa é o assassino")
    else:
        print("A pessoa é inocente")

def exercicio3(): #sete júris
    #inserir na lista
    nomes=[]
    notas=[]
    
    n=int(input("Insira o nº de atletas:"))

    for x in range(n):
        nome=str(input("Insira o nome do atleta:"))
        nomes.insert(n,nome)

    for i in range(len(nomes)):
        for j  in range(7):
            notas.append(int(input("Insira a %sº nota do atleta %s: " %(j+1,nomes[i]))))
        print("Estas são as notas atribuidas pelos jurados:")
        print(notas) #imprime notas
        print("Estas são as notas atribuidas pelos jurados e ordenadas:")
        notas.sort() #ordena as notas
        print(notas) #imprime notas
        notas.pop(0)
        notas.pop(5)
        media=sum(notas)/len(notas)
        print("Estas são as notas consideradas:")
        print(notas) 
        print("A média do %s é de: %.2f" %(nomes[i],media))
        notas.clear()

def exercicio4(): #Informações
    x=1
    idade= -1
    salario=-1
    sexo="k"
    while x != 0:
        nome=str(input("Introduza o Nome: preenchimento obrigatório "))
        if nome.isalpha():
            print("O nome foi aceite.")
            x=0
        else:
            print("O nome não foi aceite. Por favor repita.")

    while idade > 150 or idade < 0:
        idade=int(input("Introduza a idade: entre 0 a 150 "))
        if idade > 150 or idade < 0:
            print("A idade não foi aceite.") 
          
    while salario <= 0:
        salario=float(input("Introduza o salário: maior que zero "))
        if salario <= 0:
            print("O valor do salário não foi aceite.") 
    
    while sexo != 'f' or sexo != 'm':
        sexo=str(input("Introduza o sexo: (m/f) "))
        if sexo == "f" or sexo == "m":
            print("O sexo foi aceite.")
            break; 
        else:
            print("O sexo não foi aceite.")
            
    print("Nome: %s"%nome)
    print("Idade: %d"%idade)
    print("Salário: %.2f"%salario)
    print("Sexo: %s"%sexo)

def exercicio5():  #triângulos
    def triangulo(a,b,c):
        if(a+b<c) or (a+c<b) or (b+c<a):
            print("Não é um triângulo")
        elif (a==b) and (a==c):
            print("Triângulo Equilatero")
        elif (a==b) or (a==c) or (b==c):
            print("Triângulo Isóceles")
        else:
            print("Triângulo Escaleno")

    a = float(input("Insira o primeiro lado: "))
    b = float(input("Insira o segundo lado: "))
    c = float(input("Insira o terceiro lado: "))

    triangulo(a,b,c)
   
# mapeamento dos exercícios
options = {1 : exercicio1,
           2 : exercicio2,
           3 : exercicio3,
           4 : exercicio4,
           5 : exercicio5,
}

num=int(input("Insira o número de exercicio que pretende: "))
options[num]()