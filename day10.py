logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

error = 0
info = 0
warning = 0

for log in logs:
    log = log.upper()

    if "ERROR" in log:
        error += 1

    elif "INFO" in log:
        info += 1

    elif "WARNING" in log:
        warning += 1

print(f"Error log count = {error}")
print(f"Info log count = {info}")
print(f"Warning log count = {warning}")

count = {
    "error_count" : error,
    "info_count" : info,
    "warning_count" : warning,
}

maxcount = max(count, key = count.get)
print(f"The most appeared one is {maxcount}")