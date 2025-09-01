# EC2 Quick Reference Card

## 🔐 SSH Connection
```bash
ssh -i ai-security-key.pem ubuntu@18.215.244.56
```

## 📁 Code Location
```bash
cd ~/ai-security-code-examples
```

## 🧪 Test Security Examples
```bash
# Traditional security (fails against AI)
python3 traditional-security/pattern_based_security.py

# AI-aware security (succeeds)
python3 ai-aware-security/semantic_security.py
```

## 🛡️ Run Promptfoo Security Tests
```bash
export OPENAI_API_KEY='your-key'
promptfoo redteam run --config promptfoo-configs/emergency-security.yaml
```

## 🤖 Amazon Q CLI
```bash
q --version
q "How do I secure AI applications?"
```

## 💰 Cost Management
```bash
# Stop instance (saves money)
aws ec2 stop-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1

# Start instance
aws ec2 start-instances --instance-ids i-03fbaf1cb5414c674 --region us-east-1
```

**Instance ID**: `i-03fbaf1cb5414c674`  
**Region**: `us-east-1`  
**Key**: `ai-security-key.pem`
