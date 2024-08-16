# ChatConnect Architecture

## Overview
The ChatConnect application is designed using a client-server model. The central server is responsible for managing communication between clients. The server handles incoming client connections, relays messages between clients, and manages file transfers.

### Components
1. **Server**: The server handles client connections and manages communication.
2. **Client**: The client connects to the server and sends/receives messages and files.
3. **UI**: The User Interface, built with Kivy, allows users to interact with the application.

### Communication Protocols
- **UDP**: Used for sending control messages.
- **TCP**: Used for file transfers.

### Thread Management
- Two threads are used per client to ensure a lock-free algorithm:
  - One for handling incoming messages.
  - One for sending outgoing messages.
