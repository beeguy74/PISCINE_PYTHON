class calculator:
    """ class that is able to do calculations
(addition, multiplication, subtraction, division) of vector with a scalar."""

    def __init__(self, values: list):
        self.values = values

    def _print(self):
        print(self.values)

    def __add__(self, object) -> None:
        self.values = [x + object for x in self.values]
        self._print()

    def __mul__(self, object) -> None:
        self.values = [x * object for x in self.values]
        self._print()

    def __sub__(self, object) -> None:
        self.values = [x - object for x in self.values]
        self._print()

    def __truediv__(self, object) -> None:
        assert object != 0, "Division by 0"
        self.values = [x / object for x in self.values]
        self._print()
