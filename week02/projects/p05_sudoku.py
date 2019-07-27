def sudoku(board):
    if (board == []):
        return ">> invalid"
    for r in board:
        for i in r:
            if (i >=1 and i <= 9):
                continue
            else:
                return ">> invalid"
        if (len(r) == 9):
            continue
        else:
            return ">> invalid"
    valid = True
    
    checked = 0
    flag = 0
    if (valid == True):
        for r in board:
            for el in r:
                count = r.count(el)
                if(count == 1):
                    flag += 1
                else:
                    return ">> unfinished"
                if(flag == 9):
                    checked += 1
                    flag = 0
        
        if(checked == 9):
            checkedRow = True
            checked = 0
        else:
            return ">> invalid"
            
        if(checkedRow == True):
            for i in range(9):
                c = []
                for row in board:
                    c.append(row[i])
                for el in c:
                    count = c.count(el)
                if(count == 1):
                    checked += 1
        if(checked == 9):
            checkedColumn = True
            checked = 0
            
        if(checkedColumn == True):
            arr = []
            for r in range(3):
                for c in range(3):
                    block = []
                    for i in range(3):
                        for j in range(3):
                            block.append(board[3*r + i][3*c + j])
                    arr.append(block)
            for i in arr:
                for x in i:
                    count = i.count(x)
                if (count == 1):
                    checked += 1
                if (checked == 9):
                    return ">> finished"
                                
print(sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [1, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
