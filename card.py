from dataclasses import dataclass

@dataclass
class Card:
    """Class for card information."""
    suit: str
    value: int 
    # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

    #define sorting order (Ace is highest card, 2 is lowest)
    def __lt__(self, other):
        return self.value > other.value
    
    def file_name(self) -> str:
        file_name = ""
        match self.value:
            case [2,3,4,5,6,7,8,9,10]:
                file_name += str(self.value)
            case 11:
                file_name += "jack"
            case 12:
                file_name += "queen"
            case 13:
                file_name += "king"
            case 14:
                file_name += "ace"
        file_name += "_of_"
        match self.suit:
            case "H":
                file_name += "hearts"
            case "D":
                file_name += "diamonds"
            case "C":
                file_name += "clubs"
            case "S":
                file_name += "spades"
        file_name += ".png"
            