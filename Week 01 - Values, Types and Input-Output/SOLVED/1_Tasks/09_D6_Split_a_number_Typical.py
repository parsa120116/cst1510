total_seconds = 4831

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
