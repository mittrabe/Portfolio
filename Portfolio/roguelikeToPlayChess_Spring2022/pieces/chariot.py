class Chariot:
    def getDescription():
        description = "Can move [3] out and [1] to either side (L-Shape)."
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

        
        #NR (North Right)
        if col+1 < 8 and row-3 >= 0:
            validMoves.append([col+1,row-3])
        
        #NL (North Left)
        if col-1 >= 0 and row-3 >= 0:
            validMoves.append([col-1,row-3])

        #EN (East North)
        if col+3 < 8 and row-1 >= 0:
            validMoves.append([col+3,row-1])

        #ES (East South)
        if col+3 >= 0 and row+1 < 8:
            validMoves.append([col+3,row+1])

        #SR (South Right)
        if col+1 < 8 and row+3 < 8:
            validMoves.append([col+1,row+3])

        #SL (South Left)
        if col-1 >= 0 and row+3 < 8:
            validMoves.append([col-1,row+3])

        #WN (West North)
        if col-3 >= 0 and row+1 < 8:
            validMoves.append([col-3,row+1])

        #WS (West South)
        if col-3 >= 0 and row-1 >= 0:
            validMoves.append([col-3,row-1])
        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    