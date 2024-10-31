"""
7. (5 points) Version 2.0

Implement the Version, Insert, and Delete classes as follows:

• A Version represents a string that has been edited.
A Version instance has a previous value (which may be a str or Version instance)
and an edit (which may be an instance of Insert or Delete).
• Calling str on a Version instance should return the string that results from
applying its edit to the string represented by previous. Assume that string is
long enough to perform the edit.
• An edit object represents a change to a string parameterized by
some value c applied at an index i.
• The apply method for Insert inserts the string c into string t
starting at index i.
• The apply method for Delete removes c (a positive int) characters
from string t starting at index i.
"""


class Version:
    """A version of a string after an edit.

    >>> s = Version('No power?', Delete(3, 6))
    >>> print(Version(s, Insert(3, 'class!')))
    No class!
    >>> t = Version('Beary', Insert(4, 'kele'))
    >>> print(t)
    Bearkeley
    >>> print(Version(t, Delete(2, 1)))
    Berkeley
    >>> print(Version(t, Delete(4, 5)))
    Bear
    """

    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit

    def __str__(self):
        return self.edit.apply(self.previous.__str__())


class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c


class Insert(Edit):
    def apply(self, t):
        """Return a new string by inserting string c into t starting at position i."""
        return t[: self.i] + self.c + t[self.i :]


class Delete(Edit):
    def apply(self, t):
        """Return a new string by deleting c characters from t starting at position i."""
        return t[: self.i] + t[self.i + self.c :]
