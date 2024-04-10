# Q1: Race
def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    >>> race(2, 3) # Returns the wrong value, the correct value is 8
    15

    race(3, 4)  # Runs forever
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes


# Q2: Fizzbuzz
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1


# Q3: Is Prime?
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    i = 2
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


# Q4: Unique Digits
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i, cnt = 0, 0
    while i < 10:
        i, cnt = i + 1, cnt + has_digit(n, i)
    return cnt


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    >>> has_digit(0, 0)
    True
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    if n == 0 and k == 0:
        return True
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


# Q5: Bottles
"""
Answer the following questions with your group. Step through the diagram to check your answers.

1) What determines how many different frames appear in an environment diagram?

The number of functions defined in the code
The number of call expressions in the code
The number of return statements in the code
The number of times user-defined functions are called when running the code [√]
2) What happens to the return value of pass(bottles)?

It is used as the new value of remaining in the global frame
It is used as the new value of bottles in the global frame
It is used as the new value of pass in the global frame
None of the above
3) What effect does the line bottles = 98 have on the global frame?

It temporarily changes the value bound to bottles in the global frame.
It permanently changes the value bound to bottles in the global frame.
It has no effect on the global frame.                                       [√]
"""
bottles = 99
take = 1


def pass_it(around):
    # bottles is local variable, will not effect global frame's bottles
    bottles = 98
    return take


remaining = bottles - pass_it(bottles)
bottles = remaining

# Q6: Double Trouble
"""
Draw the environment diagram on paper or a whiteboard
(without having the computer draw it for you)!
Then, check your work by stepping through the diagram.
"""


def double(x):
    return x * 2


def triple(x):
    return x * 3


hat = double  # <function double>
double = triple  # <function triple>
