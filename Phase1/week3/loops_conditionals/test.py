import unittest
import tempfile
import os

class EmptyFilesTest(unittest.TestCase):
    def setUp(self):
        self.empty_team = os.path.join(TEST_DATA, EMPTY_PATH, "TeamEmpty.csv")
        self.empty_product = os.path.join(TEST_DATA, EMPTY_PATH, "ProductEmpty.csv")
        self.empty_sales = os.path.join(TEST_DATA, EMPTY_PATH, "SalesEmpty.csv")

        self.team = os.path.join(TEST_DATA, MANYROWS_PATH, "TeamMany.csv")
        self.product = os.path.join(TEST_DATA, MANYROWS_PATH, "ProductMany.csv")
        self.sales = os.path.join(TEST_DATA, MANYROWS_PATH, "SalesMany.csv")

        # set up temporary file to write to
        self.tmp_path = tempfile.NamedTemporaryFile(delete=False)

    def test_empty_team(self):
        """Assert that an empty team file results in an error when initializing
        """
        self.assertRaises(ValueError, ReportGenerator, self.empty_team, self.product)
    
    def test_empty_products(self):
        """Assert that an empty products file results in an error when initializing
        """
        self.assertRaises(ValueError, ReportGenerator, self.empty_team, self.product)

    def test_empty_sales_team(self):
        """Assert that an empty sales file results in an error when generating team report
        """
        test = ReportGenerator(self.team, self.product)
        self.assertRaises(ValueError, test.gen_team_report, self.tmp_path.name, self.empty_sales)
    
    def test_empty_sales_prod(self):
        """Assert that an empty sales file results in an error when generating product report
        """
        test = ReportGenerator(self.team, self.product)
        self.assertRaises(ValueError, test.gen_prod_report, self.tmp_path.name, self.empty_sales)
    
    def tearDown(self):
        # close temp file after concluding test
        self.tmp_path.close()
        os.unlink(self.tmp_path.name)


if __name__ == '__main__':
    unittest.main()