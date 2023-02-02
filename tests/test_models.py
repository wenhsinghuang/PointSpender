import unittest
from datetime import datetime
from utils.models import Transaction

class TestModels(unittest.TestCase):
    def test_transaction_model(self):
        t1 = Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        t2 = Transaction("UNILEVER", 200, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))

        self.assertEqual(t1.payer, "DANNON")
        self.assertEqual(t1.points, 1000)
        self.assertEqual(t1.timestamp, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        self.assertEqual(t2.payer, "UNILEVER")
        self.assertEqual(t2.points, 200)
        self.assertEqual(t2.timestamp, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))

    def test_transaction_point_modify(self):
        t = Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        t.points += 2000
        self.assertEqual(t.points, 3000)


    def test_transactions_sort(self):
            transactions = [
                Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
                Transaction("UNILEVER", 200, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
                Transaction("DANNON", -200, datetime.strptime("2020-10-31T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
                Transaction("MILLER COORS", 10000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
                Transaction("DANNON", 300, datetime.strptime("2020-10-31T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            ]
            transactions.sort(key=lambda x: x.timestamp)
            self.assertEqual(transactions[0], Transaction("DANNON", 300, datetime.strptime("2020-10-31T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ")))
            self.assertEqual(transactions[2], Transaction("UNILEVER", 200, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")))
            self.assertEqual(transactions[1], Transaction("DANNON", -200, datetime.strptime("2020-10-31T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ")))
            self.assertEqual(transactions[3], Transaction("MILLER COORS", 10000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")))
            self.assertEqual(transactions[4], Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")))


if __name__ == "__main__":
    unittest.main()