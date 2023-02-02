from datetime import datetime

class Transaction:
    def __init__(self, payer: str, points: int, timestamp: datetime):
        self.payer = payer
        self.points = points
        self.timestamp = timestamp
