# Sandbox Info

![](/images/sandbox.png)

## Overview

The Sandbox API provides a comprehensive environment for executing code, managing files, and interacting with various development tools in an isolated container environment. This API is designed to support multiple programming languages, file operations, browser automation, and terminal interactions.

## Sandbox Context

### Get Sandbox Context
```http
GET /v1/sandbox
```

Retrieves sandbox environment information including system configuration and available resources.

**Response**: `SandboxResponse`
- `success`: Boolean indicating operation success
- `message`: Operation result message
- `data`: Sandbox environment data
- `home_dir`: Home directory path in the sandbox

Example `data`:

```json
System Environment (v1.0.0.93):
- Linux 6.10.14-linuxkit (x86_64), with internet access
- User: e3f8da5a6253, with sudo privileges
- Home directory: /home/gem
- Timezone: Asia/Shanghai
- Occupied Ports: 8080,8079,8088,8091,8100,8101,8102,8200,8888,9222

Development Environment:
- Python 3.12.11 (commands: python3, pip3)
- Node.js v22.19.0 (commands: node, npm)
- Git git version 2.34.1 (command: git)
- GitHub CLI (command: gh)
- UV uv 0.8.9 (command: uv)

Available Tools:
- Text editors: vim, nano
- File operations: wget, curl, tar, zip, unzip, tree
- Network tools: ping, telnet, netcat, nmap
- Text processing: grep, sed, awk, jq
- System monitoring: htop, procps
- Image processing: imagemagick
- Audio/Video Downloader: yt-dlp
```

## Package Management

### Python Packages
```http
GET /v1/sandbox/packages/python
```

Lists all installed Python packages in the sandbox environment.

**Response**: `Response`
- Returns a list of installed Python packages with their versions

### Node.js Packages
```http
GET /v1/sandbox/packages/nodejs
```

Lists all installed Node.js packages in the sandbox environment.

**Response**: `Response`
- Returns a list of installed npm packages with their versions

