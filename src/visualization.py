"""
NYC Taxi Data Visualization Module
Contains plotting functions for taxi trip analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
plt.style.use('default')
sns.set_palette("husl")

class TaxiVisualizer:
    """Main class for creating taxi data visualizations"""
    
    def __init__(self, df):
        self.df = df
        
    def plot_temporal_patterns(self, figsize=(15, 10)):
        """Plot temporal patterns in taxi demand"""
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Hourly patterns
        hourly_trips = self.df.groupby('pickup_hour').size()
        axes[0,0].bar(hourly_trips.index, hourly_trips.values)
        axes[0,0].set_title('Trips by Hour of Day')
        axes[0,0].set_xlabel('Hour')
        axes[0,0].set_ylabel('Number of Trips')
        
        # Daily patterns
        daily_trips = self.df.groupby('pickup_day').size()
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_trips = daily_trips.reindex(day_order)
        axes[0,1].bar(daily_trips.index, daily_trips.values)
        axes[0,1].set_title('Trips by Day of Week')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # Monthly patterns
        monthly_trips = self.df.groupby('pickup_month').size()
        axes[1,0].bar(monthly_trips.index, monthly_trips.values)
        axes[1,0].set_title('Trips by Month')
        axes[1,0].set_xlabel('Month')
        
        # Heatmap: Hour vs Day
        pivot_data = self.df.groupby(['pickup_day', 'pickup_hour']).size().unstack(fill_value=0)
        pivot_data = pivot_data.reindex(day_order)
        sns.heatmap(pivot_data, ax=axes[1,1], cmap='YlOrRd')
        axes[1,1].set_title('Trip Demand Heatmap')
        
        plt.tight_layout()
        return fig
    
    def plot_fare_analysis(self, figsize=(12, 8)):
        """Plot fare-related analysis"""
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        # Fare distribution
        axes[0,0].hist(self.df['fare_amount'], bins=50, alpha=0.7)
        axes[0,0].set_title('Fare Amount Distribution')
        axes[0,0].set_xlabel('Fare Amount ($)')
        
        # Distance vs Fare
        sample_data = self.df.sample(n=min(5000, len(self.df)))
        axes[0,1].scatter(sample_data['trip_distance'], sample_data['fare_amount'], alpha=0.5)
        axes[0,1].set_title('Distance vs Fare')
        axes[0,1].set_xlabel('Trip Distance (miles)')
        axes[0,1].set_ylabel('Fare Amount ($)')
        
        # Payment type distribution
        payment_counts = self.df['payment_type'].value_counts()
        axes[1,0].pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%')
        axes[1,0].set_title('Payment Type Distribution')
        
        # Tip analysis (credit card only)
        cc_data = self.df[self.df['payment_type'] == 1]
        if len(cc_data) > 0:
            cc_data['tip_percentage'] = (cc_data['tip_amount'] / cc_data['fare_amount']) * 100
            axes[1,1].hist(cc_data['tip_percentage'], bins=30, alpha=0.7)
            axes[1,1].set_title('Tip Percentage Distribution (Credit Card)')
            axes[1,1].set_xlabel('Tip Percentage (%)')
        
        plt.tight_layout()
        return fig
    
    def plot_geographic_patterns(self, figsize=(12, 6)):
        """Plot geographic patterns"""
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Top pickup locations
        top_pickups = self.df['PULocationID'].value_counts().head(10)
        axes[0].barh(range(len(top_pickups)), top_pickups.values)
        axes[0].set_yticks(range(len(top_pickups)))
        axes[0].set_yticklabels(top_pickups.index)
        axes[0].set_title('Top 10 Pickup Locations')
        axes[0].set_xlabel('Number of Trips')
        
        # Top dropoff locations
        top_dropoffs = self.df['DOLocationID'].value_counts().head(10)
        axes[1].barh(range(len(top_dropoffs)), top_dropoffs.values)
        axes[1].set_yticks(range(len(top_dropoffs)))
        axes[1].set_yticklabels(top_dropoffs.index)
        axes[1].set_title('Top 10 Dropoff Locations')
        axes[1].set_xlabel('Number of Trips')
        
        plt.tight_layout()
        return fig
    
    def correlation_heatmap(self, figsize=(10, 8)):
        """Create correlation heatmap for numerical variables"""
        numerical_cols = ['trip_distance', 'fare_amount', 'tip_amount', 
                         'total_amount', 'passenger_count', 'trip_duration']
        
        # Filter columns that exist in the dataframe
        available_cols = [col for col in numerical_cols if col in self.df.columns]
        
        if len(available_cols) < 2:
            print("Not enough numerical columns for correlation analysis")
            return None
            
        corr_matrix = self.df[available_cols].corr()
        
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        ax.set_title('Correlation Matrix - Taxi Trip Variables')
        
        plt.tight_layout()
        return fig

def create_summary_dashboard(df, save_path=None):
    """Create a comprehensive dashboard"""
    visualizer = TaxiVisualizer(df)
    
    # Create all plots
    fig1 = visualizer.plot_temporal_patterns()
    fig2 = visualizer.plot_fare_analysis()
    fig3 = visualizer.plot_geographic_patterns()
    fig4 = visualizer.correlation_heatmap()
    
    if save_path:
        fig1.savefig(f"{save_path}_temporal.png", dpi=300, bbox_inches='tight')
        fig2.savefig(f"{save_path}_fare.png", dpi=300, bbox_inches='tight')
        fig3.savefig(f"{save_path}_geographic.png", dpi=300, bbox_inches='tight')
        if fig4:
            fig4.savefig(f"{save_path}_correlation.png", dpi=300, bbox_inches='tight')
    
    plt.show()
    
    return fig1, fig2, fig3, fig4
