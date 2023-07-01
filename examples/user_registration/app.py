import time
import logging
import logging.handlers
import random
from flask import Flask, request

app = Flask(__name__)

vector_host = 'vector-4ju2m4.bunnyenv.com'
vector_url = '/'
handler = logging.handlers.HTTPHandler(vector_host, vector_url, method='POST', secure=True)

logging.basicConfig(encoding="utf-8", level=logging.INFO, handlers=[handler])

@app.route('/')
def index():
    return 'Welcome to the User Registration App!'

@app.route('/register', methods=['POST'])
def register_user():
    username = request.form.get('username')
    email = request.form.get('email')
    
    # Business logic: Simulating user registration
    # In a real-life application, you would perform database operations or other actions here
    if username and email:
        logging.info(f'New user registered! Username: {username}, Email: {email}')
        return 'User registered successfully!'
    else:
        logging.warning('Failed to register user: invalid data')
        return 'Invalid data. User registration failed.'

if __name__ == '__main__':
    app.run()

