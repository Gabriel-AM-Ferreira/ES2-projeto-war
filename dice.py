from random import randint


class Dice:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def roll_many(self, num_rolls):
        """Return a list of num_rolls random values between 1 and number of sides."""
        return [self.roll() for _ in range(num_rolls)]

        