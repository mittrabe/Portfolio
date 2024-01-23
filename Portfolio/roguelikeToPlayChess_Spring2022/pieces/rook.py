class Rook:
    def getDescription():
        description = "Can Move any distance along any cardinal direction."
        return description

    def getMoves(pieceData):
        piece = pieceData[0]
        col = pieceData[1]
        row = pieceData[2]
        board = pieceData[3]
        validMoves = []
        pieceType = piece.getType()
        if pieceType == 'Empty':
            return validMoves

        #N
        nStop = False
        for i in range(row,0,-1):
            validMoves.append([col,i-1])
            for square in board:
                if square.getCol() == col and square.getRow() == i-1:
                    if square.getPiece().getType() != "Empty":
                        nStop = True
                        break
            if nStop == True:
                break
        #S
        sStop = False
        for i in range(row,7):
            validMoves.append([col,i+1])
            for square in board:
                if square.getCol() == col and square.getRow() == i+1:
                    if square.getPiece().getType() != "Empty":
                        sStop = True
                        break
            if sStop == True:
                break
        #E
        eStop = False
        for i in range(col,0,-1):
            validMoves.append([i-1,row])
            for square in board:
                if square.getCol() == i-1 and square.getRow() == row:
                    if square.getPiece().getType() != "Empty":
                        eStop = True
                        break
            if eStop == True:
                break
        #W
        wStop = False
        for i in range(col,7):
            validMoves.append([i+1,row])
            for square in board:
                if square.getCol() == i+1 and square.getRow() == row:
                    if square.getPiece().getType() != "Empty":
                        wStop = True
                        break
            if wStop == True:
                break
        
        return validMoves

    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass