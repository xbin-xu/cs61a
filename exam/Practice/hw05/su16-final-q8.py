"""
8. (5 points) Zhen-erators Produce Power

Implement the generator function powers of two that iterates over the infinite
sequence of non-negative integer powers of two, starting from 1.
You must do this by selectively including elements from an infinite sequence of
integers, created by calling the provided integers generator function.
You may only use the lines provided. You may not need to fill all the lines.
Hint: You may find the drop generator function useful.
"""


def integers(n):
    while True:
        yield n
        n += 1


def drop(n, s):
    for _ in range(n):
        next(s)
    for elem in s:
        yield elem


def powers_of_two(ints=integers(_________)):
    """
    >>> p = powers_of_two()
    >>> [next(p) for _ in range (10)]
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    """
    curr = _____________________________________________________________
    yield ______________________________________________________________
    yield from _________________________________________________________
