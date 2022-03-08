#O código foi compilado no VSCode com interpretador Python 3.10.0rc2, estando tudo funcional. Basta indicar o número da questão e irá iniciar o programa.

#Exercicio 1 (soma)
def exercicio1():
    i=1
    soma=1
    while i<19:
        i=i+3
        soma=soma+i
    print("A soma é %s" %soma)
'''
soma=0
for x in range(1,20,3):
    soma=soma+x
print("Soma total:",soma)
'''

#Exercicio 2 (numeros 0 a 20)
def exercicio2():
    i=-1
    while i<20:
        i=i+1
        print(i)

#Exercicio 3 (divisiveis por 4)
def exercicio3():
    i=0
    while i<100:
        i=i+1
        if (i%4) == 0:
            print(i)

#Exercicio 4 (tabuada)
def exercicio4():
    tab=int(input("Insira qual a tabuáda pretende): "))
    for x in range(10):
        x=x+1
        resultado=tab*x
        print("%s x %s = %s"%(tab,x,resultado))

#Exercicio 5 (Matriz *)
def exercicio5():
    num=int(input("Insira nº de asteriscos (quadrado/matriz): "))
    for x in range(num): #controla a alteraçao da linha
        for y in range(num): #controla a construçao da linha
            print(end="*")
        print("")
#Exercicio 6 (soma apenas positivos)
def exercicio6():
    soma=0
    for x in range(5):
        valor=int(input("Introduza o valor a somar:"))
        if (valor>0):
            soma=soma+valor
    print("A soma dos positivos é %s" %soma)
    
#Exercicio 7 (quantidade de pares/impares)
def exercicio7():
    par=0
    impar=0
    for x in range(5):
        valor=int(input("Introduza os valores:"))
        if (valor%2) == 0:
            par=par+1
        elif (valor%2) != 0:
            impar=impar+1
    print("O numero de pares é %s e o número de impares é %s" %(par,impar))

#Exercicio 8 (soma até pelo menos 20)
def exercicio8():
    soma=0
    valor=0
    while soma<20:
        valor=int(input("Introduza os valores até aingir pelo menos 20:"))
        soma=soma+valor
    print("O valor atingiu igual ou superior a 20")
   
#Exercicio 9 (introduzir password)
def exercicio9():
    password=0
    while password != 1234:
        password=int(input("Introduza a password:"))
        if password != 1234:
            print("A password está errada, introduza novamente.")
    print("A password está correta")


#Exercicio 10 (soma e contagem pares)
def exercicio10():
    par=0
    valor=0
    soma=0
    while (valor%2) == 0:
        valor=int(input("Introduza os valores a somar (pares):"))
        if (valor>0):
            par=par+1
            soma=soma+valor
    print("O numero de pares é %s e a soma é %s" %(par,soma))

'''
from forex_python.converter import CurrencyRates
c= CurrencyRates()

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
           9 : exercicio9,
           10 : exercicio10,
}

num=int(input("Insira o número de exercicio que pretende: "))
options[num]()