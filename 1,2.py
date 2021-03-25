from terminaltables import AsciiTable

a = {1: [10, 260, 4, 64, 3010, 2],
     2: [10, 200, 4, 128, 4030, 3],
     3: [8, 200, 6, 64, 4160, 2],
     4: [10, 190, 60, 64, 4820, 3],
     5: [9, 200, 6, 128, 5000, 2],
     6: [8, 200, 8, 128, 5000, 3],
     7: [9, 260, 128, 3400, 3],
     8: [8, 200, 6, 64, 3000, 2],
     9: [9, 200, 4, 64, 3300, 2],
     10: [8, 220, 6, 64, 4780, 2]
     }

alternatives = {1: [10, 260, 4, 64, 3010, 2],
                2: [10, 200, 4, 128, 4030, 3],
                3: [8, 200, 6, 64, 4160, 2],
                4: [10, 190, 60, 64, 4820, 3],
                5: [9, 200, 6, 128, 5000, 2],
                6: [8, 200, 8, 128, 5000, 3],
                7: [9, 260, 128, 3400, 3],
                8: [8, 200, 6, 64, 3000, 2],
                9: [9, 200, 4, 64, 3300, 2],
                10: [8, 220, 6, 64, 4780, 2]
                }
tableData = [
    [' ', 'Толщина(мм)-', 'Вес(г)-', 'Опер память(Гб)+', 'Память (Гб)+',
     'Аккумулятор(Mah)+', 'К.во камер+'],
    ['A1', 10, 260, 4, 64, 3010, 2],
    ['A2', 10, 200, 4, 128, 4030, 3],
    ['A3', 8, 200, 6, 64, 4160, 2],
    ['A4', 10, 190, 6, 64, 4820, 3],
    ['A5', 9, 200, 6, 128, 5000, 2],
    ['A6', 8, 200, 8, 128, 5000, 3],
    ['A7', 9, 260, 8, 128, 3400, 3],
    ['A8', 8, 200, 6, 64, 3000, 2],
    ['A9', 9, 200, 4, 64, 3300, 2],
    ['A10', 8, 220, 6, 64, 4780, 2]
]

resultTable = AsciiTable(tableData)
resultTable.inner_heading_row_border = True
resultTable.outer_border = False
resultTable.inner_row_border = False

print(resultTable.table)

box = {1: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       2: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       3: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       4: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       5: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       6: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       7: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       8: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       9: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
       10: ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H']
       }


buffer = []
for i in range(1, 10):

    for g in range(i, 11):
        check = False
        check_box = [True, True, False, False, Felse , Felse]

        for y in range(1, 3):
            if alternatives[i][y] >= alternatives[g][y]:
                check_box[y - 1] = True

        if check_box[0] and check_box[1]:
            for y in range(2, 5):
                if alternatives[i][y] <= alternatives[g][y]:
                    check_box[y - 1] = True

        for y in range(0, 5):
            if not check_box[y]:
                check = True
                break

        if not check and i != g:
            box[i][g - 1] = 'A' + str(g)
            if g not in buffer:
                buffer.append(g)
        else:
            box[i][g - 1] = 'X'

table_X = [
    [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
    ['1'] + box[1],
    ['2'] + box[2],
    ['3'] + box[3],
    ['4'] + box[4],
    ['5'] + box[5],
    ['6'] + box[6],
    ['7'] + box[7],
    ['8'] + box[8],
    ['9'] + box[9],
    ['10'] + box[10]
]

resultT = AsciiTable(table_X)
resultT.inner_heading_row_border = True
resultT.outer_border = False
resultT.inner_row_border = False
resultT.inner_column_border = True

print()
print("Таблица Парето")
print(resultT.table)
