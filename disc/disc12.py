class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


"""
Q1: Word Rope

Definition: A rope in Python is a list containing only one-letter strings
except for the last element, which may either be a one-letter string or a rope.
Implement word_rope, a Python function that takes a non-empty string s
containing only letters and spaces that does not start or end with a space.
It returns a rope containing the letters of s in which each word is in a
separate list.

Important: You may not use slicing or the split, find, or index methods of a
string. Solve the problem using list operations.

Reminder: s[-1] evaluates to the last element of a sequence s.
"""


def word_rope(s):
    """Return a rope of the words in string s.

    >>> word_rope('the last week')
    ['t', 'h', 'e', ['l', 'a', 's', 't', ['w', 'e', 'e', 'k']]]
    """
    assert s and s[0] != ' ' and s[-1] != []
    result = []
    word = _____
    for x in s:
        if x == ' ':
            "*** YOUR CODE HERE ***"
        else:
            "*** YOUR CODE HERE ***"
    return result


"""
Q2: Linear Sublists

Definition: A sublist of linked list s is a linked list of some of the elements
of s in order.
For example, <3 6 2 5 1 7> has sublists <3 2 1> and <6 2 7> but not <5 6 7>.

Definition: A linear sublist of a linked list of numbers s is a sublist
in which the difference between adjacent numbers is always the same.
For example <2 4 6 8> is a linear sublist of <1 2 3 4 6 9 1 8 5>
because the difference between each pair of adjacent elements is 2.

Implement linear which takes a linked list of numbers s
(either a Link instance or Link.empty).
It returns the longest linear sublist of s.
If two linear sublists are tied for the longest, return either one.
"""


def linear(s):
    """
    Return the longest linear sublist of a linked list s.

    >>> s = Link(9, Link(4, Link(6, Link(7, Link(8, Link(10))))))
    >>> linear(s)
    Link(4, Link(6, Link(8, Link(10))))
    >>> linear(Link(4, Link(5, s)))
    Link(4, Link(5, Link(6, Link(7, Link(8)))))
    >>> linear(Link(4, Link(5, Link(4, Link(7, Link(3, Link(2, Link(8))))))))
    Link(5, Link(4, Link(3, Link(2))))
    """

    def complete(first, rest):
        "The longest linear sublist of Link(first, rest) with difference d."
        if rest is Link.empty:
            return ____
        elif ____ == d:
            return Link(____, complete(____, ____))
        else:
            return complete(first, rest.rest)

    if s is Link.empty:
        return s

    longest = Link(s.first)  # The longest linear sublist found so far
    while s is not Link.empty:
        t = s.rest
        while t is not Link.empty:
            d = t.first - s.first
            candidate = ____
            if length(candidate) > length(longest):
                longest = candidate
            t = t.rest
        s = s.rest
    return longest


def length(s):
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)
