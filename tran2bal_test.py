import csv
import os

def remove_extra_columns_and_reorganize(input_file, output_file):
    # Step 1: Remove extra columns and reorganize remaining columns
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Reorganize columns and remove extra ones
            modified_row = [row[0], '', row[3], row[6]]  # Date, Balance, Account, Amount
            writer.writerow(modified_row)

    print("Step 1: Extra columns removed and remaining columns reorganized. Result saved to", output_file)

def invert_spreadsheet(input_file, output_file):
    # Step 2: Invert the spreadsheet
    with open(input_file, 'r', newline='') as infile:
        data = list(csv.reader(infile))

    # Revert the order of rows
    inverted_data = data[:1] + data[1:][::-1]

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(inverted_data)

    print("Step 2: Spreadsheet inverted. Result saved to", output_file)

def calculate_running_balance(input_file, output_file):
    # Step 3: Running Balance
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Write the header row
        header = next(reader)
        header[1] = "Amount"  # Rename column 2 to "Amount"
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

    print("Step 3: Running balance calculated. Result saved to", output_file)

def revert_spreadsheet(input_file, output_file):
    # Step 4: Revert the spreadsheet
    with open(input_file, 'r', newline='') as infile:
        data = list(csv.reader(infile))

    # Revert the order of rows
    reverted_data = data[:1] + data[1:][::-1]

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(reverted_data)

    print("Step 4: Spreadsheet reverted. Result saved to", output_file)

def remove_duplicate_dates_and_remove_column(input_file, output_file):
    # Step 5: Remove duplicate Dates and remove the fourth column
    unique_dates = set()
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # Check if date is unique
            if row[0] not in unique_dates:
                # Omit column 3 (Balance)
                writer.writerow([row[0], row[1], row[2]])
                unique_dates.add(row[0])

    print("Step 5: Duplicate dates removed and column 4 removed. Result saved to", output_file)


# Define input and output file paths
BASE_DIR = r'C:\PATH_TO'
INPUT_FILE = os.path.join(BASE_DIR, 'output_modified.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'Steps')
OUTPUT_FILE_STEP1 = os.path.join(OUTPUT_DIR, 'step1_output.csv')
OUTPUT_FILE_STEP2 = os.path.join(OUTPUT_DIR, 'step2_output.csv')
OUTPUT_FILE_STEP3 = os.path.join(OUTPUT_DIR, 'step3_output.csv')
OUTPUT_FILE_STEP4 = os.path.join(OUTPUT_DIR, 'step4_output.csv')
OUTPUT_FILE_FINAL = os.path.join(BASE_DIR, 'ynab2balance_test.csv')

# Example usage:
remove_extra_columns_and_reorganize(INPUT_FILE, OUTPUT_FILE_STEP1)
invert_spreadsheet(OUTPUT_FILE_STEP1, OUTPUT_FILE_STEP2)
calculate_running_balance(OUTPUT_FILE_STEP2, OUTPUT_FILE_STEP3)
revert_spreadsheet(OUTPUT_FILE_STEP3, OUTPUT_FILE_STEP4)
remove_duplicate_dates_and_remove_column(OUTPUT_FILE_STEP4, OUTPUT_FILE_FINAL)