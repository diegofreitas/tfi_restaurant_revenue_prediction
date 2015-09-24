__author__ = 'diego'

import unittest
from load import *


class LoadTest(unittest.TestCase):
    # tipo de restaurante eh descrito na segunda linha da matriz?"
    def test_bla(self):
        data = load_data()
        self.assertEqual('IL', data[0,4])

    #Qual foi a lucratividade do restaurante descrito na segunda linha da matriz?"

    def test_check_head(self):
        dataframe = load_data()
        self.assertEquals(5891, dataframe.size)

if __name__ == '__main__':
    unittest.main()
