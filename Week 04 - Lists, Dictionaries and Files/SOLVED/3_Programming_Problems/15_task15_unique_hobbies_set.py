alex_hobbies = {"reading", "gaming", "cooking", "hiking"}
sam_hobbies = {"gaming", "hiking", "photography", "music"}

both_enjoy = alex_hobbies & sam_hobbies
only_alex = alex_hobbies - sam_hobbies
all_hobbies = alex_hobbies | sam_hobbies

print("Hobbies both enjoy:", sorted(both_enjoy))
print("Hobbies only Alex enjoys:", sorted(only_alex))
print("All unique hobbies:", sorted(all_hobbies))
