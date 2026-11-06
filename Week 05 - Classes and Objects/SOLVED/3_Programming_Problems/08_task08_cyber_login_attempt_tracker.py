class Account:
    """A user account that locks after 3 failed logins."""

    MAX_ATTEMPTS = 3

    def __init__(self, username, password):
        """Store the login details and start with 0 failed attempts."""
        self.username = username
        self.password = password
        self.failed_attempts = 0

    def is_locked(self):
        """Return True if the account has too many failed attempts."""
        return self.failed_attempts >= Account.MAX_ATTEMPTS

    def login(self, password):
        """Try to log in; return True on success, False otherwise."""
        if self.is_locked():
            print(f"  {self.username}: account LOCKED, login refused.")
            return False
        if password == self.password:
            self.failed_attempts = 0
            print(f"  {self.username}: login OK.")
            return True
        self.failed_attempts += 1
        print(f"  {self.username}: wrong password ({self.failed_attempts}/{Account.MAX_ATTEMPTS}).")
        if self.is_locked():
            print(f"  {self.username}: too many failed attempts, account is now locked.")
        return False


user = Account("parsa", "S3cure!pass")

print("Test 1: correct password")
print(user.login("S3cure!pass"))

print("Test 2: one wrong, then correct (counter resets)")
print(user.login("hello123"))
print(user.login("S3cure!pass"))
print("Failed attempts now:", user.failed_attempts)

print("Test 3: three wrong passwords")
for guess in ["password", "123456", "qwerty"]:
    print(user.login(guess))

print("Test 4: correct password after the lock")
print(user.login("S3cure!pass"))
print("Locked?", user.is_locked())

print("Test 5: another user is not affected")
other = Account("sara", "tulip99")
print(other.login("tulip99"))
