class PrinterError(RuntimeError):
    pass

class Printer:
    def __init__(self, pages_per_second: int, capacity: int):
        self.pages_per_second = pages_per_second
        self._capacity = capacity
    
    def print(self, pages):
        if pages > self._capacity:
            raise PrinterError("printer does not have enough capacity for all these pages")

        self._capacity -= pages

        return f"Printed {pages} pages in {pages/self.pages_per_second:.2f} seconds."