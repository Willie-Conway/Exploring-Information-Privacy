import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend before other imports
import pandas as pd
import json
from datetime import datetime
from pathlib import Path
import os
from data_anonymization.k_anonymity import KAnonymity
from data_anonymization.l_diversity import LDiversity
from encryption.homomorphic_encryption import HomomorphicEncryption
from encryption.differential_privacy import DifferentialPrivacy
from privacy_assessment.privacy_risk_assessment import PrivacyRiskAssessor
from compliance.gdpr_checker import GDPRComplianceChecker
from visualization.privacy_heatmap import PrivacyVisualizer

def setup_demo_data() -> dict:
    """Create sample dataset for demonstration"""
    return {
        'age': [23, 27, 28, 25, 23, 27, 28, 25, 23, 27],
        'zipcode': ['10001', '10002', '10003', '10001', '10002', '10003', 
                   '10001', '10002', '10003', '10001'],
        'disease': ['Flu', 'Cold', 'HIV', 'Diabetes', 'Flu', 
                   'Cold', 'HIV', 'Diabetes', 'Flu', 'Cold']
    }

def run_privacy_demo() -> dict:
    """Execute all privacy demonstrations"""
    results = {'timestamp': datetime.now().isoformat()}
    df = pd.DataFrame(setup_demo_data())
    
    # 1. Anonymization Techniques
    print("\n=== K-Anonymity Demonstration ===")
    k_anon = KAnonymity(df.copy(), ['age', 'zipcode'])
    results['k_anonymity'] = {
        'original_2_anon': k_anon.check_k_anonymity(2),
        'generalized_2_anon': False
    }
    
    k_anon.generalize('age', {23: '20-30', 25: '20-30', 27: '20-30', 28: '20-30'})
    results['k_anonymity']['generalized_2_anon'] = k_anon.check_k_anonymity(2)
    print(f"Original dataset satisfies 2-anonymity: {results['k_anonymity']['original_2_anon']}")
    print(f"After generalization: {results['k_anonymity']['generalized_2_anon']}")

    # 2. Diversity Metrics
    print("\n=== L-Diversity Demonstration ===")
    l_div = LDiversity(df, ['age', 'zipcode'], 'disease')
    results['l_diversity'] = l_div.check_l_diversity(2)
    print(f"Dataset satisfies 2-diversity: {results['l_diversity']}")

    # 3. Encryption Demonstrations
    print("\n=== Homomorphic Encryption Demonstration ===")
    he = HomomorphicEncryption()
    encrypted_values = [he.encrypt(x) for x in [10, 20, 30]]
    encrypted_sum = he.secure_sum(encrypted_values)
    results['homomorphic_encryption'] = {
        'encrypted_sum': str(encrypted_sum.ciphertext()),
        'decrypted_sum': he.decrypt(encrypted_sum)
    }
    print(f"Encrypted sum: {results['homomorphic_encryption']['encrypted_sum']} "
          f"(decrypted: {results['homomorphic_encryption']['decrypted_sum']})")

    # 4. Differential Privacy
    print("\n=== Differential Privacy Demonstration ===")
    dp = DifferentialPrivacy(epsilon=0.5)
    true_count = 100
    noisy_count = dp.laplace_mechanism(true_count, sensitivity=1)
    results['differential_privacy'] = {
        'true_value': true_count,
        'noisy_value': float(noisy_count),
        'epsilon': 0.5
    }
    print(f"True count: {true_count}, Noisy count: {noisy_count:.2f}")

    # 5. Privacy Risk Assessment
    print("\n=== Privacy Risk Assessment ===")
    assessor = PrivacyRiskAssessor(df)
    pii_columns = assessor.identify_pii()
    results['pii_detection'] = {
        'potential_pii': pii_columns,
        'risk_scores': {col: assessor.calculate_risk_score(col) 
                       for col in df.columns}
    }
    print(f"Potential PII columns: {pii_columns}")

    # 6. GDPR Compliance
    print("\n=== GDPR Compliance Check ===")
    activities = ['lawfulness', 'transparency', 'data_minimization']
    gdpr_checker = GDPRComplianceChecker(activities)
    compliance = gdpr_checker.check_compliance()
    results['gdpr_compliance'] = compliance
    print(f"Article 5 compliance: {compliance['article_5']['requirements']}")

    return results

def generate_report(results: dict) -> bool:
    """Generate comprehensive output files with robust error handling"""
    try:
        # 1. Determine output directory (try project folder first, then home directory)
        project_dir = Path(os.getcwd())
        output_dir = project_dir / "reports"
        
        try:
            output_dir.mkdir(exist_ok=True, mode=0o755)
        except Exception as e:
            print(f"⚠️ Couldn't create project reports directory: {e}")
            output_dir = Path.home() / "privacy_reports"
            output_dir.mkdir(exist_ok=True, mode=0o755)
            print(f"⚠️ Using fallback directory: {output_dir}")
        
        print(f"\n📁 Output directory: {output_dir.absolute()}")
        
        # 2. File paths
        json_path = output_dir / "privacy_report.json"
        gdpr_path = output_dir / "gdpr_compliance.png"
        flow_path = output_dir / "data_flow.png"
        
        # 3. Save JSON report
        try:
            with open(json_path, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"✅ JSON report saved to: {json_path}")
        except Exception as e:
            print(f"❌ Failed to save JSON report: {e}")
            return False

        # 4. Generate visualizations
        visualizer = PrivacyVisualizer()
        
        # GDPR Compliance Heatmap
        try:
            gdpr_fig = visualizer.show_gdpr_compliance(results['gdpr_compliance'])
            visualizer.save_visualization(gdpr_fig, str(gdpr_path))
            print(f"✅ GDPR visualization saved to: {gdpr_path}")
        except Exception as e:
            print(f"❌ Failed to create GDPR visualization: {e}")

        # Data Flow Map
        try:
            flow_data = [
                ('User Devices', 'Web Server', {'data_type': 'PII'}),
                ('Web Server', 'Database', {'data_type': 'Encrypted Data'}),
                ('Database', 'Analytics', {'data_type': 'Anonymized Data'})
            ]
            flow_fig = visualizer.plot_data_flow(flow_data)
            visualizer.save_visualization(flow_fig, str(flow_path))
            print(f"✅ Data flow diagram saved to: {flow_path}")
        except Exception as e:
            print(f"❌ Failed to create data flow diagram: {e}")

        # 5. Verify all files were created
        success = True
        for path in [json_path, gdpr_path, flow_path]:
            if not path.exists():
                print(f"❌ File missing: {path.name}")
                success = False
                
        return success
        
    except Exception as e:
        print(f"💥 Critical error in report generation: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=== Exploring Information Privacy ===")
    print("Running comprehensive privacy analysis...\n")
    
    # Debug: Show working environment
    print(f"Python version: {os.sys.version}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Directory contents: {os.listdir()}")
    
    try:
        results = run_privacy_demo()
        report_success = generate_report(results)
        
        if report_success:
            print("\n🎉 Report generation successful!")
            print("Check these files:")
            print(f"- {Path('reports/privacy_report.json').absolute()}")
            print(f"- {Path('reports/gdpr_compliance.png').absolute()}")
            print(f"- {Path('reports/data_flow.png').absolute()}")
        else:
            print("\n⚠️ Report generation completed with some errors")
            print("Check error messages above for details")
            
    except Exception as e:
        print(f"\n💥 Fatal error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()