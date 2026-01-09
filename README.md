# MCP Currency Converter

## Configuration

Add the following JSON config into your client's MCP configuration files:

```json
"currency-converter": {
  "command": "uvx",
  "args": [
    "--from",
    "git+https://github.com/sagthorat/mcp-currency-converter.git",
    "mcp-server"
  ],
  "env": {
    "API_KEY": "your_api_key_here"
  }
}
```
