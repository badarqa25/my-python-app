from flask import Flask

application = Flask(__name__)  # Not app = Flask(__name__)

@application.route('/')
def home():
    return "Hello from AWS Elastic Beanstalk!"
