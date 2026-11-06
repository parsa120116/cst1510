lines = ["ERROR: disk full", "INFO: backup complete", "ERROR: timeout"]

for line in lines:
    if line.startswith("ERROR"):
        print("Needs attention: " + line)

print("report.csv".endswith(".csv"))

print("ERROR ERROR INFO ERROR".count("ERROR"))
