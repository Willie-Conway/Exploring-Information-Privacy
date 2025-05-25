class GDPRComplianceChecker:
    GDPR_ARTICLES = {
        'article_5': 'Principles relating to processing of personal data',
        'article_6': 'Lawfulness of processing',
        'article_17': 'Right to erasure ("right to be forgotten")',
        'article_25': 'Data protection by design and by default'
    }
    
    def __init__(self, data_processing_activities):
        self.activities = data_processing_activities
        self.compliance_report = {}
        
    def check_compliance(self):
        """Check compliance with key GDPR articles"""
        self._check_article_5()
        self._check_article_6()
        self._check_article_17()
        self._check_article_25()
        return self.compliance_report
    
    def _check_article_5(self):
        """Check data processing principles"""
        requirements = [
            'lawfulness', 'fairness', 'transparency',
            'purpose_limitation', 'data_minimization',
            'accuracy', 'storage_limitation',
            'integrity_and_confidentiality'
        ]
        
        results = {}
        for req in requirements:
            results[req] = self._evaluate_requirement(req)
            
        self.compliance_report['article_5'] = {
            'description': self.GDPR_ARTICLES['article_5'],
            'requirements': results
        }
    
    def _check_article_6(self):
        """Check lawfulness of processing"""
        lawful_bases = [
            'consent', 'contract', 'legal_obligation',
            'vital_interests', 'public_task', 'legitimate_interests'
        ]
        
        results = {}
        for basis in lawful_bases:
            results[basis] = {
                'status': 'implemented' if basis in self.activities else 'missing',
                'evidence': f"Documentation for {basis}"
            }
            
        self.compliance_report['article_6'] = {
            'description': self.GDPR_ARTICLES['article_6'],
            'lawful_bases': results
        }
    
    def _check_article_17(self):
        """Check right to erasure"""
        self.compliance_report['article_17'] = {
            'description': self.GDPR_ARTICLES['article_17'],
            'status': 'implemented' if 'erasure_procedure' in self.activities else 'missing',
            'evidence': "Erasure procedure documentation"
        }
    
    def _check_article_25(self):
        """Check data protection by design"""
        self.compliance_report['article_25'] = {
            'description': self.GDPR_ARTICLES['article_25'],
            'status': 'implemented' if 'privacy_by_design' in self.activities else 'missing',
            'evidence': "System architecture documents"
        }
    
    def _evaluate_requirement(self, requirement):
        """Evaluate a single GDPR requirement"""
        return {
            'status': 'implemented' if requirement in self.activities else 'missing',
            'evidence': f"Documentation for {requirement}"
        }