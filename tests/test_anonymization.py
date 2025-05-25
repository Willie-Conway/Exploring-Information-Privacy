import unittest
import pandas as pd
from data_anonymization.k_anonymity import KAnonymity

class TestKAnonymity(unittest.TestCase):
    def setUp(self):
        data = {
            'age': [23, 23, 28, 25, 23, 27, 28, 25, 23, 27],
            'zipcode': ['10001', '10001', '10003', '10001', '10001', '10003', '10001', '10001', '10003', '10001'],
            'disease': ['Flu', 'Cold', 'HIV', 'Diabetes', 'Flu', 'Cold', 'HIV', 'Diabetes', 'Flu', 'Cold']
        }
        self.df = pd.DataFrame(data)
        
    def test_k_anonymity_check(self):
        k_anon = KAnonymity(self.df, ['age', 'zipcode'])
        self.assertTrue(k_anon.check_k_anonymity(2))
        self.assertFalse(k_anon.check_k_anonymity(3))
        
    def test_generalization(self):
        k_anon = KAnonymity(self.df, ['age', 'zipcode'])
        hierarchy = {23: '20-30', 25: '20-30', 27: '20-30', 28: '20-30'}
        k_anon.generalize('age', hierarchy)
        self.assertEqual(len(self.df['age'].unique()), 1)

if __name__ == '__main__':
    unittest.main()