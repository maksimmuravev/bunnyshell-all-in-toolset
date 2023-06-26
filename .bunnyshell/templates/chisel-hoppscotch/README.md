# 💥 Chisel + Hoppscotch
The Chisel + Hoppscotch stack is a powerful combination for securely exposing local apps to the internet and conducting API testing. This stack leverages the unique capabilities of these two tools to provide a comprehensive solution for developers and testers.

- **Chisel**: Secure, fast, performant
- **Hoppscotch**: Developer-friendly, lightweight, PWA-like

## ⚙️  How it works?

To better explain, let's start by illustrating how tunneling works using a sequence diagram. For this purpose, I will be using [Chisel](https://github.com/jpillora/chisel) tool.

```mermaid
sequenceDiagram
    participant User
    participant Localhost
    participant Chisel Client
    participant Chisel Server

    Note over User: User is about to expose hir/her localhost app...

    User->>Chisel Client: Start Chisel Client

    Chisel Client->>Chisel Server: Handshake Request
    Chisel Server-->>Chisel Client: Handshake Response

    Chisel Client->>Chisel Server: Reverse Tunnel Request
    Chisel Server-->>Chisel Client: Reverse Tunnel Established

    Note over User: Now localhost is exposing well

    Chisel Client->>Chisel Server: Forwarding Connection
    Chisel Server-->>Localhost: Connection Established

    Note over User: User is about to access localhost "remotely"

    User->>Chisel Server: HTTP Request to Public Endpoint
    Chisel Server-->>Chisel Client: Forwarded Request
    Chisel Client-->>Localhost: Forwarded Request
    Localhost-->>Chisel Client: Local Service Response
    Chisel Client-->>Chisel Server: Local Service Response
    Chisel Server-->>User: Response Received
```

Speaking specifically about the BunnyShell template example, which is more relevant to our discussion:
```mermaid
graph LR
    subgraph Developer Machine
        style Localhost fill:#bbf300,stroke:#FF00880000,color:#000,stroke-width:2px
        User((User)) -->|1. Exposes app to| Localhost(Localhost)
        User((User)) -->|2. Run Chisel client binary| Chisel_Client((Chisel Client))
        Localhost --> |7. Responses to| Chisel_Client
        Chisel_Client --> |8. Responses to| User((User))
        
    end

    subgraph Internet
        style Chisel_Server fill:#FF0088,stroke:#000000,stroke-width:2px
        Chisel_Client -->|3. Connects to server| Chisel_Server((Chisel Server))
        Chisel_Server -->|5. Forwards requests| Chisel_Client
        User -->|4. Accesses app remotely via reversed tunnel| Chisel_Server
        Chisel_Client --> |6. Forwards request to| Localhost
    end

```

## ⚙️  Usage
See [Nginx Demo](../../../examples/nginx_demo/) example.

## 📄 License
This project is licensed under the [MIT License](../../../LICENSE).

---

```python
< 🏆 Happy BunnyShelling 🚀 >
-----------------------------
              \
               \   
               ((`\
            ___ \\ '--._
         .'`   `'    o  )
        /    \   '. __.'
       _|    /_  \ \_\_
      {_\______\-'\__\_\
```

