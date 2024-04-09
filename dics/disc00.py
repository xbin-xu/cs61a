def f(x):
    """Subtracts one from an interger `x`"""
    return x - 1


def g(x):
    """Doubles an interger `x`"""
    return x * 2


def h(x, y):
    """Concatenates the digits of two different positive intergers `x` and `y`

    >>> h(789, 12)
    78912
    >>> h(12, 789)
    12789
    """
    assert x > 0 and y > 0, "requre two positive intergers"
    return int(str(x) + str(y))


# Definition: A small expression is a call expression that contains only
# f, g, h, the number 5, and parentheses. All of these can be repeated.
# For example, h(g(5), f(f(5))) is a small expression that evaluates to 103.
# assert 103 == h(g(5), f(f(5)))

# 20+24: 5->10->20 + 5->4->3->6->12->24
assert 2024 == h(g(g(5)), g(g(g(f(f(5))))))
# 20+2+4: 5->10->20 + 5->4->3->2 + 5->4
assert 2024 == h(g(g(5)), h(f(f(f(5))), f(5)))
