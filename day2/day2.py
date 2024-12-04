def is_safe(report):
    increasing = True
    decreasing = True
    
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        
        # If difference is less than 1 or greater than 3, the report is unsafe
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        # Check if the report is not fully increasing or not fully decreasing
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
        
    return increasing or decreasing


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    
    # Check if removing a single element makes the report safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count



# Read reports from data.txt
with open('C:/Users/aksel/OneDrive/Masaüstü/personal_projects/adventofcode/2024/day2/data.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

# Count the number of safe reports
safe_reports = count_safe_reports(reports)
print(f"Number of safe reports: {safe_reports}")
