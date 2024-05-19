"""
1. (10 points) Iterators are inevitable

For each of the expressions in the table below, write the output displayed by
the interactive Python interpreter when the expression is evaluated.
The output may have multiple lines. The first row is completed for you.

* If an error occurs, write Error,
  but include all output displayed before the error.
* To display a function value, write Function.
* To display an iterator/generator value, write Iterator.
* If an expression would take forever to evaluate, write Forever.

The interactive interpreter displays the contents of the repr string of the
value of a successfully evaluated expression, unless it is None.
Assume that you have started python3 and executed the code shown on the left
first, then you evaluate each expression on the right in the order shown.
Expressions evaluated by the interpreter have a cumulative effect.

| Expression                            | Output |
|---------------------------------------+--------|
| pow(10, 2)                            | 100    |
| print(print('end', print('game')), x) |        |
| L                                     |        |
| next(x)                               |        |
| tony                                  |        |
| list(alternate(thanos[1:], thanos))   |        |
"""


def love():
    yield 1000
    yield from [2000, 3000]


x = love()
L = list(x)


def alternate(real, ity):
    i1, i2 = iter(real), iter(ity)
    try:
        while True:
            yield next(i1)
            yield next(i2)
    except StopIteration:
        yield 'inevitable'


thanos = ['power', 'space', 'reality']
tony = ['mind', 'soul', 'time']
i = iter(tony)
next(i)
tony.extend(list(i))
thanos = tony[2::-2]


def test_ans():
    """
    >>> print(print('end', print('game')), x)
    game
    end None
    None Iterator

    >>> print(L)
    [1000, 2000, 3000]

    >>> try:
    ...     next(x)
    ... except StopIteration:
    ...     print('Error')
    Error

    >>> print(tony)
    ['mind', 'soul', 'time', 'soul', 'time']

    >>> print(list(alternate(thanos[1:], thanos)))
    ['mind', 'time', 'inevitable']
    """
