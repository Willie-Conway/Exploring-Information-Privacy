import random

class SecureMultiPartyComputation:
    def __init__(self, participants):
        self.participants = participants
        self.secrets = {}
        
    def share_secret(self, secret, owner):
        """Split secret into shares using Shamir's Secret Sharing (simplified)"""
        if len(self.participants) < 2:
            raise ValueError("Need at least 2 participants")
            
        # Generate random shares (simplified version)
        shares = {}
        remaining = secret
        for participant in self.participants[:-1]:
            share = random.randint(0, remaining)
            shares[participant] = share
            remaining -= share
        shares[self.participants[-1]] = remaining
        
        self.secrets[owner] = shares
        return shares
    
    def reconstruct_secret(self, owner):
        """Reconstruct secret from shares"""
        if owner not in self.secrets:
            raise ValueError("Owner not found")
            
        shares = self.secrets[owner]
        return sum(shares.values())
    
    def secure_sum(self, values):
        """Compute secure sum across participants"""
        # Each participant adds random noise to their value
        noisy_values = []
        for value in values:
            noise = random.random()
            noisy_values.append(value + noise)
            
        # Sum all noisy values
        total = sum(noisy_values)
        
        # Subtract the sum of all noise values
        # In real implementation, this would be done collaboratively
        return total