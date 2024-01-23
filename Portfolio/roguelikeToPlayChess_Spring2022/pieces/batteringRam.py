class BatteringRam:
    def getDescription():
        description = "Can move in any cardinal direction.\nMust move as far as possible.\n\nCan capture the Fortress and Boulder."
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
            for square in board:
                if square.getCol() == col and square.getRow() == i-1:
                    if square.getPiece().getType() != "Empty" or i-1 == 0:
                        nStop = True
                        validMoves.append([col,i-1])
                        break
            if nStop == True:
                break
        #S
        sStop = False
        for i in range(row,7):
            for square in board:
                if square.getCol() == col and square.getRow() == i+1:
                    if square.getPiece().getType() != "Empty" or i+1 == 7:
                        validMoves.append([col,i+1])
                        sStop = True
                        break
            if sStop == True:
                break
        #E
        eStop = False
        for i in range(col,0,-1):
            for square in board:
                if square.getCol() == i-1 and square.getRow() == row:
                    if square.getPiece().getType() != "Empty" or i-1 == 0:
                        validMoves.append([i-1,row])
                        eStop = True
                        break
            if eStop == True:
                break
        #W
        wStop = False
        for i in range(col,7):
            for square in board:
                if square.getCol() == i+1 and square.getRow() == row:
                    if square.getPiece().getType() != "Empty" or i+1 == 7:
                        validMoves.append([i+1,row])
                        wStop = True
                        break
            if wStop == True:
                break

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    