"""
9. (8 points) Temmie Flakes (It’s just torn up pieces of construction paper.)

Implement count_ways, which takes a tree t and an integer total and returns the
number of ways any top-to- bottom sequence of consecutive nodes can sum to total.
Shown below with bolded edges are the four ways counted during count_ways(t1, 7).
The tree data abstraction is on the previous page.
"""


def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.

    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
    ...                        tree(1, [tree(4, [tree(2, [tree(2)])])])]),
    ...               tree(3, [tree(2, [tree(2),
    ...                                 tree(3)])]),
    ...               tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ...               tree(1, [tree(1),
    ...                        tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """

    def paths(__________________________________):
        ways = 0
        if _____________________________________:
            ____________________________________
        ways += sum(
            ____________________________________________________________________________
        )
        if _____________________________________:
            ____________________________________________________________________________________
        return ways

    return _____________________________________________________________________
