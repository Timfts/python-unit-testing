from unittest import TestCase
from Printer import Printer

class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_second=2.0, capacity=300)

    def test_print_within_capacity(self):

        message = self.printer.print(25)
        self.assertEqual(message, f"Printed 25 pages in 12.50 seconds.")