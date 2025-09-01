#!/bin/bash

# NYC Taxi Analysis - EC2 Deployment Commands
# Run these commands step by step on your EC2 instance

echo "🚕 NYC Taxi Analysis - EC2 Setup Commands"
echo "=========================================="
echo ""

echo "1️⃣ Connect to EC2:"
echo "ssh -i ai-security-key.pem ubuntu@18.215.244.56"
echo ""

echo "2️⃣ Update system and install dependencies:"
echo "sudo apt update && sudo apt upgrade -y"
echo "sudo apt install -y python3 python3-pip python3-venv git htop"
echo ""

echo "3️⃣ Clone the project:"
echo "cd ~"
echo "git clone https://github.com/yourusername/nyc-taxi-analysis.git"
echo "cd nyc-taxi-analysis"
echo ""

echo "4️⃣ Setup Python environment:"
echo "python3 -m venv venv"
echo "source venv/bin/activate"
echo "pip install --upgrade pip"
echo "pip install -r requirements.txt"
echo ""

echo "5️⃣ Create directories:"
echo "mkdir -p data/raw data/processed output logs"
echo ""

echo "6️⃣ Test installation:"
echo "python quick_start.py"
echo ""

echo "7️⃣ Start Jupyter Notebook:"
echo "jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
echo ""

echo "8️⃣ Access Jupyter in browser:"
echo "http://18.215.244.56:8888"
echo ""

echo "⚠️  Security Group Configuration:"
echo "Add inbound rule: Custom TCP, Port 8888, Source: Your IP"
echo ""

echo "💰 Cost Management:"
echo "Stop instance: aws ec2 stop-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1"
echo "Start instance: aws ec2 start-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1"
