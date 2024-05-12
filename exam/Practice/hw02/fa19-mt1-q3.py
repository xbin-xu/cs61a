"""
3. (5 points) You Again
Implement again, which takes a function f as an argument. The again function
returns the smallest non-negative integer n for which f(n) is equal to f(m)
for some non-negative m that is less than n. Assume that f takes non-negative
integers and returns the same value for at least two different non-negative
arguments.

Constraints:
• Lines numbered 2, 4, and 5 must begin with either while or if.
• Lines numbered 6 and 7 must contain either return or =.
"""


def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x - 3) * (x - 6)


def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x - 2)


def again(f):
    """Return the smallest non-negative integer n
    such that f(n) == f(m) for some m < n.

    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee)      # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(m) != f(n):
                return n
            m = m + 1
        n = n + 1
