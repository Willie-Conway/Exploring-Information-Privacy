import numpy as np

class DifferentialPrivacy:
    def __init__(self, epsilon=1.0):
        self.epsilon = epsilon
        
    def laplace_mechanism(self, true_value, sensitivity):
        """Apply Laplace mechanism for differential privacy"""
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale)
        return true_value + noise
    
    def exponential_mechanism(self, items, scores, sensitivity):
        """Implement exponential mechanism for differential privacy"""
        # Calculate probabilities
        probabilities = [
            np.exp(self.epsilon * score / (2 * sensitivity))
            for score in scores
        ]
        total = sum(probabilities)
        probabilities = [p / total for p in probabilities]
        
        # Select item based on probabilities
        return np.random.choice(items, p=probabilities)
    
    def gaussian_mechanism(self, true_value, sensitivity, delta):
        """Apply Gaussian mechanism for differential privacy"""
        sigma = np.sqrt(2 * np.log(1.25/delta)) * sensitivity / self.epsilon
        noise = np.random.normal(0, sigma)
        return true_value + noise