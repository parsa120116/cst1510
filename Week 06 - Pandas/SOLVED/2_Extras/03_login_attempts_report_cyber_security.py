# FINDINGS (two sentences):
# 10.0.0.12 and 10.0.0.5 are tied on total failures (8 each), but 10.0.0.12 did all 8
# in ONE session (8 of 9 attempts failed), so I would escalate it first.
# 10.0.0.5 comes next: it failed in both of its sessions (5, then 3 of 3), a repeat pattern.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and look
df = pd.read_csv("login_attempts.csv")
print(df.head())
print()
print(df.dtypes)
print(f"\nRows (sessions): {len(df)}")
print(f"Different IPs: {df['ip'].nunique()}")

# 2. A question with a filter: sessions with 3 or more failed attempts
many_failures = df[df["failed"] >= 3]
print(f"\nSessions with 3+ failed attempts: {len(many_failures)}")
print(many_failures)

# 3. A question with a group: total failed attempts per IP
failed_per_ip = df.groupby("ip")["failed"].sum()

# 4. Sort it: which IP has the most failed attempts in total?
failed_per_ip = failed_per_ip.sort_values(ascending=False)
print("\nTotal failed attempts per IP (highest first):")
print(failed_per_ip)

top_total = failed_per_ip.max()
top_ips = failed_per_ip[failed_per_ip == top_total]
print(f"\nMost failed attempts in total: {top_total}, by {top_ips.index.tolist()}")

# 5. Flag it: suspicious column with apply + lambda
df["suspicious"] = df["failed"].apply(lambda f: True if f >= 3 else False)
print()
print(df)

# 6. Chart it: failed attempts per IP (group first, then plot)
failed_per_ip.plot(kind="bar")
plt.title("Total failed login attempts per IP")
plt.xlabel("IP address")
plt.ylabel("Failed attempts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("failed_per_ip.png")
print("\nSaved failed_per_ip.png")
plt.show()

# 7. Save it: only the suspicious rows
flagged = df[df["suspicious"] == True]
flagged.to_csv("flagged_ips.csv", index=False)
print(f"Saved flagged_ips.csv ({len(flagged)} rows)")
