"""
NYC Taxi Data Processing Module
Handles data loading, cleaning, and preprocessing for taxi trip analysis.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class TaxiDataProcessor:
    """Main class for processing NYC taxi data"""
    
    def __init__(self, data_dir='data/raw/'):
        self.data_dir = data_dir
        self.df = None
        
    def load_sample_data(self, sample_rate=0.01):
        """Load and sample data from all monthly files"""
        file_list = [f for f in os.listdir(self.data_dir) if f.endswith('.parquet')]
        print(f"Found {len(file_list)} parquet files")
        
        dfs = []
        for file in sorted(file_list):
            df_month = pd.read_parquet(os.path.join(self.data_dir, file))
            # Stratified sampling by hour
            df_sample = df_month.groupby(df_month['tpep_pickup_datetime'].dt.hour).apply(
                lambda x: x.sample(frac=sample_rate, random_state=42)
            ).reset_index(drop=True)
            dfs.append(df_sample)
            
        self.df = pd.concat(dfs, ignore_index=True)
        print(f"Loaded {len(self.df)} records")
        return self.df
    
    def clean_data(self):
        """Clean and preprocess the data"""
        if self.df is None:
            raise ValueError("No data loaded. Call load_sample_data() first.")
            
        initial_count = len(self.df)
        
        # Remove outliers
        self.df = self.df[
            (self.df['trip_distance'] > 0) & 
            (self.df['trip_distance'] <= 100) &
            (self.df['fare_amount'] > 0) &
            (self.df['fare_amount'] <= 500) &
            (self.df['passenger_count'] > 0) &
            (self.df['passenger_count'] <= 6)
        ]
        
        # Handle missing values
        self.df['passenger_count'].fillna(1, inplace=True)
        self.df['RatecodeID'].fillna(1, inplace=True)
        
        # Add derived features
        self.df['trip_duration'] = (
            self.df['tpep_dropoff_datetime'] - self.df['tpep_pickup_datetime']
        ).dt.total_seconds() / 60
        
        self.df['pickup_hour'] = self.df['tpep_pickup_datetime'].dt.hour
        self.df['pickup_day'] = self.df['tpep_pickup_datetime'].dt.day_name()
        self.df['pickup_month'] = self.df['tpep_pickup_datetime'].dt.month
        
        final_count = len(self.df)
        retention_rate = (final_count / initial_count) * 100
        print(f"Data cleaning complete. Retention rate: {retention_rate:.1f}%")
        
        return self.df
    
    def save_processed_data(self, filename='nyc_taxi_cleaned.parquet'):
        """Save processed data"""
        if self.df is None:
            raise ValueError("No data to save.")
            
        filepath = os.path.join('data/processed/', filename)
        self.df.to_parquet(filepath, index=False)
        print(f"Processed data saved to {filepath}")

if __name__ == "__main__":
    # Example usage
    processor = TaxiDataProcessor('Data/trip_records/')
    df = processor.load_sample_data(sample_rate=0.01)
    df_clean = processor.clean_data()
    processor.save_processed_data()
