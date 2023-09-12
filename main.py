import numpy as np
import math

def no_censor(numbers):
    numbers.sort()
    tam = len(numbers)
    y, ft, x = [], [], []
    sum, sum2 = 0, 0
    for i in range(tam):
        ft.append(
                abs(
                        ((i+1) - 0.3)/(tam + 0.4)
                    )
            )
        y.append(math.log(math.log(1/(1 - ft[i]))))
        x.append(math.log(numbers[i]))
        sum += x[i] * y[i]
        sum2 += x[i]**2
    media1 = np.mean(x)
    media2 = np.mean(y)
    a = (sum - (tam) * media1 * media2)/(sum2 - (tam) * media1**2)
    b = media2 - a * media1
    print(a, b)

def censor(numbers):
    numbers.sort()
    censurados = list(map(int, input("Digite os numeros censurados:").split()))
    tam = len(numbers)
    tamanho_censura = len(censurados)
    y, ft, x = [], [], []
    sum, sum2 = 0, 0
    for i in range(tam):
        ft.append(
                abs(
                        ((i+1) - 0.3)/(tam + 0.4)
                    )
            )
        y.append(math.log(math.log(1/(1 - ft[i]))))
        x.append(math.log(numbers[i]))
        sum += x[i] * y[i]
        sum2 += x[i]**2
    media1 = np.mean(x)
    media2 = np.mean(y)
    a = (sum - (tam) * media1 * media2)/(sum2 - (tam) * media1**2)
    b = media2 - a * media1
    print(a, b)

def main():
    censura = input()
    numbers = list(map(int, input().split()))
    if 'C' in censura or 'c' in censura:
        censor(numbers)
    else:
        no_censor(numbers)


if __name__ == "__main__":
    main()
