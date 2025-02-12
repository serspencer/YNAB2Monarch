import csv

def modify_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)  # Read the header row

        # Define the new header and column mapping
        new_headers = ["Date", "Merchant", "Category", "Account", "Original Statement", "Notes", "Amount"]

        # Find the index of each column in the input CSV
        account_index = headers.index("Account")
        date_index = headers.index("Date")
        payee_index = headers.index("Payee")
        category_index = headers.index("Category")
        memo_index = headers.index("Memo")
        outflow_index = headers.index("Outflow")
        inflow_index = headers.index("Inflow")

        # Write the modified data to the output CSV
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(new_headers)  # Write the new header row
            for row in reader:
                # Process each row according to the specified rules
                outflow_str = row[outflow_index][1:].replace(',', '') if row[outflow_index][0] == '$' else row[outflow_index].replace(',', '')
                inflow_str = row[inflow_index][1:].replace(',', '') if row[inflow_index][0] == '$' else row[inflow_index].replace(',', '')

                outflow = float(outflow_str) if outflow_str else 0
                inflow = float(inflow_str) if inflow_str else 0
                
                # Change out NAME
                is_original_statement = row[memo_index].startswith("NAME") or row[memo_index].startswith("NAME")   # Used to determine if the memo is an original statement

                new_row = [
                    row[date_index],  # Date stays and moves to column 1
                    row[payee_index],  # Payee stays and becomes "Merchant", moves to column 2
                    row[category_index],  # Category stays, moves to column 3
                    row[account_index],  # Account stays, moves to column 4
                    row[memo_index] if is_original_statement else "",  # Memo -> Original Statement, moves to column 5
                    row[memo_index] if not is_original_statement else "",  # Memo -> Notes, moves to column 6
                    -outflow if outflow != 0 else inflow if inflow != 0 else "",  # Outflow (if not 0) becomes negative, moves to column 7
                ]
                writer.writerow(new_row)

# Example usage:
input_file = r'C:\PATH_TO\ynab.csv'
output_file = r'C:\PATH_TO\output_modified.csv'
modify_csv(input_file, output_file)
print("CSV file modified according to specifications. Result saved to output_modified.csv.")
