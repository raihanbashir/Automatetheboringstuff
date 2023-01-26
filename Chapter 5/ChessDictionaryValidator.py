def isValidChessBoard(board) :
    cblack = 0
    cwhite = 0
    type = ['pawn','rook','knight','bishop','queen','king']
    axis = ['a','b','c','d','e','f','g','h']
    pos = list(board.keys())
    piece = list(board.values())
    while True :
        #Checking if both kings are present and only one in number
        if piece.count('bking') != 1:
            return False
            break
        if piece.count('wking') != 1:
            return False
            break

        #Checking if there are at most 8 pawns for both sides
        if piece.count('bpawn') > 8 :
            return False
            break
        if piece.count('wpawn') > 8 :
            return False
            break

        #Checking if there are 16 pieces for both sides and no other items are present on the chess board
        for i in piece :
            if i[0] == 'b':
                cblack += 1
            elif i[0] == 'w':
                cwhite += 1
            else :
                return False
                exit()
        if cblack > 16 :
            return False
            break
        if cwhite > 16:
            return False
            break

        #Checking positions of the pieces
        for i in pos:
            if int(i[0]) > 8 :
                return False
                break
            if i[1] not in axis :
                return False
                break

        #Checking the type of the piece
        for i in piece:
            if i[1:] not in type :
                return False
                break
        
        #If everything is in order
        return True


board = {}
#Creating the chess board
n = int(input('Enter the number of pieces on the board : '))
for i in range(n):
     pos = input('Enter the position of the piece : ')
     piece = input('Enter the type of piece with prefix "b" or "w" to specify colour : ')
     board[pos] = piece

#Checking the board
print(isValidChessBoard(board))