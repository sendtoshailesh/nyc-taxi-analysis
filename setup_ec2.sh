#!/bin/bash

# NYC Taxi Analysis - EC2 Setup Script
# This script sets up the project environment on EC2

echo "🚕 Setting up NYC Taxi Analysis Project on EC2..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip if not already installed
sudo apt install -y python3 python3-pip python3-venv git

# Create project directory
mkdir -p ~/nyc-taxi-analysis
cd ~/nyc-taxi-analysis

# Clone the repository (replace with your GitHub URL)
echo "📥 Cloning repository..."
git clone https://github.com/yourusername/nyc-taxi-analysis.git .

# Create virtual environment
echo "🐍 Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
mkdir -p data/raw data/processed logs

# Set permissions
chmod +x setup_ec2.sh

echo "✅ Setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Upload your data files to data/raw/"
echo "3. Run analysis: python src/data_processing.py"
echo "4. Start Jupyter: jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser"
echo ""
echo "🔗 Access Jupyter at: http://18.215.244.56:8888"
echo "⚠️  Remember to configure security groups for port 8888"
