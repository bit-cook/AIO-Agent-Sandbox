"""Basic example demonstrating sandbox file operations."""

import base64
from agent_sandbox import Sandbox


def main():
    """Example of uploading a file to sandbox and processing it."""
    client = Sandbox(base_url="http://localhost:8080")

    # Example 1: Upload a local file to sandbox
    with open("./examples/foo.png", "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")
    
    # Write file to sandbox (all operations are within sandbox)
    sandbox_path = "/home/sandbox/test.png"
    write_result = client.file.write_file(
        file=sandbox_path,
        content=content,
        encoding="base64"
    )
    print(f"File written to sandbox: {sandbox_path}")
    print(f"Write result: {write_result}")
    
    # Example 2: List files in sandbox
    list_result = client.file.list_path(path="/home/sandbox")
    print(f"\nFiles in sandbox: {list_result}")
    
    # Example 3: Read file from sandbox
    read_result = client.file.read_file(file=sandbox_path)
    print(f"\nRead file from sandbox, size: {len(read_result.data.content)} bytes")
    
    # Example 4: Download file from sandbox to user's system
    # This is the only operation that touches the user's filesystem
    download_result = client.file.download_file(path=sandbox_path)
    print(f"\nDownloaded file from sandbox: {download_result}")


if __name__ == "__main__":
    main()
