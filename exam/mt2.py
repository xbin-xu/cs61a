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


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()


# 1. (7.0 points) What Would Python Display?
"""
Assume the following code has been executed. The Link class appears on the
midterm 2 study guide (page 2, left side).
Write the output printed for each expression below or Error if an error occurs.
"""


def shake(it):
    if it is not Link.empty and it.rest is not Link.empty:
        if it.first + 1 < it.rest.first:
            it.rest = Link(it.rest.first - 1, it.rest)
            shake(it)
    else:
        shake(it.rest)


it = Link(2, Link(5, Link(7)))
off = Link(1, it.rest)
shake(it)


def cruel(summer):
    while summer is not Link.empty:
        yield summer.first
        summer = summer.rest
        if summer is not Link.empty:
            summer = summer.rest


summer = Link(1, Link(2, Link(3, Link(4))))
# 1.(a)
print(it)  # <2 3 4 5 7>
# 1.(b)
print(off)  # <1 5 7>
# 1.(c)
print([x * x for x in cruel(summer)])  # [1, 9]
# 1.(d) What is the order of growth of the time it takes to evaluate
# shake(Link(1, Link(n))) in terms of n? [exponential/quadratic/linear/constant]
# linear


# 2. (6.0 points) Spin Cycle
"""
Complete the environment diagram below and then answer the questions that
follow. Do not add frames for calls to built-in functions (such as print).

Global frame
    cycle -> func cycle(a) [parent=Global]
    c -> [2, 3] <-------------------+
f1: cycle [parent=Global]           |
    a -> ---------------------------|-------+
    f -> func f(rest) [parent=f1]   |       |
    b -> [4, -----------------------+, 5]   |
    Return Value -> None            |       |
f2: f [parent=f1]                   |       |
    rest -> [4, --------------------+]      |
    Return Value -> [None] <----------------+
"""


def cycle(a):
    def f(rest):
        rest.append(a.pop())
        return [rest.append(a)]

    b = []
    a = f(b)
    b = b + [5]
    print(a)  # [None]
    print(b)  # [4, [2, 3], 5]


c = [2, 3, 4]
cycle(c)
print(c)  # [2, 3]


# 3. (8.0 points) Fearless
"""
If you sing lyrics into a mic, every connected speaker repeats them.
A Mic instance has a dictionary speakers containing Speaker instances as values,
each with its location (str) as its key. Its sing method takes a string lyrics
and invokes the repeat method of each Speaker instance connected to it.

A Speaker takes a transform function that takes and returns a string.
To connect a Speaker instance to m (Mic) in a location (str), add that instance
to the speakers dictionary of m in that location. To repeat a signal s (str),
return the result of calling the speaker’s transform function on s.

Every Mic starts connected to a Speaker in the Front location that repeats the
exact same signal it receives.

Implement the Mic and Speaker classes to match the doctests.
The str.lower and str.upper functions return lowercased and uppercased versions
of a string, respectively.
"""


class Mic:
    """A microphone connected to speakers.
    >>> m = Mic() # Front is connected automatically
    >>> m.sing('Is this thing on?')
    Front - Is this thing on?
    >>> Speaker(str.lower).connect(m, 'Left Side')
    >>> Speaker(str.upper).connect(m, 'Right Side')
    >>> m.sing("You belong with me.")
    Front - You belong with me.
    Left Side - you belong with me.
    Right Side - YOU BELONG WITH ME.
    """

    def __init__(self):
        self.speakers = {"Front": Speaker(lambda s: s)}

    def sing(self, lyrics):
        for k in self.speakers.keys():  # iterate over the keys of a dictionary
            print(k, '-', self.speakers[k].repeat(lyrics))


class Speaker:
    def __init__(self, transform):
        self.transform = transform

    def connect(self, m, location):
        m.speakers[location] = self

    def repeat(self, s):
        return self.transform(s)


# 4. (29.0 points) Who’s counting?
"""
Definition. A strip is a list of integers in which each integer is one more
than the last. For example, [3, 4, 5, 6] is a strip.
Empty and one-element lists are strips
"""

"""
4.(a)
Implement is_strip, which takes a list of integers s and returns
whether it is a strip.
"""


def is_strip(s):
    """Return whether list s is a strip.
    >>> is_strip([3, 4, 5, 6])
    True
    >>> is_strip([3, 3, 3]) # 3 after 3
    False
    >>> is_strip([3, 4, 5, 4, 6]) # 4 after 5
    False
    >>> is_strip([3, 4, 5, 5, 6]) # 5 after 5
    False
    >>> is_strip([3, 4, 5, 6, 8]) # 8 after 6
    False
    >>> is_strip([5])
    True
    >>> is_strip([])
    True
    """
    assert type(s) == list
    return len(s) == 0 or s == list(range(s[0], s[0] + len(s)))


"""
4.(b)
Implement drip, which takes two non-empty lists of integers s and t. It returns
True if there is a strip containing all and only the elements of s and t
starting with s[0] in which the elements of s appear in order and the elements
of t appear in order. It returns False otherwise
"""


def drip(s, t):
    """Return whether there is a strip made out of interleaving s and t.
    >>> drip([1, 3, 5], [2, 4, 6]) # 1 2 3 4 5 6
    True
    >>> drip([1, 4, 5], [2, 3, 6]) # 1 2 3 4 5 6
    True
    >>> drip([1, 2, 3], [4, 5, 6]) # 1 2 3 4 5 6
    True
    >>> drip([2, 4, 5], [1, 3, 6]) # No strip starting with 2 can contain 1
    False
    >>> drip([1, 2, 4, 5], [1, 3, 6]) # No strip can contain 1 and 1
    False
    >>> drip([1, 4, 5], [2, 3, 7]) # No strip can contain 5 and 7 but no 6
    False
    >>> drip([1, 5, 4], [2, 3, 6]) # No strip can contain 5 before 4
    False
    >>> drip([2], [3, 4, 5]) # 2 3 4 5
    True
    >>> drip([1], [2, 3, 5]) # No strip can contain 3 and 5 but no 4
    False
    """
    while s and t:
        if s[0] + 1 == t[0]:
            s, t = t, s[1:]  # The next element of the strip is in t
        elif len(s) >= 2 and s[0] + 1 == s[1]:
            s = s[1:]  # The next element of the strip is in s
        else:
            return False
    return is_strip(s)


"""
4.(c)
Implement longest, which takes a list of integers s. It returns the longest
strip whose elements appear in s in order. If two such strips exist, return
the one that starts earlier in s. Hint: s[-1] is the last element in list s.
"""


def longest(s):
    """Return the longest strip whose elements appear in s in order.
    >>> longest([4, 2, 3, 5, 6, 4, 6, 5]) # 2 3 4 5 is the longest strip in s
    [2, 3, 4, 5]
    >>> longest([4, 2, 3, 5, 6, 4]) # 4 5 6 is as long as 2 3 4 and is earlier
    [4, 5, 6]
    >>> longest([2, 4, 6])
    [2]
    """
    if len(s) == 0:
        return []
    return max([longest_with_s0(s), longest(s[1:])], key=len)


def longest_with_s0(s):
    """Return the longest strip in s that starts with s[0]."""
    result = s[:1]
    for k in s[1:]:
        if k == result[-1] + 1:
            result.append(k)
    return result


"""
4.(d)
Implement has_strip, which takes a Tree of integers t. It returns whether there
is a strip containing the labels along some path from the root to a leaf of t.
The Tree class is on the midterm 2 study guide (page 2 left side).
"""


def has_strip(t):
    """Return whether the elements of some root-to-leaf path form a strip.
    >>> has_strip(Tree(1, [Tree(3, [Tree(4)]), Tree(2, [Tree(2), Tree(3)])])) # 1, 2, 3
    True
    >>> has_strip(Tree(1, [Tree(3, [Tree(4)]), Tree(2, [Tree(2, [Tree(3)])])]))
    False
    >>> has_strip(Tree(1, [Tree(3, [Tree(4)]), Tree(2, [Tree(2)])]))
    False
    >>> has_strip(Tree(1, [Tree(2, [Tree(4)]), Tree(3, [Tree(3)])]))
    False
    """
    if t.is_leaf():
        return True
    for b in t.branches:
        if b.label == t.label + 1 and has_strip(b):
            return True
    return False


"""
4.(e)
Implement strips, a generator function that takes a Tree of integers t.
It yields all strips that contain the labels along a path from the root
to a leaf of t
"""


def strips(t):
    """Yield the paths from the root to a leaf of Tree t that form strips.
    >>> list(strips(Tree(1, [Tree(3, [Tree(4)]), Tree(2, [Tree(2), Tree(3)])])))
    [[1, 2, 3]]
    >>> list(strips(Tree(1, [Tree(2), Tree(2, [Tree(2), Tree(3, [Tree(4)]), Tree(3)])])))
    [[1, 2], [1, 2, 3, 4], [1, 2, 3]]
    """
    if t.is_leaf():
        yield [t.label]
    for b in t.branches:
        if b.label == t.label + 1:
            for s in strips(b):
                yield [t.label] + s

"""
4.(e)  A+ question
Fill in the blank of only_strips, which takes a Tree of integers t.
It removes all nodes that are not on a strip path.
A strip path is a path from the root to a leaf whose labels form a strip.
You may use functions implemented earlier in this question.
"""


def test_only_strips(t):
    """Call only_strips(t) and then return t. Assume has_strip(t) is True.
    >>> test_only_strips(Tree(1, [Tree(2), Tree(2, [Tree(2), Tree(3, [Tree(4)]), Tree(3)])]))
    Tree(1, [Tree(2), Tree(2, [Tree(3, [Tree(4)]), Tree(3)])])
    >>> test_only_strips(Tree(5, [Tree(6), Tree(6, [Tree(7, [Tree(9)])]), Tree(7)]))
    Tree(5, [Tree(6)])
    """
    only_strips(t)
    return t


def only_strips(t):
    """Remove all nodes of Tree t that are not on a path from the root to a leaf
    whose labels form a strip. Assume has_strip(t) is True.
    """
    t.branches = [
        b
        for b in t.branches
        if b.label == t.label + 1 and has_strip(b) and (only_strips(b) or True)
    ]
