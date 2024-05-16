"""
8. (21.0 points) CS 61A Presents The Game of Hoop.

When we introduced the Hog project to you, we designed the rules of the game
in a way that would make it possible to implement without using more advanced
concepts like OOP and iterators/generators.
Now that we’ve learned these concepts, you can rewrite parts of the game and
expand it! The new version, called Hoop, will support any number of players
greater than or equal to 2. Assume the following changes from Hog:

• All rules have been taken out except for the Sow Sad rule,
which is reiterated below.
• Each player’s strategy is a function strategy(own_score, other_scores) that
takes in that player’s score and a list of the other players’ scores,
and outputs the number of times that player wishes to roll the dice during
their turn. Order doesn’t matter for the list of other players’ scores.
• You don’t have to keep track of the leader, and there is no commentary
mechanism.

Sow Sad: If a player rolls any number of 1s in their turn, their score for that
set of rolls is a 1 regardless of whatever else they rolled.
"""


class HoopPlayer:
    def __init__(self, strategy):
        """Initialize a player with STRATEGY, and a starting SCORE of 0. The
        STRATEGY should be a function that takes this player's score and a list
        of other players' scores.
        """
        self.strategy = strategy
        self.score = 0


class HoopDice:
    def __init__(self, values):
        """Initialize a dice with possible values VALUES, and a starting INDEX
        of 0. The INDEX indicates which value from VALUES to return when the
        dice is rolled next.
        """
        self.values = values
        self.index = 0

    def roll(self):
        """Roll this dice. Advance the index to the next step before returning."""
        value = ______________
        ______________ = (______________) % ______________
        return value


class HoopGame:
    def __init__(self, players, dice, goal):
        """Initialize a game with a list of PLAYERS, which contains at least one
        HoopPlayer, a single HoopDice DICE, and a goal score of GOAL.
        """
        self.players = players
        self.dice = dice
        self.goal = goal

    def next_player(self):
        """Infinitely yields the next player in the game, in order."""
        yield from ______________
        yield from ______________

    def get_scores(self):
        """Collects and returns a list of the current scores for all players
        in the same order as the SELF.PLAYERS list.
        """
        # Implementation omitted. Assume this method works correctly.

    def get_scores_except(self, player):
        """Collects and returns a list of the current scores for all players
        except PLAYER.
        """
        return [______________ for pl in ______________ if ______________]

    def roll_dice(self, num_rolls):
        """Simulate rolling SELF.DICE exactly NUM_ROLLS > 0 times. Return sum of
        the outcomes unless any of the outcomes is 1. In that case, return 1.
        """
        outcomes = [______________ for x in ______________]
        ones = [______________ for outcome in outcomes]
        return 1 if ______________(ones) else ______________(outcomes)

    def play(self):
        """Play the game while no player has reached or exceeded the goal score.
        After the game ends, return all players' scores.
        """
        player_gen = self.next_player()
        while max(self.get_scores()) < self.goal:
            player = ______________(player_gen)
            other_scores = self.get_scores_except(player)
            num_rolls = ______________(player.score, other_scores)
            outcome = self.roll_dice(num_rolls)
            ______________ += outcome
        return self.get_scores()
