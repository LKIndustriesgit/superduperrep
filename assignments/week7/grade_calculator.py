# Hello Qianxun! More will be added.
from sys import argv
import csv
import random

# Step 1
def read_csv(filename):
    # load csv to variables in your program
    # handle file exceptions here
    data = {}
    with open(filename) as f:
        f.readline()  # Skip header
        for line in f:
            items = line.strip().split(",")  # Strip newline and split
            # Skip lines that have fewer than expected columns (e.g., less than 9)
            if len(items) < 9:
                continue  # skip this line

            # skip lines that have no 'name' (first column empty)
            if items[0].strip() == "":
                continue
            name = items[0]
            stream = items[1]
            email = items[2]
            github = items[3]

            # Clean week values: replace "-" with "0", then convert to float
            weeks = []
            for i in range(4, 9):
                value = items[i].strip()
                try:
                    weeks.append(float(value))
                except ValueError:
                    weeks.append(0.0)
            # Combine everything
            data[name] = [stream, email, github] + weeks
        return data
    pass

# Step 2
def populate_scores():
    for name, values in data.items():
        current_week_count = len(values) - 3  # weeks start after first 3 fields
        if current_week_count < 13:
            missing_weeks = 13 - current_week_count
            new_weeks = [float(random.randint(0, 3)) for _ in range(missing_weeks)]
            values.extend(new_weeks)
    pass

# Step 3
def calculate_all():
    # loop through all the students and calculate grades
    pass

def calculate_total(scores):
    total = 0
    return total

def calculate_average(scores):
    average =  0
    return average

# After the update let's save the data as a new csv file

def write_csv(filename, data):
    with open(filename, 'w') as f:
        for name, values in data.items():  # <-- 'data' must be accessible
            row = ",".join([name] + [str(v) for v in values])
            f.write(row + "\n")
    pass

# Bonus

def print_analysis():
    # print average scores for stream A, B and every week
    pass

if __name__ == "__main__":
    script, filename = argv

    print("Open file:", filename)

    data = read_csv(filename)

    populate_scores()
    calculate_all()

    user_name = "[your_name]"

    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"
    write_csv(newname, data)
    print("New file written:", newname)

    print_analysis()

# Run the file with `python grade_calculator.py sheet.csv`