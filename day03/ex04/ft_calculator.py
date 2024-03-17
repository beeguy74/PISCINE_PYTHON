class calculator:
    """ class that is able to do calculations
(addition, multiplication, subtraction, division) of vector with a scalar.
Class also is able to do calculations (dot product, addition, subtraction)
of 2 vectors. Vectors will always have identical sizes, no error handling.
"""

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

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """calculator's class method prints product of scalar
multiplications of V1 and V2"""
        res = [V1[i] * V2[i] for i in range(0, len(V1))]
        print("Dot product is:", sum(res))

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """calculator's class method prints sum vector of V1 and V2"""
        res = [float(V1[i] + V2[i]) for i in range(0, len(V1))]
        print("Add Vector is:", res)

    @classmethod
    def sous_vec(csl, V1: list[float], V2: list[float]) -> None:
        """calculator's class method prints result vector
of substraction V2 from V1"""
        res = [float(V1[i] + V2[i]) for i in range(0, len(V1))]
        res = [float(V1[i] - V2[i]) for i in range(0, len(V1))]
        print("Sous Vector is:", res)
