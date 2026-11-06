def is_palindrome(text):
    """Return True if text reads the same backward as forward (loop version)."""
    cleaned = text.lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("racecar"))   # True
print(is_palindrome("Kayak"))     # True
print(is_palindrome("python"))    # False
