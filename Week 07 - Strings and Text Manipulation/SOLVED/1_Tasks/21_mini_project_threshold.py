"""
RECORD CHECK  -  my version
===========================

Name  :  Parsa
Lane  :  IT
Date  :  Week 7 lab

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Clean one messy raw line and return a dict with clean keys and number values."""
    line = raw_line.strip().lower()             # outer spaces gone, all lowercase
    hostname_part, rest = line.split(",", 1)    # hostname | all the key=value fields

    record = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


# ====================================================================== INPUT
# Deliberately messy: extra spaces, a tab, spaces around "=", mixed case.
raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    "   srv-03,used=45 ,total=100",
    "Srv-04 , Used = 93 , Total=100",
    "\tsRv-05,   used=99.5,total=100   ",
    "SRV-06 ,used= 12 , TOTAL = 50",
]


# =============================================================== PROCESS + OUTPUT
for raw_record in raw_records:
    record = parse_line(raw_record)
    print(record)


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records (6 above)
#    [x] Run it with a value that will not convert to a number - the error was:
#        ValueError: could not convert string to float: 'n/a'
#    [x] Check every function does one job, with a docstring
