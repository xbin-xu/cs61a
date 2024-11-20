"""
5. (4 points) Insert

Fill in the following function to fulfill its comment.
The linked-list interface that you should use is given on page ??.
Warning: this problem deals with linked lists, NOT Python lists or tuples.
You cannot use +, len(), indexing (L[k]), or list construction ([...]).
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


def print_link(lnklst):
    string = '('
    while lnklst.rest is not Link.empty:
        string += str(lnklst.first) + ', '
        lnklst = lnklst.rest
    string += str(lnklst.first) + ')'
    print(string)


def link_insert(lnklst, value, before):
    """Return a linked list identical to LNKLST, but with VALUE inserted just
    before the first occurrence of BEFORE in the list, if any.
    The returned list is identical to LNKLST if BEFORE does not occur in LNKLST.
    The operation is non-destructive.

    >>> L = Link(2, Link(3, Link(7, Link(1))))
    >>> print_link(L)
    (2, 3, 7, 1)
    >>> Q = link_insert(L, 19, 7)
    >>> print_link(Q)
    (2, 3, 19, 7, 1)
    >>> print_link(link_insert(L, 19, 20))
    (2, 3, 7, 1)
    >>> L2 = Link(2, Link(3, Link(7, Link(2))))
    >>> print_link(L2)
    (2, 3, 7, 2)
    >>> Q2 = link_insert(L2, 19, 2)
    >>> print_link(Q2)
    (19, 2, 3, 7, 2)
    """
    if lnklst.rest is Link.empty:
        return Link(lnklst.first)
    elif lnklst.first != before:
        return Link(lnklst.first, link_insert(lnklst.rest, value, before))
    else:
        return Link(value, link_insert(lnklst, value, None))
