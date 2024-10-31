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
        """Roll this dice. Advance the index to the next step before returning.
        >>> five_six = HoopDice([5, 6])
        >>> five_six.roll()
        5
        >>> five_six.index
        1
        >>> five_six.roll()
        6
        >>> five_six.index
        0
        """
        value = self.values[self.index]
        self.index = (self.index + 1) % len(self.values)
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
        """Infinitely yields the next player in the game, in order.
        >>> player_gen = game.next_player()
        >>> next(player_gen) is player1
        True
        >>> next(player_gen) is player3
        False
        >>> next(player_gen) is player3
        True
        >>> next(player_gen) is player1
        True
        >>> next(player_gen) is player2
        True
        >>> new_player_gen = game.next_player()
        >>> next(new_player_gen) is player1
        True
        >>> next(player_gen) is player3
        True
        """
        yield from self.players.__iter__()
        yield from self.next_player()

    def get_scores(self):
        """Collects and returns a list of the current scores for all players
        in the same order as the SELF.PLAYERS list.
        """
        # Implementation omitted. Assume this method works correctly.
        return [pl.score for pl in self.players]

    def get_scores_except(self, player):
        """Collects and returns a list of the current scores for all players
        except PLAYER.
        >>> game.get_scores_except(player2)
        [0, 0]
        """
        return [pl.score for pl in self.players if pl != player]

    def roll_dice(self, num_rolls):
        """Simulate rolling SELF.DICE exactly NUM_ROLLS > 0 times. Return sum of
        the outcomes unless any of the outcomes is 1. In that case, return 1.
        >>> game.roll_dice(4)
        20
        """
        outcomes = [self.dice.roll() for x in range(num_rolls)]
        ones = [outcome == 1 for outcome in outcomes]
        return 1 if any(ones) else sum(outcomes)

    def play(self):
        """Play the game while no player has reached or exceeded the goal score.
        After the game ends, return all players' scores.
        >>> game.play()
        [20, 10, 60]
        """
        player_gen = self.next_player()
        while max(self.get_scores()) < self.goal:
            player = next(player_gen)
            other_scores = self.get_scores_except(player)
            num_rolls = player.strategy(player.score, other_scores)
            outcome = self.roll_dice(num_rolls)
            player.score += outcome
        return self.get_scores()


class BrokenHoopDice(HoopDice):
    def __init__(self, values, when_broken):
        super().__init__(values)
        self.when_broken = when_broken
        self.is_broken = False

    def roll(self):
        """
        >>> broken = BrokenHoopDice([5, 6, 7], 11)
        >>> broken.roll()
        5
        >>> [broken.roll() for _ in range(6)]
        [11, 6, 11, 7, 11, 5]
        """
        if self.is_broken:
            self.is_broken = not self.is_broken
            return self.when_broken
        else:
            self.is_broken = not self.is_broken
            return super().roll()


roll_once_strategy = lambda pl, ops: 1
roll_twice_strategy = lambda pl, ops: 2
always_5 = HoopDice([5])
player1 = HoopPlayer(roll_twice_strategy)
player2 = HoopPlayer(roll_once_strategy)
player3 = HoopPlayer(lambda pl, ops: 6)
game = HoopGame([player1, player2, player3], always_5, 55)
# since we omit the implementation of HoopGame.get_scores, here's what it
# should output:
game.get_scores()
