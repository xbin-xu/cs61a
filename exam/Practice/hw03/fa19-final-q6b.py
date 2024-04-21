"""
6. (20 points) Palindromes
Definition. A palindrome is a sequence that has the same elements in
normal and reverse order.

(b) (4 pt) Implement contains, which takes non-negative integers a and b.
It returns whether all of the digits of a also appear in order among the
digits of b.
Important: You may not write str, repr, list, tuple, [, or ].
"""


def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.

    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains(a // 10, b // 10)
    else:
        return contains(a, b // 10)
