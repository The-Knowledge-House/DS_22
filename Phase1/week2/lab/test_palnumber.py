### Do not modify code below! ###
import io
import unittest
import unittest.mock
from palnumber import main

class PalindromeIntTest(unittest.TestCase):
    def setUp(self):
        self.true_int = 1001
        self.false_int = 1002
        self.false_inner_int = 102101
        self.singular = 1

        self.true_float = 1.001
        self.false_float = 1.002
        self.false_inner_float = 10210.1
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_true_int(self):
        self.assertEquals(main(self.true_int), True)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_false_int(self):
        self.assertEquals(main(self.false_int), False)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_false_inner_int(self):
        self.assertEquals(main(self.false_inner_int), False)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_singular(self):
        self.assertEquals(main(self.singular), True)


class PalindromeFloatTest(unittest.TestCase):
    def setUp(self):
        self.true_float = 1.001
        self.false_float = 1.002
        self.false_inner_float = 10210.1
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_true_float(self):
        self.assertEquals(main(self.true_float), True)
    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_false_float(self):
        self.assertEquals(main(self.false_float), False)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_false_inner_float(self):
        self.assertEquals(main(self.false_inner_float), False)


if __name__ == '__main__':
    unittest.main()