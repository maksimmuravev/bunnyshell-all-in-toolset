# 💥 Grafana+Vector+Loki

The **Grafana+Vector+Loki** stack is a powerful combination of open-source tools for log management, processing, and visualization. It offers a streamlined solution for collecting, processing, storing, and analyzing logs from various sources.

- **Vector**: fast, efficient, reliable
- **Grafana**: intuitive, customizable, interactive
- **Loki**: scalable, cost-effective, flexible

## ⚙️ How it works?

```mermaid
graph LR

style A fill:#FFC107, stroke:#E65100, stroke-width:2px;
style B fill:#4CAF50, stroke:#1B5E20, stroke-width:2px;
style C fill:#2196F3, stroke:#0D47A1, stroke-width:2px;
style D fill:#9C27B0, stroke:#4A148C, stroke-width:2px;

subgraph App
    A(( ))
end

subgraph "Transformer"
    B((Vector))
end

subgraph Storage
    C(( Loki ))
end

subgraph Visualizer
    D(( Grafana ))
end

A -->|Sends logs to| B
B -->|Sends logs to| C
D -->|Reads logs from| C
D -->|Presents logs to| User
```

## ⚙️  Usage
See [User Registration App](../../../examples/user_registration_app) example.

## 📄 License
This project is licensed under the [MIT License](../../LICENSE).

---

```buttonless
🐇 Happy BunnyShelling! 🌰
```

