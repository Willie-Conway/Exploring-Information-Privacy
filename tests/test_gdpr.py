# tests/test_gdpr.py
def test_empty_activities(self):
    checker = GDPRComplianceChecker([])
    report = checker.check_compliance()
    self.assertFalse(report['article_5']['requirements']['lawfulness']['status'])