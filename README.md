# PointSpender
This is a Python solution to the Fetch coding exercise for a software engineering internship.

## Understanding of the Problem
The "transactions.csv" file contains transaction records for a user. 
Transactions with positive points indicate that the user has earned points from the payer, while transactions with negative points indicate that the user has spent points with the payer. 
This action is equivalent to the program's "spending" action. To determine the result of current spending, it is necessary to take into account the state of the transaction history after all historical spending transactions have been processed.

# Edge Cases Handling
I handle edge cases differently in `main.py` and `point_spender.py`. 
For the command line interface (CLI) in `main.py`, I print an error message and exit the program. 
For the API in `point_spender.py`, I raise an exception to help the API caller catch unexpected situations.

## Requirements
* Python 3.x

## Usage
* To run the program, use the following command: 
`python3 main.py [spend_points]`
spend_points is the amount of points to spend

## Testing
* To run the test cases, use the following command: 
`python3 -m unittest discover`
* The tests are located in the test folder and are named test_*.py

## Note
"wenhsinghuang" (personal) and "whhuang4" (school) both are my account.
