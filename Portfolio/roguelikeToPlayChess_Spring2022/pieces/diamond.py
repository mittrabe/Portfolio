class Diamond:
    def getDescription():
        description = "Can move to any square in the shape of a Diamond."
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
   
        
        validMoves.append([col,row-2])
        validMoves.append([col+1,row-1])
        validMoves.append([col+2,row])
        validMoves.append([col+1,row+1])
        validMoves.append([col,row+2])
        validMoves.append([col-1,row+1])
        validMoves.append([col-2,row])
        validMoves.append([col-1,row-1])
           

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    