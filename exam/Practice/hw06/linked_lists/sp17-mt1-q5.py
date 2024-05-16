"""
5. (4 points) Insert

Fill in the following function to fulfill its comment.
The linked-list interface that you should use is given on page ??.
Warning: this problem deals with linked lists, NOT Python lists or tuples.
You cannot use +, len(), indexing (L[k]), or list construction ([...]).
"""

def link_insert(lnklst, value, before):
    """Return a linked list identical to LNKLST, but with VALUE inserted just
    before the first occurrence of BEFORE in the list, if any.
    The returned
    list is identical to LNKLST if BEFORE does not occur in LNKLST.
    The operation is non-destructive.

    >>> L = link(2, link(3, link(7, link(1))))
    >>> print_link(L)
    (2, 3, 7, 1)
    >>> Q = link_insert(L, 19, 7)
    >>> print_link(Q)
    (2, 3, 19, 7, 1)
    >>> print_link(link_insert(L, 19, 20))
    (2, 3, 7, 1)
    """
    if _________________________________________________________________:
        return _________________________________________________________
    elif _______________________________________________________________:
        return _________________________________________________________
    else:
        return _________________________________________________________
