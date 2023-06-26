from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from flask import Flask

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="https://opentelemetry-tlqebr.bunnyenv.com/v1/traces"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    with tracer.start_as_current_span('index'):
        return 'Hello, world!'

@app.route('/hello')
def hello():
    with tracer.start_as_current_span('hello'):
        return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
