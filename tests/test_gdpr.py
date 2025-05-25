# tests/test_gdpr.py
from compliance.gdpr_checker import GDPRComplianceChecker


def test_empty_activities(self):
    checker = GDPRComplianceChecker([])
    report = checker.check_compliance()
    self.assertFalse(report['article_5']['requirements']['lawfulness']['status'])