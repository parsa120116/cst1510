episodes_per_season = 10

# Length of one episode, in seconds
season1_episode = 45 * 60 + 35        # 45 min 35 s
later_episode = 35 * 60 + 15          # 35 min 15 s (seasons 2-5)

season1_total = 1 * episodes_per_season * season1_episode
later_total = 4 * episodes_per_season * later_episode
total_seconds = season1_total + later_total

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"Total time: {hours}h {minutes}m {seconds}s")
