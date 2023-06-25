# 💥 Chisel
The **Prometheus + Pushgateway + Grafana** stack is a robust solution for monitoring, collecting, and visualizing metrics in real-time. This powerful combination of open-source tools enables you to gather, store, and analyze metrics from various sources.

- **Prometheus**: scalable, flexible, powerful
- **Pushgateway**: intermediary, batch-oriented, ephemeral
- **Grafana**: intuitive, customizable, interactive

## ⚙️  How it works?

```mermaid
graph LR

style A fill:#FFX107, stroke:#E65100, stroke-width:2px;
style P fill:#4CAF50, stroke:#1B5E20, stroke-width:2px;
style M fill:#2196F3, stroke:#0D47A1, stroke-width:2px;
style G fill:#9C27B0, stroke:#4A148C, stroke-width:2px;
style U fill:#607D8B, stroke:#263238, stroke-width:2px;

subgraph App
    A((App))
end

subgraph Metrics Exposer
    P((Pushgateway))
end

subgraph Metrics Storage
    M((Prometheus))
end

subgraph Visualization
    G((Grafana))
end

subgraph User
    U(( ))
end

A -->|Sends metrics to| P
M -->|Scrapes metrics from| P
G -->|Requests metrics from| M
U -->|Shows metrics from| G
U -->|Shows metrics directly from| M
```

## ⚙️  Usage
See [Process Memory Debugging](../../../examples/process_memory_debugging/) script example.

## 📄 License
This project is licensed under the [MIT License](../../../LICENSE).

---

🏆 Happy [BunnyShelling](https://bunnyshell.devpost.com/)! 🚀
