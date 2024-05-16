"""
3. (21.0 points) College Party

In a US presidential election, each state has a number of electors.
Definition: For some collection of states s, a win by at least k is a
(possibly empty) subset w of s such that the total number of electors for
the states in w is at least k more than the total number of electors for
the states not in w but in s.
For example, in the battleground states below, Arizona (AZ), Pennsylvania (PA),
and Michigan (MI) have a total of 11 + 20 + 16 = 47 electors.
The remaining states have a total of 6 + 16 + 10 = 32 electors.
So, the subset <AZ PA MI> is a win by 47 - 32 = 15.

"""
class State:
    electors = {}
    def __init__(self, code, electors):
        self.code = code
        self.electors = electors
        State.electors[code] = electors

battleground = [State('AZ', 11), State('PA', 20), State('NV', 6),
                State('GA', 16), State('WI', 10), State('MI', 16)]

def print_all(s):
    for x in s:
        print(x)

"""
(a) (8.0 points)

Implement wins, a generator function that takes a list of State instances
states and an integer k. For every possible win by at least k among the states,
it yields a linked list containing strings of the two-letter codes for
the states in that win.
Any order of the wins and any order of the states within a win is acceptable.
A linked list is a Link instance or Link.empty. The Link class appears on the Midterm 2 Study Guide.
"""
def wins(states, k):
    """Yield each linked list of two-letter state codes that describes a win by at least k.
    >>> print_all(wins(battleground, 50))
    <AZ PA NV GA WI MI>
    <AZ PA NV GA MI>
    <AZ PA GA WI MI>
    <PA NV GA WI MI>
    >>> print_all(wins(battleground, 75))
    <AZ PA NV GA WI MI>
    """
    if _________:
        yield Link.empty
    if states:
        first = states[0].electors
        for win in wins(states[1:], _________):
            yield Link(_________, win)
        yield from wins(states[1:], _________)


"""
(b) (7.0 points)

Implement must_win, which takes a list of State instances states
and an integer k. It returns a list of two-letter state codes (strings)
for all states that appear in every win by at least k among the states.
Assume wins is implemented correctly.
"""
def must_win(states, k):
    """List all states that must be won in every scenario that wins by k.

    >>> must_win(battleground, 50)
    ['PA', 'GA', 'MI']
    >>> must_win(battleground, 75)
    ['AZ', 'PA', 'NV', 'GA', 'WI', 'MI']
    """
    def contains(s, x):
        """Return whether x is a value in linked list s."""
        return (_________) and (_________)
    return [_________ for s in states if _________([_________ for w in wins(states, k)])]


"""
(c) (6.0 points)

Definition. A win by at least k is minimal if every state in it is necessary
to win by at least k.
The State class and battleground list are repeated here for convenience.
Assume that only this code has been executed.
You may not call wins or must_win.

Implement is_minimal, which takes a non-empty list of strings
state_codes in which every element is the code for some State instance,
as well as an integer k.
It returns whether the states named in state_codes form a minimal
win by k among all State instances that have ever been constructed.
"""

def is_minimal(state_codes, k):
    """Return whether a non-empty list of state_codes describes a minimal win by
    at least k.

    >>> is_minimal(['AZ', 'NV', 'GA', 'WI'], 0) # Every state is necessary
    True
    >>> is_minimal(['AZ', 'GA', 'WI'], 0)       # Not a win
    False
    >>> is_minimal(['AZ', 'NV', 'PA', 'WI'], 0) # NV is not necessary
    False
    >>> is_minimal(['AZ', 'PA', 'WI'], 0)       # Every state is necessary
    True
    """
    assert state_codes, 'state_codes must not be empty'
    votes_in_favor = _________
    total_possible_votes = sum(_________)

    def win_margin(n):
        """Margin of victory if n votes are in favor and the rest are against."""
        return n - (total_possible_votes - n)

    if win_margin(sum(votes_in_favor)) < k:
        return False # Not a win
    in_favor_no_smallest = _________
    return win_margin(in_favor_no_smallest) < k
