from .pawn import Pawn
from .bishop import Bishop
from .knight import Knight
from .rook import Rook
from .queen import Queen
from .ai import Ai
from .altarBoy import AltarBoy
from .batteringRam import BatteringRam
from .boulder import Boulder
from .chariot import Chariot
from .club import Club
from .diamond import Diamond
from .diplomat import Diplomat
from .donkey import Donkey
from .dragoon import Dragoon
from .farmer import Farmer
from .fencer import Fencer
from .footSoldier import FootSoldier
from .fortress import Fortress
from .general import General
from .heart import Heart
from .landMine import LandMine
from .martyr import Martyr
from .necromancer import Necromancer
from .pikeman import Pikeman
from .pope import Pope
from .prince import Prince
from .princess import Princess
#WHAT HAPPENS WHEN YOU TAKE A JESTER
from .samurai import Samurai
from .spade import Spade
from .thief import Thief
from .trojan import Trojan
from .trojanHorse import TrojanHorse
from .vampire import Vampire
from .dynamite import Dynamite

class Mimic:
    def getDescription():
        description = "[Start of Game] Can move [1] square in any direction.\n\n[Captures Piece] Takes on the moveset and abilities of captured piece."
        return description

    def getMoves(pieceData):
        piece = pieceData[0]
        col = pieceData[1]
        row = pieceData[2]
        board = pieceData[3]
        validMoves = []
        pieceType = piece.getMovesetType()
        if pieceType == 'Empty':
            return validMoves

        if piece.getPiecesTaken() == 0:
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
        else:
            value1str = ['Pawn', 'Boulder', 'FootSoldier','Samurai','Farmer']
            value2str = ['Pikeman','Trojan','Martyr','AltarBoy','Donkey'] 
            value3str =['Bishop','Knight','Thief','General','Dynamite','Club']
            value4str = ['Chariot','Ai','Mimic','Heart','Spade','Diamond']
            value5str = ['Rook','TrojanHorse','BatteringRam','Fencer','Fortress','Necromancer','Pope','Dragoon']
            value6str = ['Vampire','LandMine']
            value7str = ['Diplomat','Princess','Prince']
            value8str = []
            value9str = ['Queen']
            valueListStr = [value1str,value2str,value3str,value4str,value5str,value6str,value7str,value8str,value9str]

            listNum = 0 #which value list
            listIndex = 0 #which element in said list
            found = False
            for valueArr in valueListStr:
                for pieceType in valueArr:
                    if pieceType == piece.getMovesetType():
                        found = True
                        break
                    listIndex += 1
                if found == True:
                    break
                listNum += 1
                
                        
                

            value1 = [Pawn, Boulder, FootSoldier,Samurai,Farmer]
            value2 = [Pikeman,Trojan,Martyr,AltarBoy,Donkey] #To be Added: Priest
            value3 = [Bishop,Knight,Thief,General,Dynamite,Club]
            value4 = [Chariot,Ai,Mimic,Heart,Spade,Diamond]
            value5 = [Rook,TrojanHorse,BatteringRam,Fencer,Fortress,Necromancer,Pope,Dragoon]
            value6 = [Vampire,LandMine]
            value7 = [Diplomat, Princess, Prince] #To be added: Princess, Prince
            value8 = []
            value9 = [Queen]
            valueListClass = [value1,value2,value3,value4,value5,value6,value7,value8,value9]

            

            return valueListClass[listNum][listIndex].getMoves(pieceData)
        

        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    