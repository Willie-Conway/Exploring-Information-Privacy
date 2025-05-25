import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import networkx as nx
from typing import Dict, List

class PrivacyVisualizer:
    @staticmethod
    def show_gdpr_compliance(compliance_report: Dict) -> plt.Figure:
        """
        Visualize GDPR compliance status as a heatmap
        Args:
            compliance_report: Dictionary from GDPRComplianceChecker
        Returns:
            matplotlib Figure object
        """
        article_data = []
        for article, details in compliance_report.items():
            if 'requirements' in details:
                for req, status in details['requirements'].items():
                    article_data.append({
                        'article': article.replace('_', ' ').title(),
                        'requirement': req.replace('_', ' ').title(),
                        'status': status['status']
                    })
            elif 'lawful_bases' in details:
                for basis, status in details['lawful_bases'].items():
                    article_data.append({
                        'article': article.replace('_', ' ').title(),
                        'requirement': basis.replace('_', ' ').title(),
                        'status': status['status']
                    })
            else:
                article_data.append({
                    'article': article.replace('_', ' ').title(),
                    'requirement': 'Implementation',
                    'status': details['status']
                })
        
        df = pd.DataFrame(article_data)
        pivot = df.pivot_table(index='article', columns='requirement', 
                             values='status', aggfunc='first')
        
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(pivot == 'implemented', cmap=['#ff6b6b', '#51cf66'], 
                   ax=ax, cbar_kws={'label': 'Implemented'})
        ax.set_title('GDPR Compliance Status', pad=20, fontsize=16)
        ax.set_xlabel('Requirements', fontsize=12)
        ax.set_ylabel('GDPR Articles', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_data_flow(flow_data: List[tuple]) -> plt.Figure:
        """
        Visualize data flows between systems
        Args:
            flow_data: List of tuples (source, target, {metadata})
        Returns:
            matplotlib Figure object
        """
        G = nx.DiGraph()
        
        for source, target, data in flow_data:
            G.add_edge(source, target, **data)
            
        pos = nx.spring_layout(G, k=0.5, iterations=50)
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Draw nodes with different styles for sources and targets
        sources = {n for n, d in G.in_degree() if d == 0}
        nx.draw_networkx_nodes(
            G, pos, nodelist=sources, 
            node_size=2000, node_color='#74c0fc', ax=ax
        )
        nx.draw_networkx_nodes(
            G, pos, nodelist=set(G.nodes()) - sources,
            node_size=2000, node_color='#ff8787', ax=ax
        )
        
        # Draw edges with arrows
        nx.draw_networkx_edges(
            G, pos, arrowstyle='->', arrowsize=20, 
            edge_color='#495057', width=2, ax=ax
        )
        
        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', ax=ax)
        
        # Add edge labels
        edge_labels = {
            (u, v): d.get('data_type', '') 
            for u, v, d in G.edges(data=True)
        }
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels,
            font_color='#343a40', ax=ax
        )
        
        ax.set_title('Data Flow Map', fontsize=16)
        ax.axis('off')
        return fig

    @staticmethod
    def save_visualization(fig: plt.Figure, filename: str) -> None:
        """Save visualization to file"""
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close(fig)