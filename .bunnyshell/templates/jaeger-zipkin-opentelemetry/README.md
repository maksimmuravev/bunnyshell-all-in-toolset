# 💥 Jaeger + Zipkin + OpenTelemetry

The Jaeger + Zipkin + OpenTelemetry stack is a comprehensive set of open-source tools for distributed tracing and observability. This stack offers powerful capabilities for tracing and troubleshooting complex systems.

**Jaeger**: distributed, scalable, end-to-end
**Zipkin**: lightweight, easy-to-use, interoperable
**OpenTelemetry**: standardized, extensible, cross-platform

## ⚙️  How it works?

```mermaid
graph LR

style A fill:#FFC107,stroke:#E65100,stroke-width:2px;
style B fill:#4CAF50,stroke:#1B5E20,stroke-width:2px;
style C fill:#2196F3,stroke:#0D47A1,stroke-width:2px;
style D fill:#9C27B0,stroke:#4A148C,stroke-width:2px;
style Opentelemetry fill:#1C27B0,stroke:#4A148C,stroke-width:2px;

subgraph App
    A(( ))
end

subgraph Jaeger
    B((Jaeger UI))
    C((Jaeger Collector))
end

subgraph Zipkin
    D((Zipkin UI))
end

subgraph TelemetryVisualizingTools
    Jaeger
    Zipkin
end

subgraph TelemetryCollector
    Opentelemetry
end

A -- Sends OTLP/HTTP traces --> Opentelemetry
Opentelemetry -- Exports PROTO traces  --> Zipkin
Opentelemetry -- Exports OTLP/HTTP traces --> C
C --> B
```

## ⚙️  Usage
See [Fetch Customers](../../../examples/fetch_customers) example.

## 📄 License
This project is licensed under the [MIT License](../../../LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
      \
       \   
           /\ /|
          |||| |
           \ | \
       _ _ /  @ @
     /    \   =>X<=
   /|      |   /
   \|     /__| |
     \_____\ \__\
```
