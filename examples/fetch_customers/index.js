const express = require('express'); // Express framework
const { Resource } = require('@opentelemetry/resources'); // OpenTelemetry Resources
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions'); // OpenTelemetry Semantic Conventions
const { BasicTracerProvider, SimpleSpanProcessor } = require('@opentelemetry/sdk-trace-base'); // OpenTelemetry Tracer Provider
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http'); // OpenTelemetry OTLP HTTP Exporter
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express'); // OpenTelemetry Express Instrumentation

// Create a basic tracer provider
const provider = new BasicTracerProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'basic-service', // Set the service name for tracing
  }),
});

// Configure the OTLP HTTP exporter
const exporter = new OTLPTraceExporter({
  url: 'https://opentelemetry-g3mbdc.bunnyenv.com/v1/traces', // Specify the endpoint URL for trace export
});

// Add a span processor and register the tracer provider
provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.register();

// Initialize the Express instrumentation
const expressInstrumentation = new ExpressInstrumentation(); // Initialize the Express instrumentation
expressInstrumentation.setTracerProvider(provider); // Set the tracer provider for Express instrumentation

// Create an Express application
const app = express(); // Create an Express application

// Define a route that performs business logic
app.get('/api/customers', (req, res) => {
  const tracer = provider.getTracer('example-app'); // Get the tracer for the example app
  const span = tracer.startSpan('getCustomers', {
    attributes: {
      'http.method': req.method, // Capture the actual HTTP method used
      'http.route': req.path, // Capture the route requested
      'app.custom.attribute': 'some value', // Add a custom attribute specific to your application
    },
  }); // Start a new span with the name 'getCustomers'

  // Perform actual business logic here (fetch customers from the database)
  const customers = fetchCustomersFromDatabase(); // Fetch customers from the database
  res.json(customers); // Send the customers as JSON response

  span.end(); // End the span
});

// Simulated function to fetch customers from a database
function fetchCustomersFromDatabase() {
  // ... Perform actual database query and return results
  return [
    { id: 1, name: 'John Doe' },
    { id: 2, name: 'Jane Smith' },
  ];
}

// Start the server
const port = process.env.PORT || 3000; // Set the port for the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`); // Log the server's port when it starts
});
