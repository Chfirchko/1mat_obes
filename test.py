def epta(table):
    q = 1
    for qwerty in range(0, 4):
        max = 0
        for i in table:
            if i[2] > max and i[3] == 0:
                max = i[2]
        print(max)
        for i in table:
            if i[2] == max:
                i[3] = q
        q += 1
    for i in table:
        print(i)

table = [[[0], [1, 1], 7.1, 0],
         [[1], [1.1294095225512604, 1.482962913144534], 10.529977610806283, 0],
         [[2], [1.482962913144534, 1.1294095225512604], 11.781119181847455, 0],
         [[3], [0.6464466094067263, 1.3535533905932735], 6.514707793864213, 0]]


epta(table)