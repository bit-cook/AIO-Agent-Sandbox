# Browser & VNC

AIO Sandbox provides a full browser environment with VNC (Virtual Network Computing) access, enabling visual interaction with web applications and GUI-based workflows.

![](/images/browser.png)

## VNC Access

### Connection
Access the VNC interface at:
```
http://localhost:8080/vnc/index.html?autoconnect=true
```

The VNC server provides:
- Full desktop environment
- Pre-installed Chrome browser
- Mouse and keyboard interaction
- Screen sharing capabilities

### Features
- **Auto-connect**: URL parameter for immediate connection
- **Responsive Interface**: Adapts to different screen sizes
- **Clipboard Sharing**: Copy/paste between local and remote
- **Full-Screen Mode**: Immersive browser experience

## Browser Automation

### Chrome DevTools Protocol (CDP)
AIO Sandbox exposes CDP for programmatic browser control:

```bash
# Get CDP endpoint
curl http://localhost:8080/cdp/json/version
# Or Get Browser Info (response data.cdp_url)
curl http://localhost:8080/v1/browser/info
```

Response includes `webSocketDebuggerUrl` for connecting automation tools.

### Browser Use Integration
Example with the `browser_use` Python library:

```python
import requests
from agent_sandbox import Sandbox
from browser_use.browser.browser import BrowserSession, BrowserProfile

# Get CDP URL
client = Sandbox(base_url="http://localhost:8080")
cdp_url = client.browser.get_browser_info().cdp_url

# Configure browser profile
profile = {
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "ignore_https_errors": True,
    "viewport": {"width": 1920, "height": 1080},
}

# Create session
browser_session = BrowserSession(
    browser_profile=BrowserProfile(**profile),
    cdp_url=cdp_url
)

await browser_session.start()
page = await browser_session.browser_context.new_page()
await page.goto("https://example.com")
```

### Playwright Integration

Works with Playwright for cross-browser testing:

```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.connect_over_cdp(cdp_url)
    page = await browser.new_page()
    await page.goto("https://example.com")
    await page.screenshot(path="screenshot.png")
```

## File System Integration

### Shared Downloads
Files downloaded in the browser are immediately available through:
- File API: `/v1/file/read`
- Shell access: `/v1/shell/ws`
- Code Server: `/code-server/`

### Example Workflow
1. Browse to a website in VNC
2. Download files through browser
3. Process files using shell commands
4. Edit code in VSCode Server
5. Run scripts that access downloaded files

```bash
# Files appear in standard download location
ls /home/gem/Downloads/
```

## Browser Configuration

### Default Settings
- Chrome browser pre-installed
- JavaScript enabled
- Pop-up blocking disabled for development
- Extensions allowed
- Developer tools accessible

### Custom Configuration
Modify browser settings through:
- Chrome flags in startup scripts
- Profile configuration via CDP
- Extension installation
- Proxy configuration

### Performance Optimization
- Hardware acceleration where available
- Memory limits for stability
- CPU throttling for resource management
- Network optimization

## Use Cases

### Web Scraping
Visual verification of scraping results:
```python
# Scrape data
data = await page.evaluate("document.body.innerText")

# Verify visually in VNC
await page.screenshot(path="/tmp/verification.png")
```

### Testing Web Applications
End-to-end testing with visual feedback:
- Form submission testing
- JavaScript behavior verification
- Responsive design testing
- Cross-browser compatibility

### AI Agent Workflows
Agents can interact with web interfaces:
- Form filling and submission
- Navigation and clicking
- Content extraction
- File uploads and downloads

### Remote Development
Web-based development tools:
- Online IDEs and editors
- Browser-based terminals
- Web application testing
- Client-side debugging

## Troubleshooting

### Common Issues

**VNC Connection Failed**
```bash
# Check VNC server status
ps aux | grep vnc

# Restart if needed
service vncserver restart
```

**Browser Not Responding**
```bash
# Kill and restart Chrome
pkill chrome
# Chrome will auto-restart on next CDP connection
```

**CDP Connection Issues**
```bash
# Verify CDP endpoint
curl http://localhost:8080/cdp/json/version

# Check for proper response format
```

### Performance Tips
- Use headless mode when visual feedback isn't needed
- Limit concurrent browser instances
- Clear browser cache regularly
- Monitor memory usage

Ready to automate browser workflows? Check out our [API documentation](/api/browser) for detailed endpoint information.
