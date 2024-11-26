import random

class ActionSpace:
    def sample(self):
        """
        Chooses randomly between 0 (Sell), 1 (Hold), 2 (Buy) for action.

        Returns:
            int: Action as int
        """
        return random.choice([0, 1, 2])