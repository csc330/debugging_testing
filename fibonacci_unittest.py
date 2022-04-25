import unittest
from fibonacci import fib, fiblist

class FibonacciTest(unittest.TestCase):
    def testFibCalc(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)

    def testFibList(self):
        self.assertEqual(fiblist(0), [0, 1])
        self.assertEqual(fiblist(5), [0, 1, 1, 2, 3, 5])

def main():
    unittest.main()

if __name__ == "__main__":
    main()
