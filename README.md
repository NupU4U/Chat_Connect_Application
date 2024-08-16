# ChatConnect Application

## Overview
ChatConnect is a Python-based application designed for file sharing and client communication within a network, similar to the PSP file-sharing framework. The application utilizes a central server to manage communication between clients and supports both control messages and file transfer.

## Features
- Central server for client communication and file sharing.
- UDP for control messages and TCP for file transfer.
- Lock-free algorithm using 2 threads per client.
- User Interface built with Kivy.
- Local testing with 5 clients and 1 server.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NupU4U/ChatConnect-Application.git
