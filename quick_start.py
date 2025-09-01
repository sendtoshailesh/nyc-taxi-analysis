#!/usr/bin/env python3
"""
Quick Start Script for NYC Taxi Analysis
Run this script to perform basic analysis with sample data
"""

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Add src to path
sys.path.append('src')

try:
    from data_processing import TaxiDataProcessor
    from visualization import TaxiVisualizer
except ImportError:
    print("❌ Could not import modules. Make sure you're in the project root directory.")
    sys.exit(1)

def main():
    print("🚕 NYC Taxi Analysis - Quick Start")
    print("=" * 40)
    
    # Check if processed data exists
    processed_file = 'data/processed/nyc_taxi_cleaned.parquet'
    
    if os.path.exists(processed_file):
        print("📊 Loading processed data...")
        df = pd.read_parquet(processed_file)
    else:
        print("📥 Processing raw data...")
        # Check if raw data exists
        if not os.path.exists('Data/trip_records/'):
            print("❌ Raw data not found. Please ensure data files are in Data/trip_records/")
            print("💡 You can download sample data or use the full dataset")
            return
            
        processor = TaxiDataProcessor('Data/trip_records/')
        df = processor.load_sample_data(sample_rate=0.005)  # Small sample for quick demo
        df = processor.clean_data()
        processor.save_processed_data()
    
    print(f"✅ Data loaded: {len(df):,} records")
    
    # Basic statistics
    print("\n📈 Basic Statistics:")
    print(f"Date range: {df['tpep_pickup_datetime'].min()} to {df['tpep_pickup_datetime'].max()}")
    print(f"Average fare: ${df['fare_amount'].mean():.2f}")
    print(f"Average distance: {df['trip_distance'].mean():.2f} miles")
    print(f"Total revenue: ${df['fare_amount'].sum():,.2f}")
    
    # Create visualizations
    print("\n📊 Creating visualizations...")
    visualizer = TaxiVisualizer(df)
    
    # Create output directory
    os.makedirs('output', exist_ok=True)
    
    # Generate plots
    fig1 = visualizer.plot_temporal_patterns()
    fig1.savefig('output/temporal_patterns.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    fig2 = visualizer.plot_fare_analysis()
    fig2.savefig('output/fare_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print("✅ Analysis complete!")
    print("📁 Check the 'output' folder for visualizations")
    print("🚀 Run 'jupyter notebook notebooks/EDA_NYC_Taxi_Analysis.ipynb' for detailed analysis")

if __name__ == "__main__":
    main()
