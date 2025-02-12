import csv
from ofxparse import OfxParser

def qfx_to_csv(qfx_file, csv_file):
    with open(qfx_file, 'rb') as qfx_data:
        ofx = OfxParser.parse(qfx_data)

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

# Usage example
qfx_file = r'C:\PATH_TO\FILE_NAME.qfx'
csv_file = r'C:\PATH_TO\FILE_NAME.csv'
qfx_to_csv(qfx_file, csv_file)
