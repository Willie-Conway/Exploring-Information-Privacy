class LDiversity:
    def __init__(self, dataframe, quasi_identifiers, sensitive_attribute):
        self.dataframe = dataframe
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute
        
    def check_l_diversity(self, l):
        groups = self.dataframe.groupby(self.quasi_identifiers)
        return all(group[self.sensitive_attribute].nunique() >= l 
                  for _, group in groups)
    
    def calculate_entropy_l_diversity(self):
        """Calculate entropy l-diversity for each group"""
        groups = self.dataframe.groupby(self.quasi_identifiers)
        results = {}
        
        for name, group in groups:
            value_counts = group[self.sensitive_attribute].value_counts(normalize=True)
            entropy = -sum(p * math.log(p) for p in value_counts if p > 0)
            results[name] = entropy
            
        return results