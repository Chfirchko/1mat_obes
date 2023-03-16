import sympy


def Func(x, y):
    return x ** 2 - x * y + 3 * y ** 2 - x
    #return 2.8 * y ** 2 + 1.9 * x + 2.7 * x ** 2 + 1.6 - 1.9 * y

e = 0.0001
h = 0.2
d = 2
min = 10000
luck = 0
m = 0.5
table = [[[0, 0], 0]]
table[0][1] = Func(table[0][0][0], table[0][0][1])
'''-------------------------------------------------'''
# table.append([1, [table[0][1][0] + h, table[0][1][1]], 0])
# table[1][2] = Func(table[0][1][0] + h, table[0][1][1])
# if table[1][2] < table[0][2]:
#     min = table[1][2]
#     luck += 1
# else:
#     table.pop()
# table.append([2, [table[1][1][0], table[1][1][1] + h], 0])
# table[2][2] = Func(table[1][1][0], table[1][1][1] + h)
# if table[2][2] < min:
#     min = table[1][2]
#     luck += 1
# else:
#     table.pop()
#     table.append([2, [table[1][1][0], table[1][1][1] - h], 0])
#     table[2][2] = Func(table[1][1][0], table[1][1][1] - h)
#     if table[2][2] < min:
#         min = table[1][2]
#         luck += 1
#     else:
#         table.pop()
# if luck == 0:
#     h = h / 2
# else:
#     table.append([2, [table[1][1][0] + m * (table[1][1][0] - table[1][1][1]), table[1][1][1] + m * (table[1][1][1] - table[0][1][1])], 0])
#     table[2][2] = Func(table[2][1][0], table[2][1][1])
for i in table:
    print(i)
table1 = []
item = 0
kol = 0
while h > e:
    print('h =', h)
    table1.clear()
    item = len(table) - 1
    qwerty = table[item][1]
    table1.append([[table[item][0][0] + h, table[item][0][1]], 0])
    table1.append([[table[item][0][0], table[item][0][1] + h], 0])
    table1.append([[table[item][0][0] - h, table[item][0][1]], 0])
    table1.append([[table[item][0][0], table[item][0][1] - h], 0])
    for i in range(0, 4):
        table1[i][1] = Func(table1[i][0][0], table1[i][0][1])


    for i in table1:
        if i[1] < table[len(table) - 1][1]:
            kol += 1
            table.append(i)
            qwerty = i[1]

    if kol == 0:
        h = h / 2
        continue
    if qwerty == table[len(table) - 1][1] :
        table.append([[table[len(table) - 1][0][0] + m * (table[len(table) - 1][0][0] - table[len(table) - 2][0][0]),
                       table[len(table) - 1][0][1] + m * (table[len(table) - 1][0][1] - table[len(table) - 2][0][1])],
                      0])
        table[len(table) - 1][1] = Func(table[len(table) - 1][0][0], table[len(table) - 1][0][1])
        if table[len(table) - 1][1] > table[len(table) - 2][1]:
            table.pop()

    item += 1
    for i in table1:
        table1.pop()
    kol = 0
print()
for i in table:
    print(i)