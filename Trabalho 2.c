#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

#define EXPONENT_SIZE 11
#define MANTISSA_SIZE 52
#define SQRT_2 1.414213562373095    //15 dígitos de precisão
#define PRECISION 0.0000000001      //verificar se o abs(erro) é menor que PRECISION

//União que pode ser vista como um número float em decimal (f) e também na forma IEEE754 (bits)
typedef union nIEEE{
    double f;
    struct{
        //ORDEM IMPORTA
        uint64_t mantissa : 52;
        uint64_t exponent : 11;
        uint64_t sign : 1;
    }bits;
} nIEEE;

double newton_raphson(double, nIEEE*);

double newton_raphson(double A, nIEEE* binary){

    //Caso a entrada do usuário for 0 ou 1, retornamos a própria entrada
    if(A == 0.0 || A == 1.0){
        return A;
    }
    //Em caso de números negativos como entrada, apenas temrinamos o programa
    else if (A < 0){
        printf("Erro! Argumento nao pode ser negativo!");
        exit(EXIT_FAILURE);
    }

    int64_t e = binary->bits.exponent - 1023; // Temos acesso direto ao expoente armazenado em padrão IEEE-754
    double f1 = 0; // (1 + f)
    
    //Definição dos valores (1 + f) e o valor que multiplicaremos a raiz de (1 + f) 
    double resto_para_multiplicar = 1;
    if(e > 0){
        f1 = A / (2 << (e - 1));
        if((e % 2) == 0){
            resto_para_multiplicar = pow(2, e/2);
        }else{
            resto_para_multiplicar = SQRT_2*pow(2, (e-1)/2);
        }
    }else if(e < 0){
        f1 = A * (2 << (-e - 1));
        if((e % 2) == 0){
            resto_para_multiplicar = pow(2, e/2);
        }else{
            resto_para_multiplicar = (SQRT_2 / 2)*pow(2, (e+1)/2);
        }
    }else{
        f1 = A;
    }

    //Newton Raphson
    double xk = ((f1 - 1) / 2) + 1;
    double xk1 = (xk + (f1/xk))/2;
    double erro = fabs(xk1 - xk);

    while (erro > PRECISION)
    {
        xk = xk1;
        xk1 = (xk + (f1/xk))/2;
        erro = fabs(xk1 - xk);
    }
    
    return xk1*resto_para_multiplicar;
}

int main(void){
    //Testes
    for(float i = 0; i < 50; i = i + 0.7){

        //Inicialização da estrutura nIEEE
        nIEEE binary = {0};
        binary.f = i; //Definindo o valor de f (float decimal), mas ao mesmo tempo definindo os campos da struct bits (padrão IEEE-754)

        double valor_Newton_Raphson = newton_raphson(i, &binary);
        double valor_Sqrt_Math = sqrt(i);

        printf("i = %f - Erro = %.15lf\n", i, fabs(valor_Newton_Raphson - valor_Sqrt_Math));
    }
    return 0;
}