class Fencer:
    def getDescription():
        description = "Can move and attack up to [2] in any direction."
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
        for i in range(row,row-2,-1):
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
        for i in range(row,row+2):
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
        for i in range(col,col-2,-1):
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
        for i in range(col,col+2):
            validMoves.append([i+1,row])
            for square in board:
                if square.getCol() == i+1 and square.getRow() == row:
                    if square.getPiece().getType() != "Empty":
                        wStop = True
                        break
            if wStop == True:
                break

        #NE
        neStop = False
        colI = 1
        for i in range(row,row-2,-1):
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
        for i in range(row,row-2,-1):
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
        for i in range(col,col-2,-1):
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
        for i in range(col,col+2):
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

    