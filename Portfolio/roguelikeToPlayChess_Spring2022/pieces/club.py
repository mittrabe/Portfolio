class Club:
    def getDescription():
        description = "Can move to any square in the shape of a Club."
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

        if piece.getOwner() == "Player":
            validMoves.append([col,row-1])
            validMoves.append([col-1,row])
            validMoves.append([col+1,row])
            validMoves.append([col,row+1])
            validMoves.append([col,row+2])
            validMoves.append([col-1,row+2])
            validMoves.append([col+1,row+2])
        
        if piece.getOwner() == "CPU":
            validMoves.append([col,row+1])
            validMoves.append([col-1,row])
            validMoves.append([col+1,row])
            validMoves.append([col,row-1])
            validMoves.append([col,row-2])
            validMoves.append([col-1,row-2])
            validMoves.append([col+1,row-2])

        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    