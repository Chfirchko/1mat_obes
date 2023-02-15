import numpy as np

e = 0.1  # Точность задачи
n = 2  # Размерность
m = 0.5  # длина ребра симплекса
n1 = 0  # Счетчик для центра тяжести
excludeF = []


def Example(x1, x2):
    return 2.8 * x2 ** 2 + 1.9 * x1 + 2.7 * x1 ** 2 + 1.6 - 1.9 * x2


def Grow1(n, m):
    return ((np.sqrt(n + 1) - 1) / (n * np.sqrt(2))) * m


def Grow2(n, m):
    return ((np.sqrt(n + 1) + n - 1) / (n * np.sqrt(2))) * m


def Checkmax(x):
    for i in excludeF:
        if i == x:
            return False
    return True


x1 = [1]
x2 = [1]
F = []
F.append(Example(x1[0], x2[0]))
delta1 = Grow1(n, m)
delta2 = Grow2(n, m)

x1.append(x1[0] + delta1)
x2.append(x2[0] + delta2)
x1.append(x1[0] + delta2)
x2.append(x2[0] + delta1)
F.append(Example(x1[1], x2[1]))
print('Исходные данные')
print(x1, x2, F, sep='\n')
qwerty = 0
while qwerty < 10:
    F.append(Example(x1[qwerty + 2], x2[qwerty + 2]))
    max = 0
    min = F[0]
    for i in range(len(F) - 1):
        if F[i] > max and Checkmax(F[i]) == True:
            max = F[i]
        if F[i] < min:
            min = F[i]
    excludeF.append(max)
    weight = []

    print('max = ', max, 'min = ', min)

    qwerty += 1

print('Результат')
print(x1, x2, F, sep='\n')
