"""
4. Maximum Exponen-tree-ation

(a) For a list of integers values, define the maximum exponentiation of values
to be the largest single number that can be achieved by repeatedly combining
pairs of consecutive elements from values through exponentiation.
Two possible exponentiations for the list [3, 1, 2, 3] are shown below:

(3 ** 1) ** (2 ** 3) = 6561
(3 ** (1 ** 2)) ** 3 = 27

Of all the exponentiations of [3, 1, 2, 3], the maximum exponentiation is 6561,
which can be calculated through the below steps:

[3, 1, 2, 3]
[3 ** 1, 2, 3]
[3, 2, 3]
[3, 2 ** 3]
[3, 8]
[3 ** 8]
6561

Implement exp_tree, which accepts a non-empty list of integers values and
returns a tree whose label is the maximum exponentiation of values.
Given that the maximum exponentiation is b ** n for some two integers b and n,
the two branches of this tree should be the exp_trees of the sublists of values
used to exponentiate to b and n, respectively.
You may assume that values has a unique exponentiation tree.
For example, below is a drawing of the exp_tree for values = [3, 1, 2, 3]:

  6551
 3    8
3 1  2 3

The function should assume the standard CS61A Tree ADT definition,
which is already loaded into
code.cs61a.org, and is viewable here: code.cs61a.org/tree_adt
Note: Exponentials in Python are expressed as base ** exponent.
"""


def exp_tree(values):
    """
    Returns the exponential tree that can be made from VALUES
    with the greatest possible root label
    >>> print_tree(exp_tree([5]))
    5
    >>> print_tree(exp_tree([3, 2]))
    9
      3
      2
    >>> print_tree(exp_tree([2, 3, 2]))
    512
      2
      9
        3
        2
    >>> lst = [3, 1, 2, 3]
    >>> print_tree(exp_tree(lst))
    6561
      3
        3
        1
      8
        2
        3
    """
    if __________:  # (a)
        return __________  # (b)
    else:

        def tree_at_split(i):
            base = exp_tree(__________)  # (c)
            exponent = exp_tree(__________)  # (d)
            return tree(__________, [base, exponent])  # (e)
            trees = [tree_at_split(i) for i in range(1, len(values))]

        return max(trees, key=__________)  # (f)
