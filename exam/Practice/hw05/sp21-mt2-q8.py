"""
8. (7.0 points) The Tree of L-I-F-E

Implement word_finder, a generator function that yields each word that can be
formed by following a path in a tree from the root to a leaf, where the words
are specified in a list. When given the tree shown in the diagram below and a
word list that includes ‘SO’ and ‘SAW’, the function should first yield ‘SO’
and then yield ‘SAW’.

      'S'
 /     |    \\
'O'   'A'   'C'
      / \\   |
    'Q' 'W' 'H'

Please read through the function header and doctests below.
We have provided quite a few doctests to test different situations and
demonstrate how the function should work.
You can always call draw(t) on a particular tree object on code.cs61a.org
to help you visualize its structure and understand the results of a doctest.

(a) Here is a skeleton of a correct solution:

def word_finder(letter_tree, words_list):
    def _________(____):
        _______________ # Optional
        if ____________:
            yield ______________
        for ___________:
            yield from _________
    yield from __________

We highly encourage you to follow the skeleton.
You may diverge from the skeleton if your approach is correct and passes
the doctests, but a non-working solution that doesn’t follow the skeleton
will not receive partial credit.

A correct solution should not first find all the words and then yield them;
it should instead yield whenever it finds a new word.
Your solution may receive 0 points if it pre-computes the words.
Your function should use the standard CS61A Tree definition,
viewable here: code.cs61a.org/tree_class Please use code.cs61a.org
to try out your code. You can then paste the code here.
"""


def word_finder(letter_tree, words_list):
    """Generates each word that can be formed by following a path
    in TREE_OF_LETTERS from the root to a leaf,
    where WORDS_LIST is a list of allowed words (with no duplicates).

    # Case 1: 2 words found
    >>> words = ['SO', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree("W")]), Tree("C", [Tree("H")])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> next(gen)
    'SAW'
    >>> list(word_finder(t, words))
    ['SO', 'SAW']

    # Case 2: No words found
    >>> t = Tree("S", [Tree("I"), Tree("A", [Tree("Q"), Tree("E")]), Tree("C", [Tree("H")])])
    >>> list(word_finder(t, words))
    []

    # Case 3: Same word twice
    >>> t = Tree("S", [Tree("O"), Tree("O")] )
    >>> list(word_finder(t, words))
    ['SO', 'SO']

    # Case 4: Words that start the same
    >>> words = ['TAB', 'TAR', 'BAT', 'BAR', 'RAT']
    >>> t = Tree("T", [Tree("A", [Tree("R"), Tree("B")])])
    >>> list(word_finder(t, words))
    ['TAR', 'TAB']

    # Case 5: Single letter words
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A")
    >>> list(word_finder(t, words))
    ['A']

    # Case 6: Words end in leaf
    >>> words = ['A', 'AN', 'AH']
    >>> t = Tree("A", [Tree("H"), Tree("N")])
    >>> list(word_finder(t, words))
    ['AH', 'AN']

    # Case 7: Words start at root
    >>> words = ['GO', 'BEARS', 'GOB', 'EARS']
    >>> t = Tree("B", [Tree("E", [Tree("A", [Tree("R", [Tree("S")])])])])
    >>> list(word_finder(t, words))
    ['BEARS']

    ## Case 8: This special test ensures that your solution does *not*
    # pre-compute all the words before yielding the first one.
    # If done correctly, your solution should error only when it
    # tries to find the second word in this tree.
    >>> words = ['SO', 'SAM', 'SAT', 'SAME', 'SAW', 'SOW']
    >>> t = Tree("S", [Tree("O"), Tree("A", [Tree("Q"), Tree(1)]), Tree("C", [Tree(1)])])
    >>> gen = word_finder(t, words)
    >>> next(gen)
    'SO'
    >>> try:
    ...     next(gen)
    ... except TypeError:
    ...     print("Got a TypeError!")
    ... else:
    ...     print("Expected a TypeError!")
    Got a TypeError!
    """
