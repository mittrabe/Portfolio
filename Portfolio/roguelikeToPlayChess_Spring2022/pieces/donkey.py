class Donkey:
    def getDescription():
        description = "Can move [2] out and [1] to either side (L-Shape).\n\nCannot Jump Over Pieces."
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
        NRValid = NLValid = ENValid = ESValid = SRValid = SLValid = WNValid = WSValid = True
        savedNSquare = ""
        savedESquare = ""
        savedWSquare = ""
        savedSSquare = ""

        for square in board:

            if row-2 >= 0:
                if square.getCol() == col and square.getRow() == row-2:
                    savedNSquare = square #SavedNSquare is because when going north/up, this square needs to be checked 2nd but would have already been iterated past by the time you need to check it
                if square.getCol() == col and square.getRow() == row-1 and square.getPiece().getType() == "Empty":
                    if savedNSquare.getPiece().getType() == "Empty":
                        validMoves.append([col+1,row-2])
                        validMoves.append([col-1,row-2])
        
            if col+2 <= 7:
                if square.getCol() == col+1 and square.getRow() == row:
                    savedESquare = square
                if square.getCol() == col+2 and square.getRow() == row and square.getPiece().getType() == "Empty":
                    if savedESquare.getPiece().getType() == "Empty":
                        validMoves.append([col+2,row-1])
                        validMoves.append([col+2,row+1])

            if col-2 >= 0:
                if square.getCol() == col-2 and square.getRow() == row:
                    savedWSquare = square
                if square.getCol() == col-1 and square.getRow() == row and square.getPiece().getType() == "Empty":
                    if savedWSquare.getPiece().getType() == "Empty":
                        validMoves.append([col-2,row-1])
                        validMoves.append([col-2,row+1])

            if row+2 <= 7:
                if square.getCol() == col and square.getRow() == row+1:
                    savedSSquare = square
                if square.getCol() == col and square.getRow() == row+2 and square.getPiece().getType() == "Empty":
                    if savedSSquare.getPiece().getType() == "Empty":
                        validMoves.append([col+1,row+2])
                        validMoves.append([col-1,row+2])
    

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    