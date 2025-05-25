import pandas as pd
from collections import defaultdict

class KAnonymity:
    def __init__(self, dataframe, quasi_identifiers):
        self.dataframe = dataframe
        self.quasi_identifiers = quasi_identifiers
        
    def check_k_anonymity(self, k):
        groups = self.dataframe.groupby(self.quasi_identifiers)
        return all(len(group) >= k for _, group in groups)
    
    def generalize(self, column, hierarchy):
        """Generalize data based on predefined hierarchy"""
        self.dataframe[column] = self.dataframe[column].map(hierarchy)
        
    def suppress(self, column, threshold):
        """Suppress values that appear less than threshold times"""
        counts = self.dataframe[column].value_counts()
        to_suppress = counts[counts < threshold].index
        self.dataframe.loc[self.dataframe[column].isin(to_suppress), column] = '*'
    
    def achieve_k_anonymity(self, k):
        """Automatically generalize columns to achieve k-anonymity"""
        while not self.check_k_anonymity(k):
            for column in self.quasi_identifiers:
                unique_counts = self.dataframe[column].value_counts()
                if len(unique_counts) > 1:
                    most_common = unique_counts.idxmax()
                    self.dataframe[column] = most_common
        return self.dataframe