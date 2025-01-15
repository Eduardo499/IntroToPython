from functools import total_ordering

@total_ordering
class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    FACE_VALUES = {
        'Ace': 14,  
        'King': 13,
        'Queen': 12,
        'Jack': 11,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    def __init__(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit

    @property
    def face(self):
        """Return the Card's face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's suit."""
        return self._suit

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'

    def card_value(self):
        """Return the value of the card based on its face."""
        return self.FACE_VALUES.get(self.face, 0)

    def __eq__(self, other):
        """Check equality of two cards (same face and suit)."""
        if isinstance(other, Card):
            return self.face == other.face and self.suit == other.suit
        return False

    def __lt__(self, other):
        """Compare two cards using their value (less than)."""
        if isinstance(other, Card):
            return self.card_value() < other.card_value()
        return NotImplemented

