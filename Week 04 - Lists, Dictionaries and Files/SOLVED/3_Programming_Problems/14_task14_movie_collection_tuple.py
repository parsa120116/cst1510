movies = (("Inception", 2010), ("Matrix", 1999), ("Interstellar", 2014))

# The oldest movie
oldest = movies[0]
for movie in movies:
    if movie[1] < oldest[1]:
        oldest = movie
print(f"Oldest movie: {oldest[0]} ({oldest[1]})")

# All movie titles
print("All movie titles:")
for title, year in movies:
    print(title)

# Try to change a year
try:
    movies[1][1] = 2000
except TypeError as error:
    print("Cannot change a year:", error)
