import numpy as np
import matplotlib.pyplot as plt

class Receptor:
    k: int
    x: float
    y: float
    p0k: float
    Lk: float

    def Criar(self, k, x, y, p0k, Lk):
        self.k = k
        self.x = x
        self.y = y
        self.p0k = p0k
        self.Lk = Lk
        return self

    def Print(self):
        print("k:", self.k,"x:", self.x,"y:", self.y,"p0k:", self.p0k,"Lk:", self.Lk)

# – estimativa de distância radial que uma fonte emissora está do receptor k (em metros) em função da
# força do sinal 𝜌𝑘 que ele recebe.
def DistanciaK(Recp: Receptor, Pk: float):
    distancia = 10**((Recp.p0k-Pk)/(10*Recp.Lk))
    return distancia

def Exercicio1():
    print("\nExercicio 1:")
    
    #Constantes
    PosicaoReal = np.array([[0.0], [9.0]])
    pk1 = -48.4
    pk2 = -50.6
    pk3 = -32.2
    pk4 = -47.4
    pk5 = -46.3
    
    print("\nConsiderando os Receptores:")
    Recp1 = Receptor().Criar(1, 1.55, 17.63, -26.0, 2.1)
    Recp2 = Receptor().Criar(2, -4.02, 0.00, -33.8, 1.8)
    Recp3 = Receptor().Criar(3, -4.40, 9.60, -29.8, 1.3)
    Recp4 = Receptor().Criar(4, 9.27, 4.64, -31.2, 1.4)
    Recp5 = Receptor().Criar(5, 9.15, 12.00, -33.0, 1.5)

    #Cálculos dos raios das circunferências
    d1 = DistanciaK(Recp1, pk1)
    d2 = DistanciaK(Recp2, pk2)
    d3 = DistanciaK(Recp3, pk3)
    d4 = DistanciaK(Recp4, pk4)
    d5 = DistanciaK(Recp5, pk5)

    #Matriz de Coeficientes 
    A = np.array([[2 * (Recp5.x - Recp1.x), 2 * (Recp5.y - Recp1.y)],
                    [2 * (Recp5.x - Recp2.x), 2 * (Recp5.y - Recp2.y)],
                    [2 * (Recp5.x - Recp3.x), 2 * (Recp5.y - Recp3.y)],
                    [2 * (Recp5.x - Recp4.x), 2 * (Recp5.y - Recp4.y)]])

    #Matriz de Resultados
    B = [[(d1*d1) - (d5*d5) - (Recp1.x*Recp1.x) - (Recp1.y*Recp1.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d2*d2) - (d5*d5) - (Recp2.x*Recp2.x) - (Recp2.y*Recp2.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d3*d3) - (d5*d5) - (Recp3.x*Recp3.x) - (Recp3.y*Recp3.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d4*d4) - (d5*d5) - (Recp4.x*Recp4.x) - (Recp4.y*Recp4.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)]]

    #Matriz Transposta de A
    A_t = A.transpose()

    X = np.matmul(np.matmul(np.linalg.inv(np.matmul(A_t, A)), A_t), B)
    Erro = np.absolute(np.subtract(X, PosicaoReal))

    print(X)
    print(Erro)

    x = [Recp1.x, Recp2.x, Recp3.x, Recp4.x, Recp5.x, 0]
    y = [Recp1.y, Recp2.y, Recp3.y, Recp4.y, Recp5.y, 9]
    c1 = plt.Circle((Recp1.x, Recp1.y), d1, color='g', fill=False)
    c2 = plt.Circle((Recp2.x, Recp2.y), d2, color='g', fill=False)
    c3 = plt.Circle((Recp3.x, Recp3.y), d3, color='g', fill=False)
    c4 = plt.Circle((Recp4.x, Recp4.y), d4, color='g', fill=False)
    c5 = plt.Circle((Recp5.x, Recp5.y), d5, color='g', fill=False)
    n = ['R1', 'R2', 'R3', 'R4', 'R5', 'E']
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    fig.gca().add_artist(c1)
    fig.gca().add_artist(c2)
    fig.gca().add_artist(c3)
    fig.gca().add_artist(c4)
    fig.gca().add_artist(c5)
    plt.axis('square')

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()
    


def Exercicio2():
    print("\nExercicio 2:")
    PosicaoReal = np.array([[3.0], [3.0]])
    pk1 = -46.9
    pk2 = -46.4
    pk3 = -41.2
    pk4 = -45.8
    pk5 = -48.7

    print("\nConsiderando os Receptores:")
    Recp1 = Receptor().Criar(1, 1.55, 17.63, -26.0, 2.1)
    Recp2 = Receptor().Criar(2, -4.02, 0.00, -33.8, 1.8)
    Recp3 = Receptor().Criar(3, -4.40, 9.60, -29.8, 1.3)
    Recp4 = Receptor().Criar(4, 9.27, 4.64, -31.2, 1.4)
    Recp5 = Receptor().Criar(5, 9.15, 12.00, -33.0, 1.5)

    #Cálculos dos raios das circunferências
    d1 = DistanciaK(Recp1, pk1)
    d2 = DistanciaK(Recp2, pk2)
    d3 = DistanciaK(Recp3, pk3)
    d4 = DistanciaK(Recp4, pk4)
    d5 = DistanciaK(Recp5, pk5)

    #Matriz de Coeficientes 
    A = np.array([[2 * (Recp5.x - Recp1.x), 2 * (Recp5.y - Recp1.y)],
                    [2 * (Recp5.x - Recp2.x), 2 * (Recp5.y - Recp2.y)],
                    [2 * (Recp5.x - Recp3.x), 2 * (Recp5.y - Recp3.y)],
                    [2 * (Recp5.x - Recp4.x), 2 * (Recp5.y - Recp4.y)]])

    #Matriz de Resultados
    B = [[(d1*d1) - (d5*d5) - (Recp1.x*Recp1.x) - (Recp1.y*Recp1.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d2*d2) - (d5*d5) - (Recp2.x*Recp2.x) - (Recp2.y*Recp2.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d3*d3) - (d5*d5) - (Recp3.x*Recp3.x) - (Recp3.y*Recp3.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)],
         [(d4*d4) - (d5*d5) - (Recp4.x*Recp4.x) - (Recp4.y*Recp4.y) + (Recp5.x*Recp5.x) + (Recp5.y*Recp5.y)]]

    #Matriz Transposta de A
    A_t = A.transpose()

    X = np.matmul(np.matmul(np.linalg.inv(np.matmul(A_t, A)), A_t), B)
    Erro = np.absolute(np.subtract(X, PosicaoReal))

    print(X)
    print(Erro)

    x = [Recp1.x, Recp2.x, Recp3.x, Recp4.x, Recp5.x, 0]
    y = [Recp1.y, Recp2.y, Recp3.y, Recp4.y, Recp5.y, 9]
    c1 = plt.Circle((Recp1.x, Recp1.y), d1, color='g', fill=False)
    c2 = plt.Circle((Recp2.x, Recp2.y), d2, color='g', fill=False)
    c3 = plt.Circle((Recp3.x, Recp3.y), d3, color='g', fill=False)
    c4 = plt.Circle((Recp4.x, Recp4.y), d4, color='g', fill=False)
    c5 = plt.Circle((Recp5.x, Recp5.y), d5, color='g', fill=False)
    n = ['R1', 'R2', 'R3', 'R4', 'R5', 'E']
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    fig.gca().add_artist(c1)
    fig.gca().add_artist(c2)
    fig.gca().add_artist(c3)
    fig.gca().add_artist(c4)
    fig.gca().add_artist(c5)
    plt.axis('square')

    for i, txt in enumerate(n):
        ax.annotate(txt, (x[i], y[i]))

    plt.show()


def main():
    Exercicio1()
    Exercicio2()
    
if __name__ == '__main__':
    main()
