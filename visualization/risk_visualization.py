import matplotlib.pyplot as plt
import numpy as np

class RiskVisualizer:
    def __init__(self, risk_data):
        self.risk_data = risk_data
        
    def plot_risk_matrix(self):
        """Create a risk matrix visualization"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Define risk categories
        likelihood = ['Rare', 'Unlikely', 'Possible', 'Likely', 'Certain']
        impact = ['Negligible', 'Minor', 'Moderate', 'Major', 'Severe']
        
        # Create grid
        for i in range(len(likelihood)):
            for j in range(len(impact)):
                risk_level = i * j
                color = self._get_risk_color(risk_level)
                ax.add_patch(plt.Rectangle((i, j), 1, 1, facecolor=color, edgecolor='black'))
                ax.text(i + 0.5, j + 0.5, f'L{i+1}I{j+1}', 
                       ha='center', va='center', color='black')
        
        # Add actual risks
        for risk in self.risk_data:
            l, i = risk['likelihood'], risk['impact']
            ax.plot(l + 0.5, i + 0.5, 'ro', markersize=10)
            ax.text(l + 0.5, i + 0.5 + 0.2, risk['name'], 
                   ha='center', va='center', color='red')
        
        ax.set_xlim(0, len(likelihood))
        ax.set_ylim(0, len(impact))
        ax.set_xticks(np.arange(0.5, len(likelihood) + 0.5))
        ax.set_yticks(np.arange(0.5, len(impact) + 0.5))
        ax.set_xticklabels(likelihood)
        ax.set_yticklabels(impact)
        ax.set_xlabel('Likelihood')
        ax.set_ylabel('Impact')
        ax.set_title('Privacy Risk Matrix')
        plt.tight_layout()
        return fig
    
    def _get_risk_color(self, level):
        """Get color based on risk level"""
        if level < 4:
            return 'lightgreen'
        elif level < 8:
            return 'yellow'
        elif level < 12:
            return 'orange'
        else:
            return 'red'
    
    def plot_risk_distribution(self):
        """Plot distribution of risk levels"""
        levels = [risk['level'] for risk in self.risk_data]
        counts = {
            'Low': sum(1 for l in levels if l == 'Low'),
            'Medium': sum(1 for l in levels if l == 'Medium'),
            'High': sum(1 for l in levels if l == 'High')
        }
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(counts.keys(), counts.values(), color=['green', 'yellow', 'red'])
        ax.set_title('Distribution of Privacy Risks')
        ax.set_ylabel('Number of Risks')
        ax.set_xlabel('Risk Level')
        
        for i, v in enumerate(counts.values()):
            ax.text(i, v + 0.5, str(v), ha='center')
            
        return fig