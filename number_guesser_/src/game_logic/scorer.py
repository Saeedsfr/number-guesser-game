class Scorer:
    def __init__(self, initial_score=100):
        self.score = initial_score

    def decrement_score(self, penalty=10):
        """Decrement the score by a penalty amount."""
        self.score -= penalty
        self.score = max(0, self.score)  # Ensure score doesn't go below 0
    def update_score(self, points):
        """Update the score by a given points amount."""
        self.score += points
        self.score = max(0, self.score)  # Ensure score doesn't go below 0
    def get_score(self):
        """Return the current score."""
        return self.score
    