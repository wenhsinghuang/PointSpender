import unittest
import sys
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    def test_main_function(self):
        # Redirect stdout to capture output from the main function
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the main function with 5000 as the argument
        main(5000)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check the output
        output = captured_output.getvalue()
        expected_output = "{'DANNON': 1000, 'UNILEVER': 0, 'MILLER COORS': 5300}\n"
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
