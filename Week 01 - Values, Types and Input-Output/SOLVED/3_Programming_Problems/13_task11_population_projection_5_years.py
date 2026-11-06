population = 312032486
seconds_per_year = 365 * 24 * 60 * 60     # 31,536,000

births = seconds_per_year // 7
deaths = seconds_per_year // 13
immigrants = seconds_per_year // 45
net_change = births - deaths + immigrants

# No loops in Week 1, so one explicit step per year
population += net_change
print(f"Year 1: {population:,}")
population += net_change
print(f"Year 2: {population:,}")
population += net_change
print(f"Year 3: {population:,}")
population += net_change
print(f"Year 4: {population:,}")
population += net_change
print(f"Year 5: {population:,}")
