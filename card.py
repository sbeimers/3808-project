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
