import csv
from io import StringIO

def remove_extra_columns_and_reorganize(input_data):
    # Step 1: Remove extra columns and reorganize remaining columns
    output_data = StringIO()
    writer = csv.writer(output_data)

    for row in input_data:
        # Reorganize columns and remove extra ones
        modified_row = [row[0], '', row[3], row[6]]  # Date, Balance, Account, Amount
        writer.writerow(modified_row)

    print("Step 1: Extra columns removed and remaining columns reorganized.")
    return output_data.getvalue()

def invert_spreadsheet(input_data):
    # Step 2: Invert the spreadsheet
    output_data = StringIO()
    writer = csv.writer(output_data)

    # Revert the order of rows
    inverted_data = input_data[:1] + input_data[1:][::-1]

    writer.writerows(inverted_data)
    print("Step 2: Spreadsheet inverted.")
    return output_data.getvalue()

def calculate_running_balance(input_data):
    # Step 3: Running Balance
    output_data = StringIO()
    reader = csv.reader(input_data)
    writer = csv.writer(output_data)

    header = next(reader)
    writer.writerow(header)

    running_balance = 0
    for i, row in enumerate(reader):
        if i == 0:  # Skip the first row
            continue

        # Convert Amount to float and calculate running balance
        amount = float(row[3]) if row[3] else 0
        running_balance += amount

        # Write Date, Balance, Account, Amount
        writer.writerow([row[0], running_balance, row[2], row[3]])

    print("Step 3: Running balance calculated.")
    return output_data.getvalue()

def revert_spreadsheet(input_data):
    # Step 4: Revert the spreadsheet
    output_data = StringIO()
    writer = csv.writer(output_data)

    # Revert the order of rows
    reverted_data = input_data[:1] + input_data[1:][::-1]

    writer.writerows(reverted_data)
    print("Step 4: Spreadsheet reverted.")
    return output_data.getvalue()

def remove_duplicate_dates(input_data):
    # Step 5: Remove duplicate Dates
    unique_dates = set()
    output_data = StringIO()
    reader = csv.reader(input_data)
    writer = csv.writer(output_data)

    for row in reader:
        # Check if date is unique
        if row[0] not in unique_dates:
            writer.writerow(row)
            unique_dates.add(row[0])

    print("Step 5: Duplicate dates removed.")
    return output_data.getvalue()

# Example usage:
with open(r'C:\PATH_TO\output_modified.csv', 'r', newline='') as infile:
    input_data = list(csv.reader(infile))

output_data = remove_extra_columns_and_reorganize(input_data)
output_data = invert_spreadsheet(output_data.splitlines())
output_data = calculate_running_balance(output_data.splitlines())
output_data = revert_spreadsheet(output_data.splitlines())
output_data = remove_duplicate_dates(output_data.splitlines())

# Output the final result
with open('output.csv', 'w', newline='') as outfile:
    outfile.write(output_data)

print("Final result saved to output.csv.")
