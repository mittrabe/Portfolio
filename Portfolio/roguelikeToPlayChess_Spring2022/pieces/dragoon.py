class Dragoon:
    def getDescription():
        description = "Can move to any square that's [2] out and [1] to either side (L-Shape)."
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
        validMoves.append([col,row-1])
        validMoves.append([col,row-2])
        validMoves.append([col-1,row-2])
        validMoves.append([col+1,row-2])
        
        #E
        validMoves.append([col+1,row])
        validMoves.append([col+2,row])
        validMoves.append([col+2,row-1])
        validMoves.append([col+2,row+1])


        #S
        validMoves.append([col,row+1])
        validMoves.append([col,row+2])
        validMoves.append([col-1,row+2])
        validMoves.append([col+1,row+2])

        #W
        validMoves.append([col-1,row])
        validMoves.append([col-2,row])
        validMoves.append([col-2,row-1])
        validMoves.append([col-2,row+1])


        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    