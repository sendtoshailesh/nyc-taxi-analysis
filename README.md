# NYC Yellow Taxi Data Analysis 🚕

A comprehensive exploratory data analysis (EDA) of New York City Yellow Taxi trip data from 2023, providing actionable insights for taxi operations optimization.

## 📊 Project Overview

This project analyzes 6.4+ million taxi trips to uncover patterns in demand, pricing, and geographic distribution that can inform strategic decisions for taxi operations in NYC.

### Key Findings
- **Peak Hours**: 5-7 PM weekdays generate 2.5M+ trips per hour
- **Revenue Concentration**: Q2 and Q4 contribute 53.54% of annual revenue  
- **Strong Correlations**: 0.96 fare-distance, 0.8007 tip-distance correlation
- **Payment Trends**: 81.62% credit card usage, 17.57% average tip rate

## 🗂️ Project Structure

```
├── notebooks/
│   └── EDA_NYC_Taxi_Analysis.ipynb    # Main analysis notebook
├── data/
│   ├── processed/                      # Cleaned datasets
│   └── raw/                           # Original parquet files (not included)
├── reports/
│   ├── NYC_Taxi_Analysis_Report.pdf   # Final report
│   └── NYC_Taxi_Analysis_Report.md    # Markdown version
├── src/
│   ├── data_processing.py             # Data cleaning utilities
│   └── visualization.py              # Plotting functions
├── requirements.txt                   # Python dependencies
└── README.md                         # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- 8GB+ RAM (for full dataset processing)

### Installation
```bash
git clone https://github.com/yourusername/nyc-taxi-analysis.git
cd nyc-taxi-analysis
pip install -r requirements.txt
```

### Usage
```bash
# Launch Jupyter notebook
jupyter notebook notebooks/EDA_NYC_Taxi_Analysis.ipynb

# Or run analysis script
python src/data_processing.py
```

## 📈 Analysis Highlights

### Temporal Patterns
- **Weekday peaks**: 8-9 AM, 5-7 PM
- **Weekend patterns**: More distributed throughout day
- **Seasonal trends**: Higher demand in Q2 and Q4

### Geographic Insights
- **Top pickup**: JFK Airport (19,033 trips)
- **Manhattan dominance**: 80%+ of all trips
- **Airport routes**: Premium pricing opportunities

### Economic Analysis
- **Distance-based pricing**: $2.50 base + $2.50/mile average
- **Passenger economics**: Clear cost efficiency with higher passenger counts
- **Payment preferences**: Credit cards dominate (81.62%)

## 🛠️ Technical Details

### Data Processing
- **Sampling strategy**: Hourly stratified sampling across all dates
- **Data quality**: 96.6% retention after cleaning
- **Size reduction**: 6.4M → 363K records (representative sample)

### Technologies Used
- **Python**: pandas, numpy, matplotlib, seaborn
- **Jupyter**: Interactive analysis environment
- **Parquet**: Efficient data storage format

## 📋 Requirements

See `requirements.txt` for complete dependencies:
- pandas>=2.0.0
- numpy>=1.24.0
- matplotlib>=3.7.0
- seaborn>=0.12.0
- jupyter>=1.0.0

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/analysis-enhancement`)
3. Commit changes (`git commit -am 'Add new analysis'`)
4. Push to branch (`git push origin feature/analysis-enhancement`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Academic Context

This project was completed as part of the IITB-Upgrad Data Science program, demonstrating practical application of exploratory data analysis techniques on real-world transportation data.

## 📞 Contact

**Author**: Shailesh Mishra  
**LinkedIn**: https://www.linkedin.com/in/shaileshmishra1/

---

*For detailed analysis and insights, see the [full report](reports/NYC_Taxi_Analysis_Report.pdf)*
