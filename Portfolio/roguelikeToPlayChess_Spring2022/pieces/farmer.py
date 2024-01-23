class Farmer:
    def getDescription():
        description = "Moves and Attacks [1] Diagonally Forwards (up to 2 on first move)."
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
    
            #first move
            if piece.getTimesMoved() == 0:
                if len(board) > 0:
                    for square in board:

                        if square.getCol() == col+1 and square.getRow() == row-1:
                            validMoves.append([col+1,row-1])
                            if square.getPiece().getType() == 'Empty': #moving forward 2 if no pieces are in the way
                                validMoves.append([col+2,row-2])

                        if square.getCol() == col-1 and square.getRow() == row-1:
                            validMoves.append([col-1,row-1])
                            if square.getPiece().getType() == 'Empty': #moving forward 2 if no pieces are in the way
                                validMoves.append([col-2,row-2])
                                

            #subsequent moves
            elif piece.getTimesMoved() > 0 and row < 7:
                for square in board:
                    if square.getCol() == col+1 and square.getRow() == row-1:
                            validMoves.append([col+1,row-1])
                    #Pawn Attacks NW
                    if square.getCol() == col-1 and square.getRow() == row-1:
                            validMoves.append([col-1,row-1])

                            
        elif piece.getOwner() == 'CPU':
            #first move
            if piece.getTimesMoved() == 0:
                if len(board) > 0:
                    for square in board:
                        #moving forward 1
                        if square.getCol() == col+1 and square.getRow() == row+1:
                            if square.getPiece().getType() != "Empty":
                                validMoves.append([col+1,row+1])
                        
                        if square.getCol() == col-1 and square.getRow() == row+1:
                            if square.getPiece().getType() != "Empty":
                                validMoves.append([col-1,row+1])
                                
                        #Moving forward 2
                        if square.getCol() == col+2 and square.getRow() == row+2:
                            validMoves.append([col+2,row+2])
                        if square.getCol() == col-2 and square.getRow() == row+2:
                                validMoves.append([col-2,row+2])


            #subsequent moves
            elif piece.getTimesMoved() > 0 and row < 7:
                for square in board:
                    #Pawn Attack SE
                    if square.getCol() == col+1 and square.getRow() == row+1:
                        if square.getPiece().getType() != "Empty":
                            validMoves.append([col+1,row+1])
                    #Pawn Attacks SW
                    if square.getCol() == col-1 and square.getRow() == row+1:
                        if square.getPiece().getType() != "Empty":
                            validMoves.append([col-1,row+1])
            
    
        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    