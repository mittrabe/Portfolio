from tkinter import *

class LandMine:
    def getDescription():
        description = "Can move [1] square in any direction.\n\n[On Death] Piece that captures it dies.\nSquare it dies on and [1] square in each cardinal direction are 'destroyed' and can't be landed on for the remainder of the game"
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
    
    def onCaptureAbility():
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
            if square.getCol() == col and square.getRow() == row: 
                    addToGraveyard(square,graveyardData)
                    square.removePiece()
                    square.setBackground(False)
        

    