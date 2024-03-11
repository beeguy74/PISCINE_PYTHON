from abc import ABC, abstractmethod


    class Character(ABC):
        """Abstract class with with
        constructor and abstract method die"""
        def __init__(self, first_name, is_alive=True) -> None:
            """takes first_name as first parameter,
            is_alive as second non mandatory parameter
            set to True by default"""
            self.first_name = first_name
            self.is_alive = is_alive

        @abstractmethod
        def die(self):
            """this method should change health state"""
            pass


    class Stark(Character):
        """child of Character class, implements method die"""
        def __init__(self, first_name, is_alive=True) -> None:
            super().__init__(first_name, is_alive)

        def die(self) -> None:
            """set an attribute is_alive to False"""
            self.is_alive = False
