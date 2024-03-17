class calculator:
    """ class that is able to do calculations
(addition, multiplication, subtraction, division) of vector with a scalar."""

    def __init__(self, values: list[int | float]):
        """calculator's constructor, takes list of numbers"""
        self.values = values

    def _print(self, values=None):
        """calculator's method print, prints argument or itself"""
        print(values if values else self.values)

    def __add__(self, object: int | float) -> None:
        """calculator's method add, adds scalar to itself"""
        self.values = [x + object for x in self.values]
        self._print()

    def __mul__(self, object) -> None:
        """calculator's method mul, multiplies itself by scalar"""
        self.values = [x * object for x in self.values]
        self._print()

    def __sub__(self, object) -> None:
        """calculator's method sub, substract scalar from itslef"""
        self.values = [x - object for x in self.values]
        self._print()

    def __truediv__(self, object) -> None:
        """calculator's method truediv, divides itself by scalar"""
        assert object != 0, "Division by 0"
        self.values = [x / object for x in self.values]
        self._print()
