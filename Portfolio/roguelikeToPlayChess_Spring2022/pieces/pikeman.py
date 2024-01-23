class Pikeman:
    def getDescription():
        description = "Moves forward [1] (up to 2 on first move).\n\nAttacks up to [2] Diagonally Forwards."
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
                        #Pawn only moving forward 2 if no piece is in front
                        if square.getCol() == col and square.getRow() == row-1:
                            if square.getPiece().getType() == "Empty":
                                validMoves.append([col,row-1])
                                #Checking if pawn can move forward 2
                                for square in board:
                                    if square.getCol() == col and square.getRow() == row-2:
                                        if square.getPiece().getType() == "Empty":
                                            validMoves.append([col,row-2])

            #subsequent moves
            elif piece.getTimesMoved() > 0 and row < 7:
                for square in board:
                    if square.getCol() == col and square.getRow() == row-1:
                        if square.getPiece().getType() == "Empty":
                            validMoves.append([col,row-1])

            #Attack
            for square in board:
                #Pawn Attack NE
                if square.getCol() == col+1 and square.getRow() == row-1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col+1,row-1])
                if square.getCol() == col+2 and square.getRow() == row-2:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col+2,row-2])

                #Pawn Attacks NW
                if square.getCol() == col-1 and square.getRow() == row-1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col-1,row-1])
                if square.getCol() == col-2 and square.getRow() == row-2:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col-2,row-2])

        elif piece.getOwner() == 'CPU':
            #first move
            if piece.getTimesMoved() == 0:
                if len(board) > 0:
                    for square in board:
                        #Pawn only moving forward 2 if no piece is in front
                        if square.getCol() == col and square.getRow() == row+1:
                            if square.getPiece().getType() == "Empty":
                                validMoves.append([col,row+1])
                                #Checking if pawn can move forward 2
                                for square in board:
                                    if square.getCol() == col and square.getRow() == row+2:
                                        if square.getPiece().getType() == "Empty":
                                            validMoves.append([col,row+2])


            #subsequent moves
            elif piece.getTimesMoved() > 0 and row < 7:
                for square in board:
                    if square.getCol() == col and square.getRow() == row+1:
                        if square.getPiece().getType() == "Empty":
                            validMoves.append([col,row+1])
            
            #Attack
            for square in board:
                #Pawn Attack SE
                if square.getCol() == col+1 and square.getRow() == row+1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col+1,row+1])
                if square.getCol() == col+1 and square.getRow() == row+1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col+2,row+2])
                #Pawn Attacks SW
                if square.getCol() == col-1 and square.getRow() == row+1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col-2,row+2])
        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    