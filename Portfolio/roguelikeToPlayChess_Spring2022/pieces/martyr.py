from tkinter import *

class Martyr:
    def getDescription():
        description = "Moves forward [1] (up to 2 on first move).\n\n[On Death] Captures all Pieces in 3x1 in Front."
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
                #Pawn Attacks NW
                if square.getCol() == col-1 and square.getRow() == row-1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col-1,row-1])

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
                #Pawn Attacks SW
                if square.getCol() == col-1 and square.getRow() == row+1:
                    if square.getPiece().getType() != "Empty":
                        validMoves.append([col-1,row+1])

        return validMoves
    
    def onCaptureAbility(piece):
        pass

    def onDeathAbility(pieceData, graveyardData, start):
        def addToGraveyard(square, graveyardData):
            cpuGraveyard = graveyardData[0]
            playerGraveyard = graveyardData[1]
            deadCpuPieces = graveyardData[2]
            deadPlayerPieces = graveyardData[3]

            graveyardWidth = 1920*0.15
            graveyardHeight = 1080*0.95
            graveWidth = graveyardWidth*0.15
            graveHeight = graveyardHeight*0.05

            if square.getPiece().getOwner() == "Player":
                deadPlayerPieces.append(square.getPiece())

                colNum = 0
                rowNum = 0 
                for deadPiece in deadPlayerPieces:
                    if colNum >= 5: 
                        rowNum += 1
                        colNum = 0
                    Label(playerGraveyard, bg = '#44BEB7', image=deadPiece.resizePiece(deadPiece.getImage(), int(graveWidth), int(graveHeight))).grid(column=colNum,row=rowNum, padx=3, sticky=(N,S,E,W))
                    colNum += 1
            

            elif square.getPiece().getOwner() == 'CPU':
                deadCpuPieces.append(square.getPiece())

                colNum = 0
                rowNum = 0
                for deadPiece in deadCpuPieces:
                    if colNum >= 5: 
                        rowNum += 1
                        colNum = 0
                    Label(cpuGraveyard, bg = '#44BEB7', image=deadPiece.resizePiece(deadPiece.getImage(), int(graveWidth), int(graveHeight))).grid(column=colNum,row=rowNum, padx=3, sticky=(N,S,E,W))
                    colNum += 1

        piece = pieceData[0]
        col = pieceData[1]
        row = pieceData[2]
        board = pieceData[3]

        for square in board:
            if piece.getOwner() == 'Player':
                if (square.getCol() == col or square.getCol() == col-1 or square.getCol() == col+1) and square.getRow() == row-1:
                    if square != start: #prevents the piece that takes the martyr from dying to the martyrs death ability if the piece was initially in the 3x1 of squares 
                        addToGraveyard(square,graveyardData)
                        square.removePiece()
                        
            elif piece.getOwner() == 'CPU':
                if (square.getCol() == col or square.getCol() == col-1 or square.getCol() == col+1) and square.getRow() == row+1:
                    if square != start: #prevents the piece that takes the martyr from dying to the martyrs death ability if the piece was initially in the 3x1 of squares 
                        addToGraveyard(square,graveyardData)
                        square.removePiece()
    
        
        
        

    