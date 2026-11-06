class Account:
    """A user account that locks after 3 failed logins."""

    def __init__(self, username):
        """Store the username and start with 0 failed logins."""
        self.username = username
        self.failed_logins = 0

    def fail(self):
        """Record one failed login."""
        self.failed_logins += 1

    def locked(self):
        """Return True if there have been 3 or more failed logins."""
        return self.failed_logins >= 3


anna = Account("anna")
anna.fail()
anna.fail()
anna.fail()
print(anna.locked())

ben = Account("ben")
ben.fail()
print(ben.locked())
