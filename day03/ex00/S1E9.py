from abc import ABC, abstractmethod


class Character(ABC):
    """class Character: Abstract class with with
    constructor and abstract method die"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Character's constructor: takes first_name as first parameter,
        is_alive as second non mandatory parameter
        set to True by default"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Character's abstract method die(): this method should change health
        state"""
        pass


class Stark(Character):
    """class Stark: child of Character class, implements method die"""

    def die(self) -> None:
        """Stark's method die() set an attribute is_alive to False"""
        self.is_alive = False
