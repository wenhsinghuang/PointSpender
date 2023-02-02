import unittest
from datetime import datetime
from utils.point_spender import point_spender
from utils.models import Transaction

class TestPointSpender(unittest.TestCase):
    def test_point_spender_with_empty_csv(self):
        transactions = []
        amount_to_spend = 0
        result = point_spender(transactions, amount_to_spend)
        expected = {}
        self.assertEqual(result, expected)

    def test_point_spender_with_empty_csv_and_not_enough_points(self):
        transactions = []
        amount_to_spend = 100
        try:
            point_spender(transactions, amount_to_spend)
            assert False, "Exception not raised"
        except Exception as e:
            assert str(e) == "Error: The amount to spend should not exceed total balance."

    def test_point_spender_with_not_enough_points(self):
        transactions = [
            Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("UNILEVER", 200, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("DANNON", -200, datetime.strptime("2020-10-31T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("MILLER COORS", 10000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("DANNON", 300, datetime.strptime("2020-10-31T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
        ]
        amount_to_spend = 15000
        try:
            point_spender(transactions, amount_to_spend)
            assert False, "Exception not raised"
        except Exception as e:
            assert str(e) == "Error: The amount to spend should not exceed total balance."


    def test_point_spender_with_illegal_transactions(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", -2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 3000
        try:
            point_spender(transactions, amount_to_spend)
            assert False, "Exception not raised"
        except Exception as e:
            assert str(e) == "Error: one history transaction exceed total balance at its timestamp."

    def test_point_spender_test1(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", 2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 100
        result = point_spender(transactions, amount_to_spend)
        expected = {"A": 900, "B": 2000}
        self.assertEqual(result, expected)

    def test_point_spender_test2(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", 2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 1000
        result = point_spender(transactions, amount_to_spend)
        expected = {"A": 0, "B": 2000}
        self.assertEqual(result, expected)

    def test_point_spender_test3(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", 2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 1500
        result = point_spender(transactions, amount_to_spend)
        expected = {"A": 0, "B": 1500}
        self.assertEqual(result, expected)

    def test_point_spender_test4(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", 2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("A", 1000, datetime.strptime("2020-11-03T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 1500
        result = point_spender(transactions, amount_to_spend)
        expected = {"A": 1000, "B": 1500}
        self.assertEqual(result, expected)

    def test_point_spender_test5(self):
        transactions = [
            Transaction("A", 1000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("B", 2000, datetime.strptime("2020-11-02T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("A", -1000, datetime.strptime("2020-11-03T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("C", 1000, datetime.strptime("2020-11-04T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
        ]
        amount_to_spend = 1500
        result = point_spender(transactions, amount_to_spend)
        expected = {"A": 0, "B": 500, "C": 1000}
        self.assertEqual(result, expected)

    def test_point_spender_test6(self):
        transactions = [
            Transaction("DANNON", 1000, datetime.strptime("2020-11-02T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("UNILEVER", 200, datetime.strptime("2020-10-31T11:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("DANNON", -200, datetime.strptime("2020-10-31T15:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("MILLER COORS", 10000, datetime.strptime("2020-11-01T14:00:00Z", "%Y-%m-%dT%H:%M:%SZ")),
            Transaction("DANNON", 300, datetime.strptime("2020-10-31T10:00:00Z", "%Y-%m-%dT%H:%M:%SZ"))
        ]
        amount_to_spend = 5000
        result = point_spender(transactions, amount_to_spend)
        expected = {"DANNON": 1000, "UNILEVER": 0, "MILLER COORS": 5300}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
