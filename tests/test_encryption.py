import unittest
from encryption.homomorphic_encryption import HomomorphicEncryption
from encryption.differential_privacy import DifferentialPrivacy

class TestEncryption(unittest.TestCase):
    def test_homomorphic_encryption(self):
        he = HomomorphicEncryption()
        encrypted = he.encrypt(10)
        self.assertEqual(he.decrypt(encrypted), 10)
        
        encrypted_sum = he.secure_sum([he.encrypt(x) for x in [10, 20, 30]])
        self.assertEqual(he.decrypt(encrypted_sum), 60)
        
    def test_differential_privacy(self):
        dp = DifferentialPrivacy(epsilon=1.0)
        true_value = 100
        noisy_value = dp.laplace_mechanism(true_value, sensitivity=1)
        self.assertTrue(abs(noisy_value - true_value) < 10)  # Very basic test

if __name__ == '__main__':
    unittest.main()