import pandas as pd
import os

def add_fraud_status_column(input_file, output_file_excel):
    try:
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"File not found: {input_file}")
        
        df = pd.read_csv(input_file)
        
        if 'Fraud' not in df.columns:
            raise ValueError("'Fraud' column not found in the dataset.")
        
        df['FraudStatus'] = df['Fraud'].apply(lambda x: 'Fraud' if x == 1 else 'Not Fraud')
        
        df.to_excel(output_file_excel, index=False)
        print(f"✅ Excel file saved to: {output_file_excel}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

# ✅ Corrected main guard
if __name__ == "__main__":
    input_csv = "fraud_detection_results.csv"
    output_excel = "fraud_detection_results_with_status.xlsx"
    add_fraud_status_column(input_csv, output_excel)
