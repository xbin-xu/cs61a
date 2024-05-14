"""
4. (10 points) Apply Yourself

(a) (6 pt) Implement times, which takes a one-argument function f and
a starting value x. It returns a function g that takes a value y and
returns the minimum number of times that f must be called on x to return y.
Assume that calling f repeatedly on x eventually results in y
"""

def times(f, x):
    """Return a function g(y) that returns the number of f's in f(f(...(f(x)))) == y.

    >>> times(lambda a: a + 2, 0)(10)  # 5 times: 0 + 2 + 2 + 2 + 2 + 2 == 10
    5
    >>> times(lambda a: a * a, 2)(256) # 3 times: square(square(square(2))) == 256
    3
    """
    def repeat(z):
        """Yield an infinite sequence of z, f(z), f(f(z)), f(f(f(z))), f(f(f(f(z)))), ...."""
        yield ______________________________________________________________________________
        ____________________________________________________________________________________

    def g(y):
        n = 0
        for w in repeat(___________________________________________________________________):
            if _____________________________________________________________________________:
                ____________________________________________________________________________
            ________________________________________________________________________________

    return g
