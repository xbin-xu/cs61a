"""
3. (12.0 points) Sparse Lists

The most_common function returns the most common element in a non-empty list.
You do not need to implement this function.
Assume that it is implemented for you.

Implement the SparseList class.
A SparseList instance represents a non-empty list s.
• Its common attribute is the most common value in s.
• Its others dictionary has a value for every element in s that is not common.
The corresponding key is the index for that value in s.
• Its item method takes a non-negative integer i and returns s[i] or
the string 'out of range' if i is not smaller than the length of s.
• Its items method returns a list with the same elements as s in the
same order as s.
"""


def most_common(s):
    """Return the most common element in non-empty list s. In case of a tie,
    return the most common element that appears first in s.

    >>> most_common([3, 1, 4, 1, 5, 9])
    1
    >>> most_common([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    5
    >>> most_common([2, 7, 1, 8, 2, 8, 1, 8, 2, 8])
    8
    >>> most_common([3, 5, 7, 7, 7, 5, 5])
    5
    >>> most_common([3, 7, 5, 5, 7, 7])
    7
    """


class SparseList:
    """Represent a non-empty list as a most common value and a dictionary from
    indices to values that contains only values that are not the most common.

    >>> pi = SparseList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> pi.common
    5
    >>> pi.others
    {0: 3, 1: 1, 2: 4, 3: 1, 5: 9, 6: 2, 7: 6, 9: 3}
    >>> [pi.item(0), pi.item(1), pi.item(2), pi.item(3), pi.item(4)]
    [3, 1, 4, 1, 5]
    >>> pi.item(10)
    5
    >>> pi.item(11)
    'out of range'
    >>> pi.items()
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    """

    def __init__(self, s):
        assert s, 's cannot be empty'
        self.n = len(s)
        self.common = most_common(_________)
        self.others = {_________: _________ for i in range(_________) if _________}

    def item(self, i):
        """Return s[i] or 'out of range' if i is not smaller than the length of s."""
        assert i >= 0, 'index i must be non-negative'
        if _________:
            return 'out of range'
        elif _________:
            return _________
        else:
            return self.common

    def items(self):
        """Return a list with the same elements as s in the same order as s."""
        return [_________ for i in _________]
