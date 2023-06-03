from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Initialize Sentry SDK
# Examples of DSN is "https://d8490b5b17d24a74baec541d0f2b3df5@sentry-7f3qqz.bunnyenv.com/2"
# Where 2 is the Sentry project's "PROJECT_ID"
sentry_sdk.init(
    dsn="https://d8490b5b17d24a74baec541d0f2b3df5@sentry-7f3qqz.bunnyenv.com/2",
    integrations=[FlaskIntegration()]
)

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def index():
    try:
        raise Exception("Something went wrong!")  # Raises an exception intentionally
    except Exception as e:
        sentry_sdk.capture_exception(e)  # Captures the exception and sends it to Sentry for error tracking
        return 'Exception sent to Sentry!'  # Returns a response indicating that the exception was sent to Sentry

# Define a route for '/hello'
@app.route('/hello')
def hello():
    return 'Hello, Flask!'  # Returns a simple greeting message

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Starts the Flask development server with debugging enabled
