from phe import paillier

class HomomorphicEncryption:
    def __init__(self, key_length=2048):
        self.public_key, self.private_key = paillier.generate_paillier_keypair(
            n_length=key_length
        )
    
    def encrypt(self, value):
        """Encrypt a value using Paillier cryptosystem"""
        if isinstance(value, (int, float)):
            return self.public_key.encrypt(value)
        raise ValueError("Value must be numeric")
    
    def decrypt(self, encrypted_value):
        """Decrypt an encrypted value"""
        return self.private_key.decrypt(encrypted_value)
    
    def secure_sum(self, encrypted_values):
        """Compute secure sum of encrypted values"""
        if not encrypted_values:
            return None
        result = encrypted_values[0]
        for val in encrypted_values[1:]:
            result += val
        return result
    
    def secure_mean(self, encrypted_values, count):
        """Compute secure mean of encrypted values"""
        total = self.secure_sum(encrypted_values)
        return total * (1/count)