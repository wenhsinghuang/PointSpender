
from typing import List, Dict
from utils.models import Transaction


def point_spender(transactions: List[Transaction], amount_to_spend: int) -> Dict[str, int]:
    """
    API for to calculate balances of each payer after spend.

    Parameters:
    transactions (List[Transaction]): The initial transactions record.
    amount_to_spend (int): The amount of points to spend.

    Returns:
    balances (Dict[str, int]): balances of each payer after spend
    """
    # sort transactions by timestamp
    transactions.sort(key=lambda x: x.timestamp)
    
    # check if amount_to_spend over total points the user have.
    if sum(t.points for t in transactions) < amount_to_spend:
        raise Exception("Error: The amount to spend should not exceed total balance.")

    # calculate temporary transactions that have handled the history spending.
    for i in range(len(transactions)):
        if transactions[i].points < 0:
            for j in range(0,i):
                pay = min(transactions[j].points, abs(transactions[i].points))
                transactions[j].points -= pay
                transactions[i].points += pay
                if transactions[i].points == 0:
                    break
            if transactions[i].points < 0:
                raise Exception("Error: one history transaction exceed total balance at its timestamp.")
    
    # spend points based on rules
    for i in range(len(transactions)):
        pay = min(transactions[i].points, amount_to_spend)
        transactions[i].points -= pay
        amount_to_spend -= pay
        if amount_to_spend == 0:
            break

    balances = {}
    for i in range(len(transactions)):
        if transactions[i].payer not in balances:
            balances[transactions[i].payer] = 0
        balances[transactions[i].payer] += transactions[i].points
    
    return balances