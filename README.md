# My Python Flask App on AWS Elastic Beanstalk

This project is a simple Python Flask web application deployed to **AWS Elastic Beanstalk**. It uses **Terraform** for infrastructure provisioning and supports modern platform versions (Python 3.11 on Amazon Linux 2023).

## 🚀 Features

- Flask application with basic routing
- Deployed using AWS Elastic Beanstalk CLI
- Terraform used for VPC, EC2, and IAM configuration (optional)
- Easy to deploy and scale

## 🛠 Project Structure

my-python-app/
│
├── application.py # Main Flask app
├── requirements.txt # Python dependencies
├── .elasticbeanstalk/ # EB config
├── Procfile # Startup command for EB
├── .gitignore
└── README.md

bash
Copy
Edit

## 📦 Installation & Setup

1. **Clone the project**
   ```bash
   git clone https://github.com/badarqa25/my-python-app.git
   cd my-python-app
**Install dependencies**
pip install -r requirements.txt

**Run Locally**
python application.py

**Deploy to AWS Elastic Beanstalk**
eb init -p "Python 3.11 running on 64bit Amazon Linux 2023" my-python-app
eb create my-env
eb deploy

**Visit your app**
You’ll get a public URL from Elastic Beanstalk (e.g., http://my-env-v2.eba-nbpg9g5y.us-east-1.elasticbeanstalk.com/)
