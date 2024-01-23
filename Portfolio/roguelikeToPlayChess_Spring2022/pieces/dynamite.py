from tkinter import *

class Dynamite:
    def getDescription():
        description = "Can move [1] square in any direction.\n\n[On Death] Piece that captures it dies.\nSquare it dies on is 'destroyed' and can't be landed on for the remainder of the game"
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
        pass

    