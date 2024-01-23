class Bishop:
    def getDescription():
        description = "Move any distance along any diagonal."
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


        #NE
        neStop = False
        colI = 1
        for i in range(row,0,-1):
            if col+colI <= 7:
                validMoves.append([col+colI,i-1])
                for square in board:
                    if square.getCol() == col+colI and square.getRow() == i-1:
                        if square.getPiece().getType() != "Empty":
                            neStop = True
                            break
            if neStop == True:
                break
            colI += 1
        #NW
        nwStop = False
        colI = 1
        for i in range(row,0,-1):
            if col-colI >= 0:
                validMoves.append([col-colI,i-1])
                for square in board:
                    if square.getCol() == col-colI and square.getRow() == i-1:
                        if square.getPiece().getType() != "Empty":
                            nwStop = True
                            break
            if nwStop == True:
                break
            colI += 1
        #SE
        seStop = False
        rowI = 1
        for i in range(col,0,-1):
            if row+rowI <= 7:
                validMoves.append([i-1,row+rowI])
                for square in board:
                    if square.getCol() == i-1 and square.getRow() == row+rowI:
                        if square.getPiece().getType() != "Empty":
                            seStop = True
                            break
            if seStop == True:
                break
            rowI += 1
        #SW
        swStop = False
        rowI = 1
        for i in range(col,7):
            if row+rowI <= 7:
                validMoves.append([i+1,row+rowI])
                for square in board:
                    if square.getCol() == i+1 and square.getRow() == row+rowI:
                        if square.getPiece().getType() != "Empty":
                            swStop = True
                            break
            if swStop == True:
                break
            rowI += 1
        
        return validMoves

    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass