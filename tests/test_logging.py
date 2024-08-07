import unittest
import os
from src import setup_logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.log_file = "test.log"
        self.logger = setup_logger("test_logger", self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_logging(self):
        self.logger.info("Test log message")
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r") as f:
            content = f.read()
            self.assertIn("Test log message", content)

if __name__ == "__main__":
    unittest.main()