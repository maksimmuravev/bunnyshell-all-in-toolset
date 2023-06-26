# Fetch Customers App

## 📄 Description
The Fetch Customers App is a Node.js web application example built with Express. It demonstrates how to use OpenTelemetry for tracing in an Express application. The application fetches customer data from a faked database (actually there is not database – just text) and sends it as a JSON response. The tracing information is exported using the OTLP HTTP Exporter and can be visualized and analyzed using an OpenTelemetry-compatible tools like Jaeger and Zipkin.

## ⚙️ App Details

| Language | Framework     | All-In Toolset Part     |
| -------- | ------------- | ----------------------- |
| Node.js  | Express       | OpenTelemetry           |

## 🚀 Prerequisites
To run this application, you'll need the following:
- Node.js installed on your machine (successfully tested on 20.3.1)

## 📖 Usage
1. Clone this repository or download the source code.
2. Install the required dependencies using `npm install`.
3. Run the application using `node start`.
4. Access the API by sending a GET request to `http://localhost:3000/api/customers`.

## 📜 Tracing
The application utilizes OpenTelemetry for distributed tracing. It creates a basic tracer provider with a configured OTLP HTTP exporter. Tracing is enabled for the Express application, and a span is started and ended for each request to the `/api/customers` route. The tracing information is exported to the specified endpoint URL for further analysis via one of two visualising tools: Jaeger or Zipkin.

## 📄 License
This project is licensed under the [MIT License](./LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
   \
 /)  /)
( •-• )
/づづ
```
