import numpy as np
from scipy import stats

class TCloseness:
    def __init__(self, dataframe, quasi_identifiers, sensitive_attribute):
        self.dataframe = dataframe
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute
        
    def earth_movers_distance(self, p, q):
        """Calculate Earth Mover's Distance between two distributions"""
        return stats.wasserstein_distance(p, q)
        
    def check_t_closeness(self, t):
        """Check if dataset satisfies t-closeness"""
        global_dist = self._get_distribution(self.dataframe[self.sensitive_attribute])
        
        groups = self.dataframe.groupby(self.quasi_identifiers)
        for _, group in groups:
            local_dist = self._get_distribution(group[self.sensitive_attribute])
            emd = self.earth_movers_distance(local_dist, global_dist)
            if emd > t:
                return False
        return True
        
    def _get_distribution(self, series):
        """Get probability distribution of a series"""
        value_counts = series.value_counts(normalize=True)
        return value_counts.to_dict()