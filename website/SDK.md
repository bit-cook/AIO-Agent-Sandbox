# AIO Sandbox SDK

## Overview

The **AIO Sandbox SDK** is a Node.js library designed to integrate with the AIO Sandbox environment. It provides a comprehensive set of tools and interfaces for interacting with the sandbox, including shell execution, file management, Jupyter code execution, and more.

## Features

- **Shell Execution**: Run shell commands synchronously or asynchronously with polling.
- **File Management**: List, edit, download, and manage files within the sandbox.
- **Jupyter Integration**: Execute Jupyter notebook code with customizable parameters.
- **CDP Version Retrieval**: Fetch Chrome DevTools Protocol version information.

## Installation

To install the SDK, use the following command:

```bash
pnpm install @agent-infra/sandbox
```

## Usage

### Basic Configuration

Start by importing the SDK and configuring the client:

```typescript
import { AioClient } from "@agent-infra/sandbox";

const client = new AioClient({
  baseUrl: `https://{aio.sandbox.example}`, //The Url and Port should consistent with the Aio Sandbox
  timeout: 30000, // Optional: request timeout in milliseconds
  retries: 3, // Optional: number of retry attempts
  retryDelay: 1000, // Optional: delay between retries in milliseconds
});
```

### Shell Execution

Execute shell commands within the sandbox:

```typescript
const response = await client.shellExec({
  command: "ls -la",
});

if (response.success) {
  console.log("Command Output:", response.data.output);
} else {
  console.error("Error:", response.message);
}

// Asynchronous rotation training results, suitable for long-term tasks
const response = await client.shellExecWithPolling({
  command: "ls -la",
  maxWaitTime: 60 * 1000,
});
```

### File Management

List files in a directory:

```typescript
const fileList = await client.fileList({
  path: "/home/gem",
  recursive: true,
});

if (fileList.success) {
  console.log("Files:", fileList.data.files);
} else {
  console.error("Error:", fileList.message);
}
```

### Jupyter Code Execution

Run Jupyter notebook code:

```typescript
const jupyterResponse = await client.jupyterExecute({
  code: "print('Hello, Jupyter!')",
  kernel_name: "python3",
});

if (jupyterResponse.success) {
  console.log("Output:", jupyterResponse.data);
} else {
  console.error("Error:", jupyterResponse.message);
}
```

## Sandbox Startup Instructions

To start the sandbox locally, follow these steps:

1. Ensure you have Docker installed.
2. Pull the AIO Sandbox Image and start it.

```shell
docker pull aio.sandbox:latest
docker run -it -p 8821:8080 aio.sandbox:latest
```

3. The sandbox server will be available at `http://localhost:8821`.
4. then you should change client baseUrl:

```ts
const client = new AioClient({
  baseUrl: "http://localhost:8821",
});
```

## Development

### Build

Compile the TypeScript code:

```bash
pnpm build
```

### Test

Run tests using Vitest:

```bash
pnpm test
```

### Clean

Remove the `dist` directory:

```bash
pnpm clean
```

## Contributing

Contributions are welcome! Please submit issues and pull requests to improve the SDK.
