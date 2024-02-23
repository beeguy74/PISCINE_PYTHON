from types import FunctionType


def ft_filter(test: FunctionType | None, items: list):
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    def default_test(a):
        return a

    test = test if test else default_test
    yield [x for x in items if test(x)]
