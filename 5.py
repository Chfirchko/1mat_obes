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

def Func(x, y):
    return 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y


def Str_count(s):
    s = ''.join(s.split())
    s = compile(s, 'string', 'eval')
    return (eval(s))


x, y = sp.symbols('x, y')
func = 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y
e = 0.01
table = [[0, [-0.25, 0.5], 0]]
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


    gesse = sp.zeros(2)

    gesse[0] = float(sp.diff(Str_count(delta), x))
    gesse[1] = float(sp.diff(Str_count(delta), y))
    gesse[2] = float(sp.diff(Str_count(delta1), x))
    gesse[3] = float(sp.diff(Str_count(delta1), y))
    print('Матрица Гессе:', gesse, '', sep='\n')
    d = float(gesse[0] * gesse[3] - gesse[1] * gesse[2])
    print(gesse[0])
    if int(gesse[0]) > 0 and d > 0:
        print('угловые миноры матрицы Гессе:')
        print(gesse[0], '> 0')
        print(d, '> 0')
        v1 = delta.replace('x', str(table[i][1][0]))
        v1 = v1.replace('y', str(table[i][1][1]))
        v2 = delta1.replace('x', str(table[i][1][0]))
        v2 = v2.replace('y', str(table[i][1][1]))
        v1 = Str_count(v1)
        v2 = Str_count(v2)

        v = [v1, v2]
        gesse = gesse.inv()
        print('Составляющие вектора:', v, gesse)
        x11 = [gesse[0] * v[0] + gesse[1] * v[1], gesse[2] * v[0] + gesse[3] * v[1]]
        x12 = [table[i][1][0] - x11[0], table[i][1][1] - x11[1]]
        print('Координаты точки х(', i + 1, '): ', x12, sep='')
        table.append([1, x12, Func(x12[0], x12[1])])
        print(delta)
        v1 = delta.replace('x', str(table[i + 1][1][0]))
        v1 = v1.replace('y', str(table[i + 1][1][1]))
        v2 = delta1.replace('x', str(table[i + 1][1][0]))
        v2 = v2.replace('y', str(table[i + 1][1][1]))
        v1 = Str_count(v1)
        v2 = Str_count(v2)
        v = [v1, v2]
        print(v)
        Norm = sp.sqrt(v[0] ** 2 + v[1] ** 2)
        print('Норма вектора градиента: ', Norm)
        i += 1
    else:
        print('ЖОПА!!!!')
        exit()
for i in table:
    print(i)
print('Найденная точка: ', float(Func(table[len(table) - 1][1][0], table[len(table) - 1][1][1])))
