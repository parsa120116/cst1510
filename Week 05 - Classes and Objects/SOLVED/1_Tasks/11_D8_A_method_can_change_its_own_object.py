class Checker:
    def __init__(self):
        self.over_limit_count = 0

    def check(self, value, limit):
        """Add 1 to the count if value is over limit."""
        if value > limit:
            self.over_limit_count += 1

checker = Checker()
checker.check(87, 100)
checker.check(120, 100)
checker.check(130, 100)
print(checker.over_limit_count)
