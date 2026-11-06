weeks_per_year = 52
years = 3
total_weeks = weeks_per_year * years      # 156 weeks

savings = 0.0
savings += 10 * total_weeks               # £10 every week for 3 years
savings += 20 * weeks_per_year            # +£20 each week, year 1 only
savings -= 0.50 * (total_weeks // 2)      # -£0.50 every 2 weeks (sister)

print(f"Final savings after 3 years: £{savings:.2f}")
