"""
5. (6 points) Won’t You Be My Neighbor?

(a) (4 pt) Write repeat_digits, which takes a positive integer n and
returns another integer that is identical to n but with each digit repeated.
"""


def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.

    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if rest == 0:
        return last * 10 + last
    return repeat_digits(rest) * 100 + last * 10 + last
