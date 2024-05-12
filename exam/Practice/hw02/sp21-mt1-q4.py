"""
4. (10.0 points) Domain On the Range
The domain of a function is the set of all possible argument values,
while the range of a function is the set of values that it can return.
In this two part-question, you will implement higher-order functions
to restrict the domain and range of other functions.
"""

"""
(a) (4.0 points) restrict_domain

Implement restrict_domain, a function that accepts three parameters
(f, low_d, high_d) and returns a higher-order function that returns the same
thing as f when given an argument between low_d and high_d, inclusive,
and otherwise returns float("-inf").
"""


def restrict_domain(f, low_d, high_d):
    """Returns a function that restricts the domain of F,
    a function that takes a single argument x.
    If "x is not between LOW_D and HIGH_D (inclusive),
    it returns -Infinity, but otherwise returns F(x).

    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    >>> f(100)
    10.0
    """

    def wrapper_method_name(x):
        if x >= low_d and x <= high_d:
            return f(x)
        return float("-inf")

    return wrapper_method_name


"""
(b) (5.0 points) restrict_range

Implement restrict_range, a function that accepts three parameters
(f, low_r, high_r) and returns a higher-order function that returns the same
thing as f when that result is between low_r and high_r (inclusive),
and otherwise returns float("-inf").
"""


def restrict_range(f, low_r, high_r):
    """Returns a function that restricts the range of F, a function
    that takes a single argument X. If the return value of F(X)
    is not between LOW_R and HIGH_R (inclusive), it returns -Infinity,
    but otherwise returns F(X).

    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """

    def wrapper_method_name(x):
        tmp = f(x)
        if tmp >= low_r and tmp <= high_r:
            return tmp
        return float("-inf")

    return wrapper_method_name


"""
(c) (1.0 points) restrict_both

Now that you have those two functions defined, you’ll implement restrict_both, a higher-order function
that accepts a function f and four numeric arguments (low_d, high_d, low_r, high_r) and returns the
result of applying both restrict_domain and restrict_range on f.
"""


def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to (LOW_D, HIGH_D)
    and a range restricted to (LOW_R, HIGH_R).

    >>> diva = lambda x: (10000 // x) * 9
    >>> f = restrict_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """
    return restrict_range(restrict_domain(f, low_d, high_d), low_r, high_r)
