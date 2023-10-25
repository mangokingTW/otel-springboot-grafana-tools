import requests
import time
import logging
from opentelemetry import trace
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

logging.basicConfig(level=logging.DEBUG)
LoggingInstrumentor().instrument(set_logging_format=True)

# Resource can be required for some backends, e.g. Jaeger
# If resource wouldn't be set - traces wouldn't appears in Tempo
resource = Resource(attributes={
    "service.name": "python-app"
})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

# Configure a Tempo exporter (replace with your Tempo backend details)
tempo_exporter = OTLPSpanExporter(
    endpoint="http://tempo-distributor.observability.svc.cluster.local:4317",
    insecure=True,
)

span_processor = BatchSpanProcessor(tempo_exporter)

# Create a SpanProcessor and add the Tempo exporter
trace.get_tracer_provider().add_span_processor(span_processor)

# Wrap your HTTP request code with OpenTelemetry instrumentation
RequestsInstrumentor().instrument(tracer=tracer)

while True:
    # Make an HTTP request
    logging.info("Make an HTTP request")
    with tracer.start_as_current_span("http_request"):
        response = requests.get(
                "http://springboot-app:8080/fail",
                timeout=5,
                )
        logging.info("Response: "+ response.text)
    time.sleep(1)

# Don't forget to uninstrument after making the request
RequestsInstrumentor().uninstrument()
