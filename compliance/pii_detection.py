import re
from typing import List, Dict

class PIIDetector:
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
            'phone': r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})\b',
            'credit_card': r'\b(?:\d[ -]*?){13,16}\b',
            'ip_address': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        }
        
    def detect_pii(self, text: str) -> Dict[str, List[str]]:
        """Detect PII in text using regular expressions"""
        results = {}
        
        for pii_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                # Flatten match groups and filter empty strings
                flat_matches = [match for match in matches if match] if isinstance(matches[0], tuple) else matches
                results[pii_type] = list(set(flat_matches))  # Remove duplicates
                
        return results
    
    def analyze_dataframe(self, df, sample_size=1000):
        """Analyze a DataFrame for PII columns"""
        results = {}
        
        for column in df.columns:
            # Sample data to improve performance
            sample = df[column].dropna().astype(str).sample(min(sample_size, len(df)))
            column_results = {}
            
            for pii_type in self.patterns:
                count = sum(sample.str.contains(self.patterns[pii_type], regex=True))
                if count > 0:
                    column_results[pii_type] = {
                        'count': count,
                        'percentage': (count / len(sample)) * 100
                    }
            
            if column_results:
                results[column] = column_results
                
        return results
    
    def generate_pii_report(self, df):
        """Generate a comprehensive PII report"""
        analysis = self.analyze_dataframe(df)
        report = {
            'pii_columns_found': len(analysis),
            'details': analysis,
            'risk_assessment': self._assess_risk(analysis)
        }
        return report
    
    def _assess_risk(self, analysis):
        """Assess risk based on PII findings"""
        risk_score = 0
        high_risk_types = ['ssn', 'credit_card']
        medium_risk_types = ['email', 'phone']
        
        for column, findings in analysis.items():
            for pii_type in findings:
                if pii_type in high_risk_types:
                    risk_score += findings[pii_type]['percentage'] * 1.0
                elif pii_type in medium_risk_types:
                    risk_score += findings[pii_type]['percentage'] * 0.5
                else:
                    risk_score += findings[pii_type]['percentage'] * 0.2
                    
        if risk_score > 50:
            return 'High'
        elif risk_score > 20:
            return 'Medium'
        else:
            return 'Low'