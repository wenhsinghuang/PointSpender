import sys
import os
import csv
from datetime import datetime
from utils.models import Transaction
from utils.point_spender import point_spender

def parse_timestamp(timestamp_str: str) -> datetime:
    return datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')

def main(amount_to_spend: int) -> None:
    """
    Process I/O and data pre-processing.

    Parameters:
    amount_to_spend (int): The amount of points to spend.

    Returns:
    None.
    """
    csv_file_path = os.path.join(os.getcwd(), 'transactions.csv')
    if not os.path.exists(csv_file_path):
        print(f'Error: The transactions.csv file was not found in the current working directory ({os.getcwd()})')
        sys.exit(1)
    
    if not os.access(csv_file_path, os.R_OK):
        # file is not readable
        print('Error: file is not readable')
        sys.exit(1)
        
    transactions = []
    with open(csv_file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header
        for row in reader:
            payer, points, timestamp = row
            transactions.append(Transaction(payer, int(points), parse_timestamp(timestamp)))
    
    # through this API, we can change only main() to adapt different data format.
    balances = point_spender(transactions, amount_to_spend)
    print(balances)

if __name__ == '__main__':
    # argument check
    if len(sys.argv) != 2:
        print('Error: Incorrect number of arguments. Please specify the amount to spend.')
        sys.exit(1)

    try:
        amount_to_spend = int(sys.argv[1])
    except ValueError:
        print('Error: Invalid argument type. Please enter a valid integer.')
        sys.exit(1)
    
    if amount_to_spend < 0:
        print('Error: The amount to spend should not be a negative number.')
        sys.exit(1)
    
    main(amount_to_spend)
