import os
import csv
from ofxparse import OfxParser

def qfx_to_csv(qfx_file):
    with open(qfx_file, 'rb') as qfx_data:
        ofx = OfxParser.parse(qfx_data)

        csv_file = os.path.splitext(qfx_file)[0] + '.csv'

        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write CSV headers
            writer.writerow(['Date', 'Transaction Type', 'Amount', 'Payee', 'Memo'])

            # Write transactions
            for transaction in ofx.account.statement.transactions:
                writer.writerow([
                    transaction.date.strftime('%Y-%m-%d'),
                    transaction.type,
                    transaction.amount,
                    transaction.payee,
                    transaction.memo
                ])

# Directory containing QFX files
input_directory = r'C:\PATH_TO'

# Iterate over files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.qfx'):
        qfx_file = os.path.join(input_directory, filename)
        qfx_to_csv(qfx_file)
