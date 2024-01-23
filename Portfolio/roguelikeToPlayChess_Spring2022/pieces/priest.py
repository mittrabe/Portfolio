class Priest:
    def getDescription():
        description = ""
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
        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    