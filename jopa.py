import sympy as sp

'''
лекция:
func = x ** 2 - x * y + 3 * y ** 2 - x
e = 0.1
h = 0.4
table = [[0, [0, 0], 0]]
методичка:
func = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
e = 0.1
h = 0.4
table = [[0, [1, 1], 0]]
'''



def Str_count(s):
    s = ''.join(s.split())
    s = compile(s, 'string', 'eval')
    return float(eval(s))


def Str_count_h(s):
    s = ''.join(s.split())
    print(s)
    perviy = s[:s.find("*")]
    vtoroy = s[s.find("-") + 1:]
    print('qwetrverewqgeqrgv   ', perviy, vtoroy, sep='\n')
    perviy = round(float(perviy), 10)
    vtoroy = round(float(vtoroy), 10)
    return vtoroy / perviy


def Func(x, y):
    return x ** 2 - x * y + 3 * y ** 2 - x


x, y, h = sp.symbols('x, y, h')
func = x ** 2 - x * y + 3 * y ** 2 - x

e = 0.0001
he = 0.4
table = [[0, [0, 0], 0]]
table[0][2] = Func(table[0][1][0], table[0][1][1])
Norm = 100
i = 0
delta = sp.diff(func, x)
delta1 = sp.diff(func, y)
print('Градиент: ', delta, delta1, sep='\n')
print()
delta = str(delta)
delta1 = str(delta1)
while Norm > e:
    print('--------------------------------------')
    print('Номер итерации: ', i)
    print('--------------------------------------')


    v1 = delta.replace('x', str(table[i][1][0]))
    v1 = v1.replace('y', str(table[i][1][1]))
    v2 = delta1.replace('x', str(table[i][1][0]))
    v2 = v2.replace('y', str(table[i][1][1]))

    v1 = Str_count(v1)
    v2 = Str_count(v2)

    v = [v1, v2]
    print('Значение градиента:', v)

    x1 = [table[i][1][0] - h * v[0], table[i][1][1] - h * v[1]]
    print('Координаты точки x' + str(i + 1) + ': ', x1)
    expr = x1[0] ** 2 - x1[0] * x1[1] + 3 * x1[1] ** 2 - x1[0]
    expr = sp.diff(expr)
    expr = str(expr)
    he = Str_count_h(expr)
    print(he)
    x1 = [table[i][1][0] - he * v[0], table[i][1][1] - he * v[1]]
    print('Координаты точки x' + str(i + 1) + ': ', x1)
    f1 = Func(x1[0], x1[1])
    print('Значение функции в точке x' + str(i + 1) + ': ', f1)
    table.append([i + 1, x1, f1])
    print()
    print("таблица:")
    for item in table:
        print(item)
    if table[i][2] > table[i + 1][2]:
        delta = str(delta)
        delta1 = str(delta1)

        v1 = delta.replace('x', str(table[i + 1][1][0]))
        v1 = v1.replace('y', str(table[i + 1][1][1]))
        v2 = delta1.replace('x', str(table[i + 1][1][0]))
        v2 = v2.replace('y', str(table[i + 1][1][1]))

        v1 = Str_count(v1)
        v2 = Str_count(v2)

        v = [v1, v2]
        print('вектор градиента:', v)
        Norm = sp.sqrt(v[0] ** 2 + v[1] ** 2)
        print('Норма вектора градиента: ', Norm)
        i += 1
    else:
        h = h / 2
        x1 = [table[i][1][0] - h * v[0], table[i][1][1] - h * v[1]]
        print('Координаты новой точки x' + str(i + 1) + ': ', x1)
        f1 = Func(x1[0], x1[1])
        print('Значение функции в новой точке x' + str(i + 1) + ': ', f1)
        table.pop()
        table.append([i + 1, x1, f1])
        delta = str(delta)
        delta1 = str(delta1)

        v1 = delta.replace('x', str(table[i + 1][1][0]))
        v1 = v1.replace('y', str(table[i + 1][1][1]))
        v2 = delta1.replace('x', str(table[i + 1][1][0]))
        v2 = v2.replace('y', str(table[i + 1][1][1]))

        v1 = Str_count(v1)
        v2 = Str_count(v2)

        v = [v1, v2]
        print('вектор градиента:', v)
        Norm = sp.sqrt(v[0] ** 2 + v[1] ** 2)
        print('Норма вектора градиента: ', Norm)
        i += 1
print('Найденная точка: ', Func(table[len(table) - 1][1][0], table[len(table) - 1][1][1]))
