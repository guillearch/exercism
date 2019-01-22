class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.latest_score = self.scores[-1]
        self.personal_best_score = max(self.scores)
        self.personal_top_score = sorted(self.scores, reverse=True)[:3]
        self.dif = self.personal_best() - self.latest()

    def latest(self):
        return self.latest_score

    def personal_best(self):
        return self.personal_best_score

    def personal_top(self):
        return self.personal_top_score

    def report(self):
        if self.dif <= 0:
            return f"Your latest score was {self.latest()}. That's your personal best!"
        return f"Your latest score was {self.latest()}. That's {self.dif} short of your personal best!"
