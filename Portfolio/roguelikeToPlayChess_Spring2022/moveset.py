from xml.etree.ElementTree import PI
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.ai import Ai
from pieces.altarBoy import AltarBoy
from pieces.batteringRam import BatteringRam
from pieces.boulder import Boulder
from pieces.chariot import Chariot
from pieces.club import Club
from pieces.diamond import Diamond
from pieces.diplomat import Diplomat
from pieces.donkey import Donkey
from pieces.dragoon import Dragoon
from pieces.farmer import Farmer
from pieces.fencer import Fencer
from pieces.footSoldier import FootSoldier
from pieces.fortress import Fortress
from pieces.general import General
from pieces.heart import Heart
from pieces.jester import Jester
from pieces.landMine import LandMine
from pieces.martyr import Martyr
from pieces.mimic import Mimic
from pieces.necromancer import Necromancer
from pieces.pikeman import Pikeman
from pieces.pope import Pope
from pieces.priest import Priest
from pieces.prince import Prince
from pieces.princess import Princess
from pieces.samurai import Samurai
from pieces.spade import Spade
from pieces.thief import Thief
from pieces.trojan import Trojan
from pieces.trojanHorse import TrojanHorse
from pieces.vampire import Vampire
from pieces.dynamite import Dynamite

class Movesets:

    def getOnDeathAbility(self, piece, col, row, board, graveyardData, start, *args):
        pieceData = [piece, col, row, board]
        pieceType = piece.getType()

        if pieceType == 'Martyr':
            Martyr.onDeathAbility(pieceData, graveyardData, start)
        #if pieceType == 'TrojanHorse':
            #TrojanHorse.onDeathAbility(pieceData, graveyardData, start, args[0])
        
        #else:
            #return "no 'on death' ability"

    def getDescription(self, piece):
        desc = ''
        pieceType = piece.getType()

            
        if pieceType == 'Empty': #DONE
            return ''

        if pieceType == "Pawn": #DONE
            desc = Pawn.getDescription()

        elif pieceType == "Bishop": #DONE
            desc = Bishop.getDescription()

        elif pieceType == "Knight": #DONE
            desc = Knight.getDescription()

        elif pieceType == "Rook": #DONE
            desc = Rook.getDescription()

        elif pieceType == "Queen": #DONE
            desc = Queen.getDescription()

        elif pieceType == "King": #DONE
            desc = King.getDescription()

        elif pieceType == "Boulder": #DONE
            desc = Boulder.getDescription()

        elif pieceType == "FootSoldier": #DONE
            desc = FootSoldier.getDescription()

        elif pieceType == "Samurai": #DONE
            desc = Samurai.getDescription()

        elif pieceType == "Farmer": #DONE
            desc = Farmer.getDescription()

        elif pieceType == "Pikeman": #DONE
            desc = Pikeman.getDescription()

        elif pieceType == "Trojan": #DONE 
            desc = Trojan.getDescription()

        elif pieceType == "Martyr": #DONE (HAS ABILITY)
            desc = Martyr.getDescription()

        elif pieceType == "AltarBoy": #DONE 
            desc = AltarBoy.getDescription()

        elif pieceType == "Donkey": #DONE
            desc = Donkey.getDescription()

        elif pieceType == "Thief": #DONE (HAS ABILITY)
            desc = Thief.getDescription()

        elif pieceType == "General": #DONE
            desc = General.getDescription()

        elif pieceType == "Dynamite": #DONE
            desc = Dynamite.getDescription()

        elif pieceType == "LandMine": #DONE (NEEDS ABILITY)
            desc = LandMine.getDescription()

        elif pieceType == "Club": #DONE
            desc = Club.getDescription()

        elif pieceType == "Chariot": #DONE 
            desc = Chariot.getDescription()

        elif pieceType == "Ai": #DONE 
            desc = Ai.getDescription()

        elif pieceType == "Mimic": #DONE (Needs Diagram)
            desc = Mimic.getDescription()

        elif pieceType == "Heart": #DONE
            desc = Heart.getDescription()

        elif pieceType == "Spade": #DONE
            desc = Spade.getDescription()

        elif pieceType == "Diamond": #DONE 
            desc = Diamond.getDescription()

        elif pieceType == "TrojanHorse": #DONE (HAS ABILITY) 
            desc = TrojanHorse.getDescription()

        elif pieceType == "Fortress": #DONE (MIGHT NEED NERFING) 
            desc = Fortress.getDescription()

        elif pieceType == "BatteringRam": #DONE 
            desc = BatteringRam.getDescription()

        elif pieceType == "Fencer": #DONE 
            desc = Fencer.getDescription()

        elif pieceType == "Necromancer": #DONE (HAS ABILITY) 
            desc = Necromancer.getDescription()

        elif pieceType == "Pope": #DONE 
            desc = Pope.getDescription()

        elif pieceType == "Vampire": #DONE 
            desc = Vampire.getDescription()

        elif pieceType == "Jester": #NOT DONE (Needs Diagram)
            desc = Jester.getDescription()

        elif pieceType == "Dragoon": #DONE
            desc = Dragoon.getDescription()

        elif pieceType == "Diplomat": #DONE (NEEDS ABILITY)
            desc = Diplomat.getDescription()

        elif pieceType == "Princess": #NOT DONE 
            desc = Princess.getDescription()
            
        elif pieceType == "Prince": #NOT DONE 
            desc = Prince.getDescription()

        
        
            

        return desc
    
    
    def getMoveset(self, piece, col, row, board, when):
        pieceData = [piece, col, row, board]
        validMoves = []
        if piece.getType() != 'Jester' or when == 'update':
            pieceType = piece.getMovesetType()
        if piece.getType() == 'Jester' and when == 'move':
            pieceType = "Jester"

            
        if pieceType == 'Empty': #DONE
            return validMoves

        if pieceType == "Pawn": #DONE
            validMoves = Pawn.getMoves(pieceData)

        elif pieceType == "Bishop": #DONE
            validMoves = Bishop.getMoves(pieceData)

        elif pieceType == "Knight": #DONE
            validMoves = Knight.getMoves(pieceData)

        elif pieceType == "Rook": #DONE
            validMoves = Rook.getMoves(pieceData)

        elif pieceType == "Queen": #DONE
            validMoves = Queen.getMoves(pieceData)

        elif pieceType == "King": #DONE
            validMoves = King.getMoves(pieceData)

        elif pieceType == "Boulder": #DONE
            validMoves = Boulder.getMoves(pieceData)

        elif pieceType == "FootSoldier": #DONE
            validMoves = FootSoldier.getMoves(pieceData)

        elif pieceType == "Samurai": #DONE
            validMoves = Samurai.getMoves(pieceData)

        elif pieceType == "Farmer": #DONE
            validMoves = Farmer.getMoves(pieceData)

        elif pieceType == "Pikeman": #DONE
            validMoves = Pikeman.getMoves(pieceData)

        elif pieceType == "Trojan": #DONE 
            validMoves = Trojan.getMoves(pieceData)

        elif pieceType == "Martyr": #DONE (NEEDS ABILITY)
            validMoves = Martyr.getMoves(pieceData)

        elif pieceType == "AltarBoy": #DONE 
            validMoves = AltarBoy.getMoves(pieceData)

        elif pieceType == "Donkey": #DONE
            validMoves = Donkey.getMoves(pieceData)

        elif pieceType == "Thief": #DONE (NEEDS ABILITY)
            validMoves = Thief.getMoves(pieceData)

        elif pieceType == "General": #DONE
            validMoves = General.getMoves(pieceData)

        elif pieceType == "Dynamite": #DONE
            validMoves = Dynamite.getMoves(pieceData)

        elif pieceType == "LandMine": #DONE (NEEDS ABILITY)
            validMoves = LandMine.getMoves(pieceData)

        elif pieceType == "Club": #DONE
            validMoves = Club.getMoves(pieceData)

        elif pieceType == "Chariot": #DONE 
            validMoves = Chariot.getMoves(pieceData)

        elif pieceType == "Ai": #DONE 
            validMoves = Ai.getMoves(pieceData)

        elif pieceType == "Mimic": #DONE (Needs Diagram)
            validMoves = Mimic.getMoves(pieceData)

        elif pieceType == "Heart": #DONE
            validMoves = Heart.getMoves(pieceData)

        elif pieceType == "Spade": #DONE
            validMoves = Spade.getMoves(pieceData)

        elif pieceType == "Diamond": #DONE 
            validMoves = Diamond.getMoves(pieceData)

        elif pieceType == "TrojanHorse": #DONE (NEEDS ABILITY) 
            validMoves = TrojanHorse.getMoves(pieceData)

        elif pieceType == "Fortress": #DONE (MIGHT NEED NERFING) 
            validMoves = Fortress.getMoves(pieceData)

        elif pieceType == "BatteringRam": #DONE 
            validMoves = BatteringRam.getMoves(pieceData)

        elif pieceType == "Fencer": #DONE 
            validMoves = Fencer.getMoves(pieceData)

        elif pieceType == "Necromancer": #DONE (NEEDS ABILITY) 
            validMoves = Necromancer.getMoves(pieceData)

        elif pieceType == "Pope": #DONE 
            validMoves = Pope.getMoves(pieceData)

        elif pieceType == "Vampire": #DONE 
            validMoves = Vampire.getMoves(pieceData)

        elif pieceType == "Jester": #NOT DONE (Needs Diagram)
            validMoves = Jester.getMoves(pieceData)

        elif pieceType == "Dragoon": #DONE
            validMoves = Dragoon.getMoves(pieceData)

        elif pieceType == "Diplomat": #DONE (NEEDS ABILITY)
            validMoves = Diplomat.getMoves(pieceData)

        elif pieceType == "Princess": #NOT DONE 
            validMoves = Princess.getMoves(pieceData)
            
        elif pieceType == "Prince": #NOT DONE 
            validMoves = Prince.getMoves(pieceData)

        
        
            

        return validMoves
            