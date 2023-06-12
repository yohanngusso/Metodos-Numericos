# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:24:46 2020

@author: Yohann
"""

import math as m
import numpy as np

############################-----###########################################
def Menu():
    print('\n')
    print('**************************************')
    print('*                Menu                *')
    print('************************************ *')
    print('* 1-Raízes                           *')
    print('* 2-Sistemas de Equações Lineares    *')
    print('* 3-Interpolação                     *')
    print('* 4-Integração Numérica              *')
    print('* 5-Equações Diferenciais Ordinárias *')
    print('* 0-Sair                             *')
    print('**************************************')

############################-----############################################
def Raízes():
    print('\n')
    print('**************************************')
    print("\n1 – Bissecção")
    print("\n2 – Newton")
    print("\n3 – Secantes")
    print("\n0 – Voltar")
    print('\n')
    print('**************************************')
    raízes_1()#indo para o def que realização a confirmação para cada método especifico das raizes

############################-----############################################
def raízes_1():
    metodo = int(input("Escolha um método: "))#escolha de um dos 3 métodos do def Raízes
    if metodo > 3: # se for digitado algo maior que 3 ooções o programa volta para o def raízes_1
        print('\nDigite uma opção válida!')
        raízes_1()
    else:
        confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:')) #váriavel criada para realizar uma confirmação se o usuario digitou o metodo correto
        if confirmação == 1:
                if metodo == 1:# se for digitado 1 vai para o def bissecção 
                    print("\nBissecção\n")
                    bissecção()#chamando a função e indo para ela
                elif metodo == 2:
                    print("\nNewton\n")
                    Newton()
                elif metodo == 3:
                    print("\nSecantes\n")
                    Secantes()
        else:
                print('Voltando...')
                Raízes()


############################################################################
def SEL():
    print('\n')
    print('**************************************')
    print("\n1 – Eliminação de Gauss")
    print("\n2 – Decomposição LU")
    print("\n3 – Jacobi-Richardson")
    print("\n4 – Gauss-Seidel")
    print("\n0 – Voltar")
    print('**************************************')
    sel_1()

############################################################################
def sel_1():
    metodo = int(input("Escolha um método: "))
    if metodo > 4:
        print('\nDigite uma opção válida!')
        SEL()
    else:
        confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:'))
        if confirmação == 1:
            if metodo == 1:
                print("\nEliminação de Gauss\n")
                Gauss()
            elif metodo == 2:
                print("\nDecomposição LU\n")
                LU()
            elif metodo == 3:
                print("\nJacobi-Richardson\n")
                JacobiR()
            elif metodo == 4:
                print("\nGauss-Seidel\n")
                GaussSeidel()
        else:
            print('Voltando...')
            SEL()

############################################################################
def Interpolação():
    print('\n')
    print('**************************************')
    print("\n1 – Lagrange")
    print("\n2 – Newton")
    print("\n0 – Voltar")
    print('**************************************')
    Interpolação_1()


############################################################################
def Interpolação_1():
    metodo = int(input("Escolha um método:"))
    if metodo > 2:
        print('\nDigite uma opção válida')
        Interpolação()
    else:
        confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:'))
        if confirmação == 1:
            if metodo == 1:
                print("\nLagrange\n")
                PnLagrange()
            elif metodo == 2:
                print("\nNewton\n")
                PnNewton()
        else:
            print('Voltando...')
            Interpolação()

###########################################################################
def Integração_Numérica():
    print('\n')
    print('**************************************')
    print("\n1 - Trapézio\n")
    print("\n2 – 1/3 de Simpson\n")
    print("\n3 – 3/8 de Simpson\n")
    print("\n4 – Regra de Simpson Mistas")
    print("\n0 – Voltar\n")
    print('**************************************')
    Integração_Numérica_1()


###########################################################################
def Integração_Numérica_1():
    metodo = int(input("Escolha um método:"))
    if metodo > 4:
        print('\nDigite uma opção válida!')
        Integração_Numérica()
    else:
        confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:'))
        if confirmação == 1:
            if metodo == 1:
                print("\nTrapézio\n")
                trapezio()
            elif metodo == 2:
                print("\n1/3 de Simpson\n")
                terço_simpson()
            elif metodo == 3:
                print("\n3/8 de Simpson\n")
                oitavo_simpson()
            elif metodo == 4:
                print("\nRegra de Simpson Mistas\n")
                simpsonmisto()
                

        else:
            print('Voltando...')
            Integração_Numérica()


###########################################################################
def EDO():
    print('\n')
    print('**************************************')
    print("\n1 – Método de Taylor")
    print("\n2 – Runge-Kutta 4ª Ordem")
    print("\n3 - Euler")
    print("\n0 – Voltar")
    print('**************************************')
    EDO_1()

###########################################################################
def EDO_1():
    metodo = int(input("Escolha um método:"))
    if metodo > 3:
        print('\nDigite uma opção válida!')
        EDO()
    else:
        confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:'))
        if confirmação == 1:
            if metodo == 1:
                print("\n1 – Método de Taylor\n")
                Euler()
            elif metodo == 2:
                print("\nRunge-Kutta 4ª Ordem\n")
                Runge_Kutta()
            elif metodo == 3:
                print("\n3 - Euler\n")
                Euler()

        else:
            print('Voltando...')
            EDO()



###########################################################################
#repetição utilizando o while true
def raiz_do_programa ():

    while True:
        Menu()
        opção =int(input('Digite o assunto desejado:'))

        if opção == 1:
                Raízes() #indo para o def raiz para demonstrar o print dos métodos de raízes


        elif opção == 2:
                    SEL()


        elif opção == 3:
                Interpolação()

        elif opção == 4:
                Integração_Numérica()


        elif opção == 5:
                EDO()


        elif opção==0:
              confirmação = int(input('Você tem certeza que quer continuar ? Se sim digite 1, se não tecle qualquer número para voltar:'))
              if confirmação == 1:
                 print('Encerrando...') 
                 break #não se utiliza um def para fazer encerrar o programa pois é necessário que ele "corte" a repetição "dentro" do while True!!!

        else:
            print('Digite uma opção válida')


############################-----###########################################
#Método de Bissecção
def f(x):
    return (x+1)**2*m.exp(x**2-2)-1


def bissecção():
    a = float(input("Digite a = "))
    b = float(input("Digite b = "))
    e = float(input("Precisão = "))
    while True:
        xk = ((a+b)/2)
        #print(xk)
        print(" x = ", xk)
        if f(a)*f(xk)<0:
            b=xk
        elif  f(a)*f(xk)>0:
            a=xk
        x_novo = ((a+b)/2)
        if (abs(x_novo-xk)/abs(x_novo) < e) :
            print("Raiz encontrada!!! x = ", x_novo)
            break
#após os calculos ele volta para o menu automaticamente por ser while true até que seja utilizado no próprio def raiz_do_programa o comando break(que para a repetição)
############################-----###########################################

#Método de Newton

def Newton ():
    x0=float(input('Digite o valor inicial:'))
    erro=float(input('Digite o erro máximo:'))

    while True:
        xk_1=x0-((FN(x0))/(DN(x0)))
        cp=((abs(xk_1-x0))/(abs (xk_1))) #criterio de parada
        if  cp<erro:
            print('A raiz da função é:',xk_1)
            break
        else:
            x0=xk_1

def FN(x):  #Função
    return ((4*m.cos(x))-(m.exp(x)))

def DN(x): #Derivada da função
    return ((-4*m.sin(x))-(m.exp(x)))


############################-----###########################################

#Método das Secantes

def Secantes():

    xi=float(input('Digite o valor inicial:'))
    xf=float(input('Digite o valor final:'))
    e=float(input('Digite o erro máximo:'))

    while True:
        xk=((xi*fs(xf)-(xf*fs(xi)))/(fs(xf)-fs(xi)))
        cp=((abs(xf-xi))/(abs (xf)))
        xi=xf
        xf=xk
        if  cp<e:
            print('A raiz da função é:', xk)
            break

def fs(x):
    return m.sqrt(x)-5*m.e**(-x)
############################-----###########################################

# Eliminação de Gauss
def Gauss():
    #Tanto em vetor como em matriz, começa da posição '0'
    #Entrada de matrizes: lista de listas (por linhas)
    A = [[5,2,1],[3,1,4],[1,1,3]]
    #Entrada de vetor: apenas uma lista
    b=[7,7,13]
    #len(A): "cálculo o total de linhas de A"
    n = len(A)
    #range(P): P é o número de vezes que tem que repetir
    for k in range(n-1):
        #range(a,b): Começa em a e vai até b-1, [a,b)
        for i in range(k+1,n):
            Mult = A[i][k]
            for j in range(k,n):
                A[i][j]=A[i][j]-A[k][j]*Mult/A[k][k]
            b[i]=b[i]-b[k]*Mult/A[k][k]
    print("A =",A)
    print("b =",b)
    print(" ")

    #Retrosubstituição:
    b[n-1]=b[n-1]/A[n-1][n-1]
    #Range(a,b,-z): Começa em a, vai até b+1, voltando de z em z
    for h in range(n-2,-1,-1):
        #Somatório:
        soma = 0
        for j in range(h+1,n):
            soma = soma + A[h][j]*b[j]
        b[h] = (b[h]-soma)/A[h][h]
    print("Solução x =",b)



############################-----###########################################
# Decomposição LU
def LU():
    A = [[5,2,1],
         [3,1,4],
         [1,1,3]]

    b = [0,-7,-5]
    n = len(A)
    #Decomposição LU, escrita na mesma matriz
    for i in range(1,n):
        for j in range(n):
            if i<=j: #Cálculo dos elementos Uij
                soma = 0
                for k in range(i):
                    soma = soma + A[i][k]*A[k][j]
                A[i][j] = A[i][j]-soma
            elif i>j: #Cálculo dos elementos Lij
                soma = 0
                for k in range(j):
                    soma = soma + A[i][k]*A[k][j]
                A[i][j] = (A[i][j]-soma)/A[j][j]
    print("\n \nNa parte estritamente inferior da matriz estão os elementos de L, na parte diagonal e superior, os elementos de U\n")
    print(A)

    #Resolução de Ly=b: substituindo da linha "2" até a linha "n"
    for i in range(1,n):
        soma = 0
        for j in range(i):
            soma = soma + A[i][j]*b[j]
        b[i] = b[i] - soma
    print("\nSolução de Ly=b, y =",b)

    #Resolução de Ux=y
    b[n-1] = b[n-1]/A[n-1][n-1]
    #range(a,b,-z): começa em a, vai até b+1, voltando de z em z
    for i in range(n-2,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma = soma + A[i][j]*b[j]
        b[i] = (b[i]-soma)/A[i][i]
    print("\nSolução de Ux=y, x =",b)

############################-----###########################################

# Jacobi-Richardson
def JacobiR():
    A=[[10,2,1],[1,5,1],[2,3,10]]
    b=[7,-8,6]
    n = len(A)
    x = np.zeros(n)
    x_old = np.zeros(n)
    e = float(input("Entre com a precisão: "))
    NM = int(input("Entre com o número máximo de iterações: "))
    k=0 #contador de iteração
    while True:
        k=k+1
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma = soma + A[i][j]*x_old[j]
            x[i] = (b[i]-soma)/A[i][i]
        print("x(",k,") =",x)
        #critério de parada:
        erro = x-x_old
        if np.max(abs(erro))/np.max(abs(x))<e:
            print("Solução encontrada!")
            break
        x_old = np.copy(x)
        #segurança para não entrar em loop infinito
        if k >= NM:
            print("Número máximo de iterações excedido!")
            print("Possível divergência no método!")
            break
############################-----###########################################

# Gauss-Seidel
def GaussSeidel():
    A=[[5,1,1],
       [3,4,1],
       [3,3,6]]

    b=[5,6,0]
    n = len(A)
    x = np.zeros(n)
    x_old = np.zeros(n)
    e = float(input("Entre com a precisão: "))
    NM = int(input("Entre com o número máximo de iterações: "))
    k=0 #contador de iteração
    while True:
        k=k+1
        for i in range(n):
            soma = 0
            for j in range(n):
                if i != j:
                    soma = soma + A[i][j]*x[j]
            x[i] = (b[i]-soma)/A[i][i]
        print("x(",k,") =",x)
        #critério de parada:
        erro = x-x_old
        if np.max(abs(erro))/np.max(abs(x))<e:
            print("Solução encontrada!")
            break
        x_old = np.copy(x)
        #segurança para não entrar em loop infinito
        if k >= NM:
            print("Número máximo de iterações excedido!")
            print("Possível divergência no método!")
            break

############################-----###########################################

# Polinômio Interpolador de Lagrange
def PnLagrange():
    x = [1,2,3]
    f = [1.5708,1.5719,1.5739]
    n=len(x)
    X = float(input("Entre com o valor a ser calculador no Polinômio, X = "))

    #Cálculo Direto no Polinômio:
    S = 0
    for k in range(n):
        Lk = 1
        for j in range(n):
            if k != j:   #  != diferente
                Lk = Lk*(X-x[j])/(x[k]-x[j])
        S = S + f[k]*Lk
    print("P(",X,") =",S)

############################-----###########################################


# Polinômio Interpolador de Newton
def PnNewton():
    x = [1,2,3]
    f = [1.5708,1.5719,1.5739]
    n=len(x)
    X = float(input("Entre com o valor a ser calculador no Polinômio, X = "))

    #Diferenças Divididas:
    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            f[j] = (f[j]-f[j-1])/(x[j]-x[j-i])
        print("f =",f)
    #Cálculo de Pn(X)
    S = 0
    for i in range(n):
        P = 1
        for j in range(i):
            P=P*(X-x[j])
        S = S + f[i]*P
    print("P(",X,") =",S)

############################-----###########################################

# Regra do Trapézio
def fb(x):
    return m.sqrt(1+(64*(x**4)+48*(x**3)+9*(x**2)))

def trapezio():

    x0 = float(input('Digite o valor inicial do intervalo de integração:'))
    x1 = float(input('Digite o valor final do intervalo de integração:'))
    n  = int(input('Digite o número de trapézios:'))

    h=(x1-x0)/n

    S=fb(x0)+fb(x1)
    for i in range (1,n):
        S+=2*(fb(x0+(i*h)))
    I=(h/2)*S

    print('O resultado da integral é:',I)

############################-----###########################################
# 1/3 de Simpson
def f_terço_simpson(x):
    return m.exp(x)*m.cos(x)

def terço_simpson():

    a = float(input("Digite o valor limite inferior a = "))
    b = float(input("Digite o valor limite superior b = "))
    n = int(input("Digite o número de intervalos desejados n = "))

    if n%2 == 0:  #Resto da divisão de A por B: A%B
        h = (b-a)/n
        s = f_terço_simpson(a) + f_terço_simpson(b)
        for i in range(1,n):
            if i%2 == 0:
                s = s + 2*f_terço_simpson(a+i*h)
            else:
                s = s + 4*f_terço_simpson(a+i*h)
        I = (h/3)*s
        print("Valor aproximado da integral com",n,"subintervalos = ",I)
    else:
        print("\nNúmero de intervalos deve ser PAR! \nTente novamente!")
        terço_simpson()


############################-----###########################################
#3/8 de Simpson
def f_simpson_oitavos(x):
    return m.exp(x)*m.cos(x)

def oitavo_simpson():
    a = float(input("Digite o valor limite inferior a = "))
    b = float(input("Digite o valor limite superior b = "))
    n = int(input("Digite o número de intervalos desejados n = "))

    if n%3 == 0:
        h = (b-a)/n
        s = f_simpson_oitavos(a) + f_simpson_oitavos(b)
        for i in range(1,n):
            if i%3 == 0:
                s = s + 2*f_simpson_oitavos(a+i*h)
            else:
                s = s + 3*f_simpson_oitavos(a+i*h)
        I = (3*h/8)*s
        print("Valor aproximado da integral com",n,"subintervalos = ",I)
    else:
        print("\nNúmero de intervalos deve ser MÚLTIPLO DE 3!\nTente novamente!")
        oitavo_simpson()

############################-----###########################################
        
def f_simpsonmisto():
    k = m.exp()*m.cos()
    return k

def simpsonmisto():
    a = float(input("Digite o valor limite inferior a = "))
    b = float(input("Digite o valor limite superior b = ")) 
    n = int(input("Digite o número de intervalos desejados n = "))
    if n%2 == 0:
        h = (b-a)/n
        s = f(a) + f(b)
        for i in range(1,n):
            if i%2 == 0:
                s = s + 2*f(a+i*h)
            else:
                s = s + 4*f(a+i*h)
        I = (h/3)*s
        print("1/3 de Simpson")
        print("Valor aproximado da integral com",n,"subintervalos = ",I)
    elif n%3 == 0:
        h = (b-a)/n
        s = f(a) + f(b)
        for i in range(1,n):
            if i%3 == 0:
                s = s + 2*f(a+i*h)
            else:
                s = s + 3*f(a+i*h)
        I = (3*h/8)*s
        print("3/8 de Simpson")
        print("Valor aproximado da integral com",n,"subintervalos = ",I)
    else:
        h = (b-a)/n
        s1 = f(a)
        for i in range(1,n-3):
            if i%2 == 0:
                s1 = s1 + 2*f(a+i*h)
            else:
                s1 = s1 + 4*f(a+i*h)
        s1 = s1 + f(a+(n-3)*h)
        I1 = (h/3)*s1
        
        s2 = f(a+(n-3)*h) + 3*(f(a+(n-2)*h)+f(a+(n-1)*h)) + f(b)
        I2 = (3*h/8)*s2
        I = I1 + I2
        print("Misto de Simpson")
        print("Valor aproximado da integral com",n,"subintervalos = ",I)
        
############################-----###########################################
#Método de Euler
def f_edo(x,y):
    return -y+x+2

def Euler():
    x = float(input("Digite o valor de x da condição inicial: x0 = "))
    y = float(input("Digite o valor de y da condição inicial: y0 = "))
    xN = float(input("Digite o valor final de x: xN = "))
    N = int(input("Digite quantos passos deseja N = "))

    h = (xN-x)/N
    print("Com estes dados, o tamanho do passo será h =",h)
    print("x( 0 ) =",x,"y( 0 ) = ",y)
    for i in range(N):
        y = y+h*f_edo(x,y)
        x = x+h
        print("x(",i+1,") =",x,"y(",i+1,") = ",y)
############################-----###########################################
#Runge-Kutta 4ª Ordem

def funçãok (x,y):

    d=-y+x+2
    return d

def Runge_Kutta():
    x = float(input("Digite o valor de x da condição inicial: x0 = "))
    y = float(input("Digite o valor de y da condição inicial: y0 = "))
    xN = float(input("Digite o valor final de x: xN = "))
    N = int(input("Digite quantos passos deseja N = "))
    P = input("Deseja visualizar os valores de k? y/n = ")
    h = (xN-x)/N
    print("Com estes dados, o tamanho do passo será h =",h)
    print("\nx( 0 ) =",x,"y( 0 ) = ",y)

    for i in range(N):
        k1 = f_edo(x,y)
        k2 = f_edo(x+h/2,y+(h*k1)/2)
        k3 = f_edo(x+h/2,y+(h*k2)/2)
        k4 = f_edo(x+h,y+(h*k3))
        if P == "y":
            print("\nk1 = ",k1)
            print("k2 = ",k2)
            print("k3 = ",k3)
            print("k4 = ",k4)
        y = y+(h/6)*(k1+2*k2+2*k3+k4)
        x = x+h
        print("x(",i+1,") =",x,"y(",i+1,") = ",y)
############################-----###########################################


raiz_do_programa() #chamando a função principal...