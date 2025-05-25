import pandas as pd

class DataFlowMapper:
    def __init__(self):
        self.flows = []
        
    def add_flow(self, source, destination, data_type, purpose):
        """Add a data flow between systems"""
        self.flows.append({
            'source': source,
            'destination': destination,
            'data_type': data_type,
            'purpose': purpose
        })
        
    def get_flows(self):
        """Get all data flows as a DataFrame"""
        return pd.DataFrame(self.flows)
        
    def find_pii_flows(self):
        """Identify flows containing PII"""
        pii_keywords = ['name', 'email', 'address', 'phone', 'ssn', 'credit card']
        pii_flows = []
        
        for flow in self.flows:
            if any(keyword in flow['data_type'].lower() for keyword in pii_keywords):
                pii_flows.append(flow)
                
        return pd.DataFrame(pii_flows)
    
    def generate_data_protection_impact(self):
        """Generate DPIA-like assessment"""
        df = self.get_flows()
        impact = []
        
        for _, row in df.iterrows():
            risk = 'low'
            if any(keyword in row['data_type'].lower() 
                  for keyword in ['ssn', 'medical', 'financial']):
                risk = 'high'
            elif any(keyword in row['data_type'].lower() 
                    for keyword in ['email', 'phone', 'address']):
                risk = 'medium'
                
            impact.append({
                'flow': f"{row['source']} → {row['destination']}",
                'data_type': row['data_type'],
                'risk': risk,
                'protection_measures': self._suggest_protection(risk)
            })
            
        return pd.DataFrame(impact)
    
    def _suggest_protection(self, risk):
        """Suggest protection measures based on risk level"""
        measures = {
            'high': "Encryption at rest and in transit, strict access controls, anonymization",
            'medium': "Encryption in transit, role-based access controls",
            'low': "Basic access controls"
        }
        return measures.get(risk, "No special measures")