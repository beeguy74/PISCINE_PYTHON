from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King is naked"""

    def set_hairs(self, value):
        """I'm the hairs setter."""
        self._hairs = value

    def get_hairs(self):
        """I'm the hairs getter."""
        return self._hairs

    hairs = property(get_hairs, set_hairs)

    def set_eyes(self, value):
        """I'm the eyes setter."""
        self._eyes = value

    def get_eyes(self):
        """I'm the hairs setter."""
        return self._eyes

    eyes = property(get_eyes, set_eyes)
