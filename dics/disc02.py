# Q1: Warm Up
"""
What is the value of result after executing
result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)?
Talk about it with your whole group and make sure
you all agree before anybody presses Check Answer.
"""

result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)
assert result == 30

# Draw an environment diagram
"""
Global frame
    team  ------------------------------.
[x] team  -> func team(work) <------.   |
    dream -> func dream(work, s)    |   |
    work  -> 3                      |   |
    t     -> func abs(...)   <------|---.
f1: dream [parent=Global frame]     |
    work  --------------------------.
    s     -> 4
    t     -> False
    Retrun Value -> True
f2: team [parent=Global frame]
    work  -> 2
    Return Value -> 1

Notes: To evaluatethe expression `<left> and <right>`:
1. Evaluate the subexpression <left>.
2. If the result is a false value v, then the expression evaluates to v.
3. Otherwise, the expression evaluates to the value of the subexpression <right>.

so, `and` and `or` will return <left> or <right> not True or False
"""


# Q2: Make Keeper
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"

    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1

    return f


# Q3: Digit Finder
def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"
    return lambda n: (n // pow(10, k - 1)) % 10

    # def f(n):
    #     """
    #     Diagnostics:
    #     1. "k" 可能未绑定 [reportUnboundVariable]
    #     2. Local variable `k` referenced before assignment [F823]
    #     """
    #     # while n > 0 and k > 0:
    #     #     n, k = n // 10, k - 1
    #
    #     cnt = 0
    #     while n > 0 and cnt < k - 1:
    #         n, cnt = n // 10, cnt + 1
    #     return n % 10
    #
    # return f


# Q4: Match Maker
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """

    def check(x):
        while x // (10**k) > 0:
            # if x // (10**k) % 10 != x % (10**k) % 10:
            if x // (10**k) % 10 != x % 10:
                return False
            x //= 10
        return True

    return check
