"""
6. (4 points) Dr. Frankenlink
Implement replace, which takes two non-empty linked lists s and t,
as well as positive integers i and j with i < j.
It mutates s by removing elements with indices from i to j
(removing element i but not removing element j) and replacing them with t.
Afterward, s contains all of the objects in t, so a change to t would be
reflected in s as well.
t may change as a result of calling replace. Assume s has at least j elements.
"""


def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.

    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        _________________________________________________________________________________
    else:
        for k in range(j - i):
            _______________ = (___________________________________________________________)
    end = t
    while ___________________________________________________________________________:
        end = end.rest
    s.rest, end.rest = ______________________________, ______________________________
