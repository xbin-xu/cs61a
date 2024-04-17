# 1. (8.0 points) What Would Python Display?
"""
Assume the following code has been executed already.
"""
one = 1


def choose(one):
    if big(one):
        print('A')
    if huge(one):
        print('B')
    elif big(one) or huge(one):
        print('C')
    if big(one) or print('D'):
        print('E')
    else:
        print('F')


big = lambda x: x >= one
huge = lambda x: x > one


def which():
    one = 3

    def this():
        return one
        return one + 1

    return this
    one = 4


choose(one + one)  # A, B, E
print(which()())  # 3


# 2. (8.0 points) Silence of the Lambda
"""
Complete the environment diagram below and then answer the questions that
follow. There is one question for each labeled blank in the diagram.
The blanks with no labels have no questions associated with them and are
not scored. If a blank contains an arrow to a function, write the function
as it would appear in the diagram.

Global frame
    r -> func f(f) [parent=Global]
    n -> 10
    # g -> func lambda(n) [parent=Global]
    g -> func lambda(k) [parent=f1]
f1: lambda<line 6> [parent=Global]
    n -> -1
    Return Value -> func lambda(k) [parent=f1] <----+
f2: r [parent=Global]                               |
    f ----------------------------------------------+
    k -> 2 -> 3
    m -> None
    Return Value -> 10
f3: lambda<line 6> [parent=f1]
    k -> 2
    Return Value -> None
"""


def r(f):
    k = 2
    k, m = k + 1, f(k)
    return n


n = 10
g = (lambda n: lambda k: print(k * n))(-1)
r(g)  # print -2


# 3. (8.0 points) Nearly Square
"""
Implement near_square, which takes positive integer n and non-negative
integer k. It returns the largest integer less than or equal to n which
is the product of two positive integers that differ by k or less.
You may use solve, which is provided.
"""


def near_square(n, k):
    """Return the largest integer that is less than or equal to n and
    equals a * b for some positive integers a and b where abs(a - b) <= k.

    >>> near_square(125, 0) # 11 * 11 = 121 and abs(11 - 11) = 0
    121
    >>> near_square(120, 3) # 10 * 12 = 120 and abs(10 - 12) = 2
    120
    >>> near_square(120, 1) # 10 * 11 = 110 and abs(10 - 11) = 1
    110
    """
    while True:
        gap = k
        while gap >= 0:
            x = solve(gap, n)
            if x == round(x):  # Check if x is a whole number
                return n
            gap = gap - 1
        n = n - 1


def solve(b, c):
    """Returns the largest x for which x * (x + b) = c

    >>> solve(2, 120) # x=10 solves x * (x + 2) = 120
    10.0
    >>> solve(2, 121) # x=10.045... solves x * (x + 2) = 121
    10.045361017187261
    """
    return (b * b / 4 + c) ** 0.5 - b / 2


# 4. (16.0 points) Nice Dice
"""
A dice integer is a positive integer whose digits are all greater than or
equal to 1 and all less than or equal to 6.
"""


def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.

    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322) # 2 and 3 are different digits.
    False
    >>> streak(99999) # 9 is not allowed in a dice integer.
    False
    """
    d = n % 10
    if d < 1 or d > 6:
        return False
    while n:
        # if n >= 10 and n % 10 != n // 10 % 10:
        if d != n % 10:
            return False
        n = n // 10
    return True


def changes(n):
    """Return the number of adjacent digits that are different in dice number n.

    >>> changes(22222)
    0
    >>> changes(222255)
    1
    >>> changes(22322)
    2
    >>> changes(22366666622)
    3
    >>> changes(52431)
    4
    """
    count = 0
    while n >= 10:
        if n % 10 != (n // 10) % 10:
            count = count + 1
        n = n // 10
    return count


def count_if(f):
    """Return a function that takes a positive integer n and returns
    the count of its digits for which f returns a true value.

    >>> is_three = lambda d: d == 3
    >>> count_threes = count_if(is_three) # count_threes returns the number of threes in n
    >>> count_threes(431663334231)        # 3 appears 5 times
    5
    """

    def g(n):
        count = 0
        while n:
            if f(n % 10):
                count += 1
            n = n // 10
        return count

    return g


def count_at_least(k):
    """Return a function that returns how many of the digits of its argument are at least k.

    >>> above_3 = count_at_least(3) # above_3 returns the # of digits greater than or equal to 3
    >>> above_3(431663334231)
    9
    """
    return count_if(lambda d: d >= k)


def times(k, n, d):
    """Returns whether n contains digit d exactly k times.

    >>> times(3, 6132344561, 4)     # 4 only appears 2 times
    False
    >>> times(3, 61323445614, 4)    # 4 appears exactly 3 times
    True
    """
    return count_if(lambda x: x == d)(n) == k


def streak(n):
    """Return whether positive n is a dice integer in which all the digits are the same.

    >>> streak(22222)
    True
    >>> streak(4)
    True
    >>> streak(22322) # 2 and 3 are different digits.
    False
    >>> streak(99999) # 9 is not allowed in a dice integer.
    False
    """
    return count_if(lambda x: x > 0 and x < 7 and x == n % 10)(n) == count_if(
        lambda x: True
    )(n)
    # return (
    #     count_if(lambda x: x == 1)(n) == count_if(lambda x: True)(n)
    #     or count_if(lambda x: x == 2)(n) == count_if(lambda x: True)(n)
    #     or count_if(lambda x: x == 3)(n) == count_if(lambda x: True)(n)
    #     or count_if(lambda x: x == 4)(n) == count_if(lambda x: True)(n)
    #     or count_if(lambda x: x == 5)(n) == count_if(lambda x: True)(n)
    #     or count_if(lambda x: x == 6)(n) == count_if(lambda x: True)(n)
    # )
