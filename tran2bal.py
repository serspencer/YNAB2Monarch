import csv

def calculate_running_balance(input_file, output_file):
    amount_index = None
    balance_index = None
    balance = 0

    # Read input CSV file and find the index of the amount column
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        headers.append("Running Balance")
        for i, header in enumerate(headers):
            if header.strip().lower() == 'amount':
                amount_index = i
            elif header.strip().lower() == 'running balance':
                balance_index = i
        if amount_index is None:
            print("Amount column not found in CSV.")
            return

        rows = list(reader)

        # Calculate running balance in reverse order
        for row in reversed(rows):
            amount = float(row[amount_index].strip())
            balance += amount
            row.append(balance)

        # Update headers if balance index not found
        if balance_index is None:
            headers.append("Running Balance")

        # Write rows with running balance to output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers)
            for row in rows:
                writer.writerow(row)

def remove_duplicate_dates(input_file, output_file):
    date_index = None
    unique_dates = set()

    # Read input CSV file and find the index of the date column
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        for i, header in enumerate(headers):
            if header.strip().lower() == 'date':
                date_index = i
                break
        if date_index is None:
            print("Date column not found in CSV.")
            return

        # Write rows with unique dates to output CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers)
            for row in reader:
                date = row[date_index].strip()
                if date not in unique_dates:
                    writer.writerow(row)
                    unique_dates.add(date)

# Example usage:
temp_file = r'C:\PATH_TO\temp.csv'
input_file = r'C:\PATH_TO\output_modified.csv'
output_file = r'C:\PATH_TO\ynab2balance.csv'

calculate_running_balance(input_file, temp_file)
remove_duplicate_dates(temp_file, output_file)

print("Running balance added and duplicates removed. Result saved to output_with_balance.csv.")
