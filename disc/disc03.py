# Q1: Swipe
def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10)
        print(n % 10)


# Q2: Skip Factorial
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 1:
        return 1
    else:
        return n * skip_factorial(n - 2)


# Q3: Is Prime
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

    def divisor(i):
        if i == n:
            return True
        return n % i != 0 and divisor(i + 1)

    return divisor(2)


# Q4: Recursive Hailstone
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)


def even(n):
    return hailstone(n // 2) + 1


def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    return hailstone(3 * n + 1) + 1


# Q5: Sevens
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        elif who < 1:
            who = k
        return f(i + 1, who, direction)

    return f(1, 1, 1)


def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)


# Q6: Karel the Robot
# https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
"""
# write any code you want
from karel.stanfordkarel import *

def turn_around():
   turn_left()
   turn_left()

def goto_center():
   if front_is_clear():
      move()
      if front_is_clear():
         move()
      goto_center()
      if front_is_blocked():
         turn_around()
      move()

def main():
   # your code here...
   goto_center()
"""
