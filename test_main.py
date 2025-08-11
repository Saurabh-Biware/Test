import unittest
import subprocess
import sys
from main import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!")

    def test_main_execution(self):
        """Test running the script directly to cover __main__ block"""
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.stdout.strip(), "Hello World!")


if __name__ == "__main__":
    unittest.main()
