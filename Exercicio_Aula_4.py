
def exercicio1(): # listas com exemplos
    #criação de lista

    L=[5,7,2,9,4,1,3]
    print("o tamanho da lista é", len(L))
    print("o elemento max da lista é", max(L))
    print("o elemento min da lista é", min(L))
    print("A soma dos elementos é", sum(L))
    L.sort()
    print("A ordem crescente é", L)
    L.sort(reverse=True)
    print("A ordem decrescente é", L)

def exercicio2(): # listas com exemplos
    #inserir na lista
    lista=[]
    for x in range(4):
        nome=str(input("Insira um nome:"))
        lista.insert(x,nome)
    print(lista)
    print("o terceiro elemento é", lista[2])
    lista[0]="Joao"
    print(lista)
    lista.insert(1,"Maria") #insere na posiçao 1
    print(lista)
    lista.pop(len(lista)-1) #apagar
    print(lista)
    lista.sort() #ordena
    print("A ordem crescente é", lista)

def exercicio3():   # multiplos de 3 (de 1 a 50) apresentando duas listas
    #inserir na lista
    multiplos=[]
    pares=[]
    for x in range(1,51):
        if (x%3) == 0:
            multiplos.append(x) #coloca na ultima posiçao
            if (x%2) == 0:
                pares.append(x) 
    print("A lista dos múltiplos de 3:", multiplos)
    print("A lista de números pares:", pares)

def exercicio4(): # lista com exemplos
    numeros=[]
    for x in range(5):
        numeros.append(int(input("Insira o  valor inteiro: ")))
    print(numeros)
    print("O valor maximo  inserido foi %d"%max(numeros),min(numeros))
    media=sum(numeros)/len(numeros)
    print("O  valor da media é %f"%media)
    for x  in  numeros: #por este processo o x  corresponde  ao conteudo e nao ao indice
        if x>media:
            print("O numero %d")
    valor=int(input("Que valor pretende verificar?"))
    if valor in numeros:
        print("O valor esta presente na lista")
    else:
        print("O valor nao esta presente na lista")

def exercicio5(): # soma de listas
    L1=[5,7,2,9,4]
    L2=[1,8,5,3,2]
    novalista=[]
    cont=0
    for x in range(5):
        novalista.append(L1[x]+L2[x])
    novalista.sort()
    print(novalista)
    for i in L1:
        for j  in L2:
            if (i==j):
                cont+=1 #cont=cont+1
    print("Nº de valores iguais: ",cont)

def exercicio6(): #agenda telefonica com dicionario
    agenda={
        "Maria":[99887766,99887755],
        "Pedro":92345678,
        "Patricia":99887711
    }

    x=input("Visualizar o contacto de:")
    print(agenda[x])
    agenda["Pedro"]=914455661
    print(agenda)
    agenda["João"]=[998811234]
    print(agenda)
    print("O nº de  contactos da agenda é",len(agenda))
    print(agenda.keys()) # cria uma lista
    agenda.popitem() # apaga o item
    print(agenda)

def exercicio7(): # ementa com um dicionario
    menu={
        "Entremeada":7,
        "Sardinha":6,
        "Filetes":5.5,
        "Prego":7,
        "Hamburguer":5.5,
    }

    res=input("Quer visualizar o menu? (s/n)")
    if res=="s":
        for x,y in menu.items():
            print("Prato",x,y,"€")
        prato=input("Qual o prato que pretende:")
        if prato in menu:
            print("O prato está a ser preparado!")
        else:
            print("O prato não existe ou pode estar esgotado")
    else:
        print("Obrigado pela visita")

def exercicio8(): #dicionário de tabela e media da turma
    turma={
        "Ana":12,
        "Beatriz":13,
        "António":11,
        "José":9.5
    }
    notas=turma.values()
    media=sum(notas)/4
    print("A média da turma é",media)
    print(turma)

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