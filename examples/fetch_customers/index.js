const express = require('express');
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');
const { BasicTracerProvider, SimpleSpanProcessor } = require('@opentelemetry/sdk-trace-base');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { ExpressInstrumentation } = require('@opentelemetry/instrumentation-express');

const provider = new NodeTracerProvider({
  resource: {
    service_name: 'example-server'
  }
});

// Configure the OTLP HTTP exporter
const exporter = new OTLPTraceExporter({
  url: 'https://opentelemetry-j62w35.bunnyenv.com/v1/traces',
});

provider.addSpanProcessor(new SimpleSpanProcessor(exporter));
provider.register();

// Initialize the Express instrumentation
const expressInstrumentation = new ExpressInstrumentation();
expressInstrumentation.setTracerProvider(provider);

// Create an Express application
const app = express();

// Define a route that performs business logic
app.get('/api/customers', (req, res) => {
  const tracer = provider.getTracer('example-app');
  const span = tracer.startSpan('getCustomers');

  // Perform actual business logic here
  const customers = fetchCustomersFromDatabase();
  res.json(customers);

  span.end();
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
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

