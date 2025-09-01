# Deployment Guide

## 🚀 GitHub Setup

### 1. Initialize Git Repository
```bash
cd /Users/mshailes/Documents/IITB-Upgrad/NYC-Taxi-assignment
git init
git add .
git commit -m "Initial commit: NYC Taxi Analysis project"
```

### 2. Create GitHub Repository
1. Go to GitHub.com and create a new repository named `nyc-taxi-analysis`
2. Add remote origin:
```bash
git remote add origin https://github.com/yourusername/nyc-taxi-analysis.git
git branch -M main
git push -u origin main
```

## 🖥️ EC2 Deployment

### 1. Connect to EC2
```bash
ssh -i ai-security-key.pem ubuntu@18.215.244.56
```

### 2. Setup Project
```bash
# Download and run setup script
wget https://raw.githubusercontent.com/yourusername/nyc-taxi-analysis/main/setup_ec2.sh
chmod +x setup_ec2.sh
./setup_ec2.sh
```

### 3. Configure Security Groups
Add inbound rule for Jupyter Notebook:
- Type: Custom TCP
- Port: 8888
- Source: Your IP address

### 4. Start Jupyter Notebook
```bash
cd ~/nyc-taxi-analysis
source venv/bin/activate
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### 5. Access Analysis
Open browser: `http://18.215.244.56:8888`

## 📊 Data Upload Options

### Option 1: SCP Upload
```bash
scp -i ai-security-key.pem -r data/processed/ ubuntu@18.215.244.56:~/nyc-taxi-analysis/data/
```

### Option 2: Download Sample Data
```bash
# On EC2 instance
cd ~/nyc-taxi-analysis/data/processed/
wget https://your-data-source.com/nyc_taxi_sample.parquet
```

## 🔧 Troubleshooting

### Memory Issues
If running out of memory:
```bash
# Check memory usage
free -h

# Use smaller sample size in data_processing.py
# Modify sample_rate parameter to 0.001 or smaller
```

### Port Issues
If port 8888 is busy:
```bash
jupyter notebook --ip=0.0.0.0 --port=8889 --no-browser --allow-root
```

### Permission Issues
```bash
sudo chown -R ubuntu:ubuntu ~/nyc-taxi-analysis
chmod -R 755 ~/nyc-taxi-analysis
```

## 💰 Cost Management

### Stop Instance When Not in Use
```bash
aws ec2 stop-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1
```

### Start Instance
```bash
aws ec2 start-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1
```

## 📝 Notes
- Instance ID: `i-03fbaf1cb5414c674`
- Region: `us-east-1`
- Key file: `ai-security-key.pem`
- Public IP may change after restart
