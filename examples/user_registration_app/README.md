# User Registration App

## Description
The User Registration App is a Python web application example that allows users to register by providing their username and email. It demonstrates a basic user registration process with logging functionality integrated using Grafana+Vector+Loki.

The application showcases how to handle user registration requests, perform basic business logic, and send logs to Loki for logging, monitoring and analysis.

## App Details

| Language  | Framework | All-In Toolset Part |
|-----------|-----------|---------------------|
| Python    | Flask     | Grafana+Vector+Loki |

## Prerequisites
To run this application, you'll need the following:
- Python 3.x
- Flask (install via `pip install flask`)

## Usage
1. Clone this repository or download the source code.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python app.py`.
4. Access the application by navigating to `http://localhost:5000` in your web browser.
5. To register a new user, make a POST request to `http://localhost:5000/register` with the following parameters:
```bash
curl -X POST -d "username=johndoe&email=johndoe@example.com" http://localhost:5000/register
```

## Logging
The application is configured to send logs to Loki, a powerful log aggregation system. The logs are sent using the provided logging mechanism in the code, which can be customized based on your Loki setup. Ensure that the `vector_host` and `vector_url` variables in `app.py` are correctly set to match your Loki configuration.

## License
This project is licensed under the [MIT License](LICENSE).

