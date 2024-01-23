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
from .mimic import Mimic
from .necromancer import Necromancer
from .pikeman import Pikeman
from .pope import Pope
from .prince import Prince
from .princess import Princess
from .samurai import Samurai
from .spade import Spade
from .thief import Thief
from .trojan import Trojan
from .trojanHorse import TrojanHorse
from .vampire import Vampire
from .dynamite import Dynamite

import random 

class Jester:
    def getDescription():
        description = "[On Move] Takes on the moveset and abilities of a random piece with value 7 or below."
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
        

        value1str = ['Pawn', 'Boulder', 'FootSoldier','Samurai','Farmer']
        value2str = ['Pikeman','Trojan','Martyr','AltarBoy','Donkey'] 
        value3str =['Bishop','Knight','Thief','General','Dynamite','Club']
        value4str = ['Chariot','Ai','Mimic','Heart','Spade','Diamond']
        value5str = ['Rook','TrojanHorse','BatteringRam','Fencer','Fortress','Necromancer','Pope','Dragoon']
        value6str = ['Vampire','LandMine']
        value7str = ['Princess','Prince'] 
        valueListStr = [value1str,value2str,value3str,value4str,value5str,value6str,value7str]

        value1 = [Pope,Pawn, Boulder, FootSoldier,Samurai,Farmer]
        value2 = [Pikeman,Trojan,Martyr,AltarBoy,Donkey] #To be Added: Priest
        value3 =[Bishop,Knight,Thief,General,Dynamite,Club]
        value4 = [Chariot,Ai,Mimic,Heart,Spade,Diamond]
        value5 = [Rook,TrojanHorse,BatteringRam,Fencer,Fortress,Necromancer,Pope,Dragoon]
        value6 = [Vampire,LandMine]
        value7 = [Princess, Prince] 
        valueList = [value1,value2,value3,value4,value5,value6,value7]

        randValue = random.randint(0,len(valueList)-1)
        randPiece = random.randint(0,len(valueList[randValue])-1)
        newType = valueList[randValue][randPiece]
        newTypeStr = valueListStr[randValue][randPiece]
        piece.setMovesetType(newTypeStr)
        validMoves = newType.getMoves(pieceData)
                   


        return validMoves
    
    def onCaptureAbility():
        pass

    def onDeathAbility():
        pass

    