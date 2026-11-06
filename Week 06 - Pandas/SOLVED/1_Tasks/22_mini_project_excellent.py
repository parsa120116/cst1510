"""
RECORD CHECK  -  my version
===========================

Name  :  Parsa
Lane  :  IT
Date  :  November 2026

Run it:   python template.py

Reads servers.csv (hostname, used_gb, total_gb), works out how full each
server's disk is, gives it a status, reports the servers that need attention
and a count per status, then saves a CSV report and a bar chart.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read the data file: one row per server.

df = pd.read_csv("servers.csv")


# ================================================================= PROCESS
# 2. percent = how full each disk is: (used_gb / total_gb) * 100
#    status  = OVER LIMIT (100%+), WARNING (90%+), otherwise OK

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)


# ================================================================== OUTPUT
# 3. Threshold : print the whole DataFrame.
#    Typical   : print only the servers that are not OK.
#    Excellent : count per status, save a CSV report and a bar chart.

print("All servers:")
print(df)

not_ok = df[df["status"] != "OK"]
print("\nServers that need attention:")
print(not_ok)

status_counts = df.groupby("status")["hostname"].count()
print("\nServers per status:")
print(status_counts)

df.to_csv("servers_report.csv", index=False)
print(f"\nChecked {len(df)} servers. {len(not_ok)} need attention.")
print("Saved servers_report.csv")

status_counts.plot(kind="bar")
plt.title("Servers per status")
plt.xlabel("Status")
plt.ylabel("Number of servers")
plt.tight_layout()
plt.savefig("server_status.png")
print("Saved server_status.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [x] Checked one row by hand: srv-05 -> 126 / 120 * 100 = 105.0 -> OVER LIMIT
#    [x] One condition only, so no & / | needed
#    [x] Column names match the CSV header exactly: hostname, used_gb, total_gb
