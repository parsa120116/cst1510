"""
RECORD CHECK  -  my version
===========================

Name  :  Parsa
Lane  :  IT
Date  :  November 2026

Run it:   python template.py

Reads servers.csv (hostname, used_gb, total_gb) and works out how full
each server's disk is.
"""

import pandas as pd

# ==================================================================== LOAD
# 1. Read the data file: one row per server.

df = pd.read_csv("servers.csv")


# ================================================================= PROCESS
# 2. percent = how full each disk is: (used_gb / total_gb) * 100

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100


# ================================================================== OUTPUT
# 3. Threshold: print the whole DataFrame, with the percent column.

print(df)


# ==========================================================================
# 4. Before you finish:
#    [x] Checked one row by hand: srv-01 -> 87 / 120 * 100 = 72.5
#    [x] Column names match the CSV header exactly: hostname, used_gb, total_gb
