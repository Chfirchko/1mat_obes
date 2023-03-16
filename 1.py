import math as np


def Him(x1, x2):
    return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7)

def Example1(x1, x2):
    return x1 ** 2 - x1 * x2 + 3 * x2 ** 2 - x1


def Example(x):
    x1 = x[0]
    x2 = x[1]
    return x1 ** 2 - x1 * x2 + 3 * x2 ** 2 - x1

    #return 2.8 * x2 ** 2 + 1.9 * x1 + 2.7 * x1 ** 2 + 1.6 - 1.9 * x2


def Grow1(n, m):
    return ((np.sqrt(n + 1) - 1) / (n * np.sqrt(2))) * m


def Grow2(n, m):
    return ((np.sqrt(n + 1) + n - 1) / (n * np.sqrt(2))) * m


e = 0.0001  # Точность задачи
n = 2  # Размерность
m = 0.35  # длина ребра симплекса
n1 = 0  # Счетчик для центра тяжести
table = [[[0], [0, 0], 0, 0]]  # Таблица
pop_top = 0
table[0][2] = Example(table[0][1])
qwerty1 = 0
delta1 = Grow1(n, m)
delta2 = Grow2(n, m)
table.append([[1], [delta1 + table[0][1][0], delta2 + table[0][1][1]], 0, 0])
table.append([[2], [delta2 + table[0][1][0], delta1 + table[0][1][1]], 0, 0])
# Итерация 0
# --------------------------------------------------------------------------------------------------------------
table[1][2] = Example(table[1][1])
table[2][2] = Example(table[2][1])
q = 1
qwerty = 0
while qwerty != 100:
    int(qwerty)
    two_smallest_dicks = []
    big_dick = 0
    max = -1000
    # print()
    # print(max)
    # for i in table:
    #     print(i)
    # print()
    # --------------------------------------------------------------------------------------------------------------

    for i in table:
        if i[2] > max and i[3] == 0:
            max = i[2]
            big_dick = i[0][0]
    print('max = ', max)
    for i in table:
        if i[2] == max:
            i[3] = q
    q += 1
    # Рсчет центра тяжести точки
    weight = [0, 0]
    for i in table:
        if i[3] != 1:
            n1 += 1
    two_biggiest_dicks = []
    for i in table:
        two_biggiest_dicks.append([i[2], i[0]])
    two_biggiest_dicks = sorted(two_biggiest_dicks, key=lambda x: x[0])
    for asd in range(len(two_biggiest_dicks) - 2):
        two_biggiest_dicks.pop()
    two_biggiest_dicks = sorted(two_biggiest_dicks, key=lambda x: x[1])
    n2 = 0  # Счетчик для длвух мелких значений
    for i in two_biggiest_dicks:
        two_smallest_dicks.append(i)
    for i in range(len(table)):
        if n2 == 2:
            break
        if table[i][2] == two_biggiest_dicks[0][0]:
            n2 += 1
            weight[0] += table[i][1][0]
            weight[1] += table[i][1][1]
            two_biggiest_dicks.pop(0)
    weight[0] = weight[0] / n
    weight[1] = weight[1] / n
    print('weight = ', weight)
    mirror = [2 * weight[0] - table[big_dick][1][0], 2 * weight[1] - table[big_dick][1][1]]
    table.append([[3 + qwerty], mirror, 0, 0])
    print('mirror = ', mirror)
    if qwerty == 0:
        table[3][2] = Example(table[3][1])  # Значение функции в полученной вершине mirror
    else:
        if qwerty1 == 0:
            table[qwerty + 3][2] = Example(table[qwerty + 3][1])
        else:
            print(qwerty + 3 - qwerty1)
            for i in table:
                print(i)

            table[qwerty + 3 - qwerty1][2] = Example(table[qwerty + 3 - qwerty1][1])

    three_biggiest_dicks = []
    nombers_of_three_biggiest_dicks = []
    for item in table:
        three_biggiest_dicks.append(item[2])
        three_biggiest_dicks.append(item[0])
        nombers_of_three_biggiest_dicks.append(three_biggiest_dicks)
        three_biggiest_dicks = []
    nombers_of_three_biggiest_dicks = sorted(nombers_of_three_biggiest_dicks, key=lambda x: x[0])
    nombers_of_three_biggiest_dicks.pop()

    if table[len(table) - 1][2] > max:
        table.pop()

        a = table[len(table) - 1][1][0] - table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][0]
        b = 0.5 * a
        c = table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][0] + b

        a = table[len(table) - 1][1][1] - table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][1]
        b = 0.5 * a
        c1 = table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][1] + b

        table.append([[qwerty + 4], [c, c1], 0, 0])
        table[qwerty + 3 - pop_top][2] = Example(table[qwerty + 3 - pop_top][1])

        a = table[len(table) - 3 - pop_top][1][0] - table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][0]
        b = 0.5 * a
        c = table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][0] + b

        a = table[len(table) - 3 - pop_top][1][1] - table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][1]
        b = 0.5 * a
        c1 = table[nombers_of_three_biggiest_dicks[0][1][0] - pop_top][1][1] + b
        table.append([[qwerty + 5], [c, c1], 0, 0])
        table[qwerty + 4 - pop_top][2] = Example(table[qwerty + 4 - pop_top][1])
        qwerty += 2
        qwerty1 += 1
        pop_top += 1
        for i in table:
            if i[2] > max and i[3] == 0:
                max = i[2]
                big_dick = i[0][0]
        for i in table:
            if i[2] == max:
                i[3] = q
        q += 1

        Center_weight = []
        Center_weight.append(1 / 3 * float(
            table[nombers_of_three_biggiest_dicks[2][1][0]][1][0] + table[nombers_of_three_biggiest_dicks[1][1][0]][1][0] +
            table[nombers_of_three_biggiest_dicks[0][1][0]][1][0]))
        Center_weight.append(1 / 3 * float(
            table[nombers_of_three_biggiest_dicks[2][1][0]][1][1] + table[nombers_of_three_biggiest_dicks[1][1][0]][1][1] +
            table[nombers_of_three_biggiest_dicks[0][1][0]][1][1]))
        print('центр тяжести симплекса = ', Center_weight)
        print('Полученная точка = ', Example(Center_weight))
        print(table[nombers_of_three_biggiest_dicks[2][1][0]][2] - Example(Center_weight))

        print('проверка условие окончание поиска:')
        if abs(table[nombers_of_three_biggiest_dicks[0][1][0]][2] - Example(Center_weight)) < e or abs(
                table[nombers_of_three_biggiest_dicks[1][1][0]][2] - Example(Center_weight)) < e or abs(
                table[nombers_of_three_biggiest_dicks[2][1][0]][2] - Example(Center_weight)) < e:
            print(abs(table[nombers_of_three_biggiest_dicks[0][1][0]][2] - Example(Center_weight)), '< e')
            print(abs(table[nombers_of_three_biggiest_dicks[1][1][0]][2] - Example(Center_weight)), '< e')
            print(abs(table[nombers_of_three_biggiest_dicks[2][1][0]][2] - Example(Center_weight)), '< e')
            print('Это все!!!')
            break
        print(abs(table[nombers_of_three_biggiest_dicks[0][1][0]][2] - Example(Center_weight)), '> e')
        print(abs(table[nombers_of_three_biggiest_dicks[1][1][0]][2] - Example(Center_weight)), '> e')
        print(abs(table[nombers_of_three_biggiest_dicks[2][1][0]][2] - Example(Center_weight)), '> e')
    # # --------------------------------------------------------------------------------------------------------------

    print()
    for i in table:
        print(i)
    qwerty += 1
