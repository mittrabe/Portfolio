class Fortress:
    def getDescription():
        description = "Can move to any square on the board.\nUnable to capture other pieces.\n\nCan only be captured by a Battering Ram."
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
            if square.getPiece().getType() == 'Empty':
                validMoves.append([square.getCol(),square.getRow()])

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    