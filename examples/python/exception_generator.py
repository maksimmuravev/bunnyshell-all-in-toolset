from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Initialize Sentry SDK
sentry_sdk.init(
    dsn="https://d8490b5b17d24a74baec541d0f2b3df5@sentry-7f3qqz.bunnyenv.com/2",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/')
def index():
    try:
        raise Exception("Something went wrong!")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return 'Exception sent to Sentry!'

@app.route('/hello')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
