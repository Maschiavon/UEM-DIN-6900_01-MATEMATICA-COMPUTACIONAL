import math
import numpy as np
import matplotlib.pyplot as plt


def MCcos(x : float) -> float:
    # Mudança de variável para economizar multiplicações
    y = x*x

    # Constantes
    if2 = -0.5
    if4 = 1/24
    if6 = -1/720
    if8 = 1/40320
    if10 = -1/3628800
    if12 = 1/479001600

    # 7 primeiros termos da Série de Taylor para a função cosseno com reestruturação com esquema de Horner
    return (1 + y*(if2 + y*(if4 + y*(if6 + y*(if8 + y*(if10 + y*if12))))))

def MCsin(x : float) -> float:
    # Mudança de variável para economizar multiplicações
    y = x*x

    # Constante
    if3 = -1/6
    if5 = 1/120
    if7 = -1/5040
    if9 = 1/362880
    if11 = -1/39916800

    # 6 primeiros termos da Série de Taylor para a função seno com reestruturação com esquema de Horner
    return (x + x*y*(if3 + y*(if5 + y*(if7 + y*(if9 + y*if11)))))


def main():
    # Serve para printar os resultados
    x = []
    y = []
    fig, ax = plt.subplots()

    PI = math.pi

    # Conversão do ângulo digitado pelo usuário em graus para radianos no intervalo entre [0, 2PI] 
    # i = math.radians(float(input("Digite um ângulo (em graus): "))) % (2*math.pi)
    increment = 2*PI/30
    for i in np.arange(0.0, 2*PI, increment):
        x.append(i)
        r = 0
        # Conversão dos ângulos maiores que PI radianos para seu respectivo angulo negativo em radianos
        if (PI < i) and (i < 2*PI):
            i = -(2*PI - i)
        
        # Se estiver dentro do intervalo aceitável [-PI/4, PI/4], apenas calculamos o seno de i 
        if (-PI/4 <= i) and (i <= PI/4):
            r = MCsin(i)
            print("I = " + str(i) + " Erro = " + str(abs(MCsin(i) - math.sin(i))))
        
        # sen(x) = cos(x - PI/2) nesse intervalo
        elif (PI/4 < i) and (i <= 3*PI/4):
            r = MCcos(i - PI/2)
            print("I = " + str(i) + " Erro = " + str(abs(MCcos(i - PI/2) - math.sin(i))))
        
        # sen(x) = -sen(x - PI) nesse intervalo
        elif (3*PI/4 < i) and (i <= PI):
            r = -MCsin(i - PI)
            print("I = " + str(i) + " Erro = " + str(abs(-MCsin(i - PI) - math.sin(i))))
        
        # sen(x) = -cos(x + PI/2) nesse intervalo
        elif (-3*PI/4 < i) and (i < -PI/4):
            r = -MCcos(PI/2 + i)
            print("I = " + str(i) + " Erro = " + str(abs(-MCcos(PI/2 + i) - math.sin(i))))
        
        # sen(x) = -sen(PI + x) nesse intervalo
        else:
            r = -MCsin(PI + i)
            print("I = " + str(i) + " Erro = " + str(abs(-MCsin(PI + i) - math.sin(i))))
        y.append(r)

    ax.scatter(x, y)
    plt.axis('square')
    for i in range(1, 30):
        ax.annotate("", (x[i], y[i]))

    plt.show()
        

if __name__ == '__main__' :
    main()