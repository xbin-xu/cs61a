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


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.

    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3 4 0 1 2 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3 4 0 8 2 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        return replace(s.rest, t, i - 1, j - 1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
    end = t
    while end.rest is not Link.empty:
        end = end.rest
    s.rest, end.rest = t, s.rest
