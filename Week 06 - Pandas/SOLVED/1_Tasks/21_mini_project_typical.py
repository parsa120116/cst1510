"""
RECORD CHECK  -  my version
===========================

Name  :  Parsa
Lane  :  IT
Date  :  November 2026

Run it:   python template.py

Reads servers.csv (hostname, used_gb, total_gb), works out how full each
server's disk is, gives it a status and shows the servers that need attention.
"""

import pandas as pd

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
# 3. Threshold: print the whole DataFrame.
#    Typical  : print only the servers that are not OK (boolean filter, no loop).

print("All servers:")
print(df)

not_ok = df[df["status"] != "OK"]
print("\nServers that need attention:")
print(not_ok)


# ==========================================================================
# 4. Before you finish:
#    [x] Checked one row by hand: srv-03 -> 460 / 500 * 100 = 92.0 -> WARNING
#    [x] One condition only, so no & / | needed
#    [x] Column names match the CSV header exactly: hostname, used_gb, total_gb
