from S1E9 import Character


def return42(first, second, third) -> str:
    """formats three arguments as string with tuple"""
    return f"Vector: {(first, second, third)}"


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True) -> None:
        """Baratheons's constructor: does't use Character's constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self) -> None:
        """Baratheon's method die: set is_alive as False"""
        self.is_alive = False

    def __repr__(self) -> str:
        """Baratheon's method __repr__: returns string
        with name, color of eyes and hairs"""
        return return42(self.family_name, self.eyes, self.hairs)

    def __str__(self) -> str:
        """Baratheons's method __repr__: returns string
        with name, color of eyes and hairs"""
        return self.__repr__


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True) -> None:
        """Stark's constructor: uses Character's constructor
        to set first_name and is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance

    def die(self) -> None:
        """Lannister's method die: set is_alive as False"""
        self.is_alive = False

    def __repr__(self) -> str:
        """Lannister's method __repr__: returns string
        with name, color of eyes and hairs"""
        return return42(self.family_name, self.eyes, self.hairs)

    def __str__(self) -> str:
        """Lannister's method __repr__: returns string
        with name, color of eyes and hairs"""
        return self.__repr__
