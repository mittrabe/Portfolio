from pieces.king import King

class Movesets:

    def getMoveset(self, piece, col, row, board):
        pieceData = [piece, col, row, board]
        validMoves = []
        pieceType = piece.getType()
        if pieceType == 'Empty':
            return validMoves

        if pieceType == "Pawn":
            if piece.getColor() == "black":
                
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
                    #Pawn Attacks NW
                    if square.getCol() == col-1 and square.getRow() == row-1:
                        if square.getPiece().getType() != "Empty":
                            validMoves.append([col-1,row-1])

            elif piece.getColor() == 'white':
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
                    #Pawn Attacks SW
                    if square.getCol() == col-1 and square.getRow() == row+1:
                        if square.getPiece().getType() != "Empty":
                            validMoves.append([col-1,row+1])
            

            
        elif pieceType == "Bishop":
            #NE
            neStop = False
            colI = 1
            for i in range(row,0,-1):
                if col+colI <= 7:
                    validMoves.append([col+colI,i-1])
                    for square in board:
                        if square.getCol() == col+colI and square.getRow() == i-1:
                            if square.getPiece().getType() != "Empty":
                                neStop = True
                                break
                if neStop == True:
                    break
                colI += 1
            #NW
            nwStop = False
            colI = 1
            for i in range(row,0,-1):
                if col-colI >= 0:
                    validMoves.append([col-colI,i-1])
                    for square in board:
                        if square.getCol() == col-colI and square.getRow() == i-1:
                            if square.getPiece().getType() != "Empty":
                                nwStop = True
                                break
                if nwStop == True:
                    break
                colI += 1
            #SE
            seStop = False
            rowI = 1
            for i in range(col,0,-1):
                if row+rowI <= 7:
                    validMoves.append([i-1,row+rowI])
                    for square in board:
                        if square.getCol() == i-1 and square.getRow() == row+rowI:
                            if square.getPiece().getType() != "Empty":
                                seStop = True
                                break
                if seStop == True:
                    break
                rowI += 1
            #SW
            swStop = False
            rowI = 1
            for i in range(col,7):
                if row+rowI <= 7:
                    validMoves.append([i+1,row+rowI])
                    for square in board:
                        if square.getCol() == i+1 and square.getRow() == row+rowI:
                            if square.getPiece().getType() != "Empty":
                                swStop = True
                                break
                if swStop == True:
                    break
                rowI += 1


        elif pieceType == "Knight":
            pass
            #NR (North Right)
            if col+1 < 8 and row-2 >= 0:
                validMoves.append([col+1,row-2])
            
            #NL (North Left)
            if col-1 >= 0 and row-2 >= 0:
                validMoves.append([col-1,row-2])

            #EN (East North)
            

            #ES (East South)

            #SR (South Right)

            #SL (South Left)

            #WN (West North)
            if col-2 >= 0 and row+1 < 8:
                validMoves.append([col-2,row+1])

            #WS (West South)
            if col-2 >= 0 and row-1 >= 0:
                validMoves.append([col-2,row-1])




        elif pieceType == "Rook":
            #N
            nStop = False
            for i in range(row,0,-1):
                validMoves.append([col,i-1])
                for square in board:
                    if square.getCol() == col and square.getRow() == i-1:
                        if square.getPiece().getType() != "Empty":
                            nStop = True
                            break
                if nStop == True:
                    break
            #S
            sStop = False
            for i in range(row,7):
                validMoves.append([col,i+1])
                for square in board:
                    if square.getCol() == col and square.getRow() == i+1:
                        if square.getPiece().getType() != "Empty":
                            sStop = True
                            break
                if sStop == True:
                    break
            #E
            eStop = False
            for i in range(col,0,-1):
                validMoves.append([i-1,row])
                for square in board:
                    if square.getCol() == i-1 and square.getRow() == row:
                        if square.getPiece().getType() != "Empty":
                            eStop = True
                            break
                if eStop == True:
                    break
            #W
            wStop = False
            for i in range(col,7):
                validMoves.append([i+1,row])
                for square in board:
                    if square.getCol() == i+1 and square.getRow() == row:
                        if square.getPiece().getType() != "Empty":
                            wStop = True
                            break
                if wStop == True:
                    break



        elif pieceType == "Queen":
            #N
            nStop = False
            for i in range(row,0,-1):
                validMoves.append([col,i-1])
                for square in board:
                    if square.getCol() == col and square.getRow() == i-1:
                        if square.getPiece().getType() != "Empty":
                            nStop = True
                            break
                if nStop == True:
                    break
            #S
            sStop = False
            for i in range(row,7):
                validMoves.append([col,i+1])
                for square in board:
                    if square.getCol() == col and square.getRow() == i+1:
                        if square.getPiece().getType() != "Empty":
                            sStop = True
                            break
                if sStop == True:
                    break
            #E
            eStop = False
            for i in range(col,0,-1):
                validMoves.append([i-1,row])
                for square in board:
                    if square.getCol() == i-1 and square.getRow() == row:
                        if square.getPiece().getType() != "Empty":
                            eStop = True
                            break
                if eStop == True:
                    break
            #W
            wStop = False
            for i in range(col,7):
                validMoves.append([i+1,row])
                for square in board:
                    if square.getCol() == i+1 and square.getRow() == row:
                        if square.getPiece().getType() != "Empty":
                            wStop = True
                            break
                if wStop == True:
                    break

            #NE
            neStop = False
            colI = 1
            for i in range(row,0,-1):
                if col+colI <= 7:
                    validMoves.append([col+colI,i-1])
                    for square in board:
                        if square.getCol() == col+colI and square.getRow() == i-1:
                            if square.getPiece().getType() != "Empty":
                                neStop = True
                                break
                if neStop == True:
                    break
                colI += 1
            #NW
            nwStop = False
            colI = 1
            for i in range(row,0,-1):
                if col-colI >= 0:
                    validMoves.append([col-colI,i-1])
                    for square in board:
                        if square.getCol() == col-colI and square.getRow() == i-1:
                            if square.getPiece().getType() != "Empty":
                                nwStop = True
                                break
                if nwStop == True:
                    break
                colI += 1
            #SE
            seStop = False
            rowI = 1
            for i in range(col,0,-1):
                if row+rowI <= 7:
                    validMoves.append([i-1,row+rowI])
                    for square in board:
                        if square.getCol() == i-1 and square.getRow() == row+rowI:
                            if square.getPiece().getType() != "Empty":
                                seStop = True
                                break
                if seStop == True:
                    break
                rowI += 1
            #SW
            swStop = False
            rowI = 1
            for i in range(col,7):
                if row+rowI <= 7:
                    validMoves.append([i+1,row+rowI])
                    for square in board:
                        if square.getCol() == i+1 and square.getRow() == row+rowI:
                            if square.getPiece().getType() != "Empty":
                                swStop = True
                                break
                if swStop == True:
                    break
                rowI += 1


        elif pieceType == "King":
            validMoves = King.getMoves(pieceData)
            

        return validMoves
            