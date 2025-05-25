class PrivacyRiskAssessor:
    def __init__(self, dataset):
        self.dataset = dataset
        self.risks = {}
        
    def identify_pii(self):
        """Identify potential personally identifiable information"""
        pii_columns = []
        for column in self.dataset.columns:
            col_data = self.dataset[column].dropna().astype(str)
            if self._is_pii(col_data):
                pii_columns.append(column)
        return pii_columns
    
    def _is_pii(self, series):
        """Heuristic check for PII"""
        sample = series.sample(min(100, len(series)))
        
        # Check for email patterns (updated regex)
        email_count = sample.str.contains(r'@\w+\.\w+').sum()
        if email_count / len(sample) > 0.1:
            return True
            
        # Check for phone numbers (non-capturing group)
        phone_count = sample.str.contains(r'(?:\d{3}[-\.\s]\d{3}[-\.\s]\d{4})').sum()
        if phone_count / len(sample) > 0.1:
            return True
            
        return False
    
    def calculate_risk_score(self, column):
        """Calculate privacy risk score for a column"""
        uniqueness = self.dataset[column].nunique() / len(self.dataset)
        sensitivity = self._estimate_sensitivity(column)
        return uniqueness * sensitivity
    
    def _estimate_sensitivity(self, column):
        """Estimate sensitivity of data in a column"""
        if column.lower() in ['ssn', 'social security']:
            return 1.0
        elif column.lower() in ['email', 'phone', 'address']:
            return 0.8
        elif column.lower() in ['name', 'dob']:
            return 0.6
        else:
            return 0.3