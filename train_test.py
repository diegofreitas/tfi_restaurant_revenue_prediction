__author__ = 'diego'

import unittest
from train import *


class TrainTest(unittest.TestCase):
    def test_rmse_should_be_less_than_1900000(self):
        score = train()
        self.assertLess(score, 1900000)



if __name__ == '__main__':
    unittest.main()
