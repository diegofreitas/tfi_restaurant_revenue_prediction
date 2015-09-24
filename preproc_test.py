__author__ = 'diego'

import unittest


class PreProcTest(unittest.TestCase):
    '''1. Transforme dados de texto para numeros para que o algo possa usar. ignorando os atributos id e data abertura
    X[0] >>> [0 '07/17/1999' '\xc4\xb0stanbul' 'Big Cities' 'IL' 4 5.0 4.0 4.0 2 2 5 4 5
     5 3 5 5.0 1 2 2 2 4 5 4 1 3 3 1 1 1.0 4.0 2.0 3.0 5 3 4 5 5 4 3 4
     5653753.0]
    X[0] >>> [31 0 2 4 5.0 4.0 4.0 2 2 5 4 5 5 3 5 5.0 1 2 2 2 4 5 4 1 3 3 1 1 1.0 4.0
     2.0 3.0 5 3 4 5 5 4 3 4 5653753.0]'''

    def test_bla(self):
        self.assertEqual('IL', data[0, 4])

        pass

    '''2. Separe a matriz em datasets de treino e teste
    X_train, X_test, y_train, y_test'''


if __name__ == '__main__':
    unittest.main()
