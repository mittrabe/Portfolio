class Movesets():

    def getMoveset(self, piece, col, row, board):
        validMoves = []
        pieceType = piece.getPieceType()
        if pieceType == 'Empty':
            return validMoves

        if pieceType == "Pawn":
            if piece.getPieceColor() == "black":
                #first move
                if piece.getTimesMoved() == 0:
                    validMoves.append([col,row-1])
                    if len(board) > 0:
                        for square in board:
                            if square.getCol() == col and square.getRow() == row-1:
                                print(square.getCoordinates())
                                if square.getPiece().getPieceType() == "Empty":
                                    validMoves.append([col,row-2])
                #subsequent moves
                elif piece.getTimesMoved() > 0 and row < 7:
                    validMoves.append([col,row-1])

            elif piece.getPieceColor() == 'white':
                #first move
                if piece.getTimesMoved() == 0:
                    validMoves.append([col,row+1])
                    validMoves.append([col,row+2])
                #subsequent moves
                elif piece.getTimesMoved() > 0 and row > 0:
                    validMoves.append([col,row+1])
            

            
        elif pieceType == "Bishop":
            pass
        elif pieceType == "Knight":
            pass
        elif pieceType == "Rook":
            pass
        elif pieceType == "Queen":
            pass
        elif pieceType == "King":
            #N, NE, NW
            if row < 7: #N
                validMoves.append([col,row+1])
                if col < 7: #NE
                    validMoves.append([col+1,row+1])
                if col > 0: #NW
                    validMoves.append([col-1,row+1])
            
            #S, SE, SW
            if row > 0: #S
                validMoves.append([col,row-1])
                if col < 7: #SE
                    validMoves.append([col+1,row-1])
                if col > 0: #SW
                    validMoves.append([col-1,row-1])
            
            #E, W
            if col < 7: #E
                validMoves.append([col+1,row])
            if col > 0: #W
                validMoves.append([col-1,row])


        return validMoves
            