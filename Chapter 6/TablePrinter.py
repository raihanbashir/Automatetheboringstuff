tableData = [['apples','oranges','cherries','banana'],
['Alice','Bob','Carol','David'],
['dogs','cats','moose','goose']]
def printTable(table):
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(20), end = ' ')
        print('')

printTable(tableData)