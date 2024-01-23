class Boulder:
    def getDescription():
        description = "Can move [1] square in any direction.\nUnable to capture other pieces.\n\nCan only be captured by a Battering Ram."
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

        
        for square in board:
            #N, NE, NW
            if square.getCol() == col and square.getRow() == row+1 and square.getPiece().getType() == "Empty":
                validMoves.append([col,row+1])
            elif square.getCol() == col+1 and square.getRow() == row+1 and square.getPiece().getType() == "Empty":
                validMoves.append([col+1,row+1])
            elif square.getCol() == col-1 and square.getRow() == row+1 and square.getPiece().getType() == "Empty":
                validMoves.append([col-1,row+1])

            #S, SE, SW
            elif square.getCol() == col and square.getRow() == row-1 and square.getPiece().getType() == "Empty":
                validMoves.append([col,row-1])
            elif square.getCol() == col+1 and square.getRow() == row-1 and square.getPiece().getType() == "Empty":
                validMoves.append([col+1,row-1])
            elif square.getCol() == col-1 and square.getRow() == row-1 and square.getPiece().getType() == "Empty":
                validMoves.append([col-1,row-1])
        
            elif square.getCol() == col+1 and square.getRow() == row and square.getPiece().getType() == "Empty":
                validMoves.append([col+1,row])
            elif square.getCol() == col-1 and square.getRow() == row and square.getPiece().getType() == "Empty":
                validMoves.append([col-1,row])


        return validMoves
    
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    