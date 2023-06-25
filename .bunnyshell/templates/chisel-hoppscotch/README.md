# 💥 Chisel
The Chisel + Hoppscotch stack is a powerful combination for securely exposing local apps to the internet and conducting API testing. This stack leverages the unique capabilities of these two tools to provide a comprehensive solution for developers and testers.

- **Chisel**: Secure, fast, performant
- **Hoppscotch**: Developer-friendly, lightweight, PWA-like

## ⚙️  How it works?

### Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant Localhost
    participant Chisel_Client
    participant Chisel_Server

    Note over User: Chisel Reverse Tunneling Setup

    User->>Chisel_Client: Start Chisel Client

    Chisel_Client->>Chisel_Server: Handshake Request
    Chisel_Server-->>Chisel_Client: Handshake Response

    Note over User: Localhost to Chisel Server

    Chisel_Client->>Chisel_Server: Reverse Tunnel Request
    Chisel_Server-->>Chisel_Client: Reverse Tunnel Established

    Note over User: Exposing Localhost

    Chisel_Client->>Chisel_Server: Forwarding Connection
    Chisel_Server-->>Localhost: Connection Established

    Note over User: Accessing Local Service

    User->>Chisel_Server: HTTP Request to Public Endpoint
    Chisel_Server-->>Chisel_Client: Forwarded Request
    Chisel_Client-->>Localhost: Forwarded Request
    Localhost-->>Chisel_Client: Local Service Response
    Chisel_Client-->>Chisel_Server: Local Service Response
    Chisel_Server-->>User: Response Received
```

## ⚙️  Usage
See [Process Memory Debugging](../../../examples/process_memory_debugging/) script example.

## 📄 License
This project is licensed under the [MIT License](../../../LICENSE).

---

🏆 Happy [BunnyShelling](https://bunnyshell.devpost.com/)! 🚀
