# 💥 Grafana + Vector + Loki

The **Grafana + Vector + Loki** stack is a powerful combination of open-source tools for log management, processing, and visualization. It offers a streamlined solution for collecting, processing, storing, and analyzing logs from various sources.

- **Vector**: fast, efficient, reliable
- **Grafana**: intuitive, customizable, interactive
- **Loki**: scalable, cost-effective, flexible

## ⚙️  How it works?

```mermaid
graph LR

style App fill:#E6F4F1,stroke:#2980B9,color:black;
style Jaeger fill:#FDEDD0,stroke:#E89C0C,color:black;
style Zipkin fill:#FFF3CD,stroke:#E89C0C,color:black;
style TelemetryCollector fill:#FADBD8,stroke:#E74C3C,color:black;
style TelemetryVisualizingTools fill:#D6EAF8,stroke:#2980B9,color:black;

subgraph App
    A((App))
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
See [User Registration](../../../examples/user_registration) example.

## 📄 License
This project is licensed under the [MIT License](../../../LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
              \
               \   
                     /\    .-" /
                    /  ; .'  .' 
                   :   :/  .'   
                    \  ;-.'     
       .--""""--..__/     `.    
     .'           .'    `o  \   
    /                    `   ;  
   :                  \      :  
 .-;        -.         `.__.-'  
:  ;          \     ,   ;       
'._:           ;   :   (        
    \/  .__    ;    \   `-.     
     ;     "-,/_..--"`-..__)    
     '""--.._:`
```
