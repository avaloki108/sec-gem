# Claude Code Integration Guide

This guide explains how to integrate Sec-Gemini with Claude Code using the Model Context Protocol (MCP).

## Prerequisites

- Claude Desktop or Claude Code installed
- Python 3.10 or later
- Sec-Gemini API key (set in `SEC_GEMINI_API_KEY` environment variable)

## Setup Instructions

### 1. Install Sec-Gemini Python SDK

```bash
pip install sec_gemini
```

Or install from source:

```bash
cd sec-gemini-python
uv sync --all-extras
```

### 2. Configure Claude Code

Claude Code uses MCP (Model Context Protocol) to connect to external tools and services. To add Sec-Gemini as an MCP server:

#### For Claude Desktop

1. Open Claude Desktop settings
2. Navigate to the "Developer" section
3. Click "Edit Config" to open your `claude_desktop_config.json`
4. Add the Sec-Gemini MCP server configuration:

```json
{
  "mcpServers": {
    "sec-gemini": {
      "command": "python",
      "args": ["-m", "sec_gemini.mcp_server"],
      "env": {
        "SEC_GEMINI_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

#### For Claude Code (VS Code Extension)

1. Open VS Code settings (Cmd/Ctrl + ,)
2. Search for "Claude Code MCP"
3. Add the configuration from `.claude/mcp_config.json` to your settings

Or manually edit your VS Code settings.json:

```json
{
  "claude.mcpServers": {
    "sec-gemini": {
      "command": "python",
      "args": ["-m", "sec_gemini.mcp_server"],
      "env": {
        "SEC_GEMINI_API_KEY": "${env:SEC_GEMINI_API_KEY}"
      }
    }
  }
}
```

### 3. Set Your API Key

Set your Sec-Gemini API key as an environment variable:

**Linux/macOS:**
```bash
export SEC_GEMINI_API_KEY="your-api-key-here"
```

**Windows (PowerShell):**
```powershell
$env:SEC_GEMINI_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set SEC_GEMINI_API_KEY=your-api-key-here
```

### 4. Restart Claude Code

After adding the configuration, restart Claude Desktop or reload VS Code for the changes to take effect.

## Using Sec-Gemini with Claude Code

Once configured, you can ask Claude Code to use Sec-Gemini for cybersecurity tasks:

- **Vulnerability Analysis**: "Use Sec-Gemini to analyze this code for security vulnerabilities"
- **Smart Contract Review**: "Ask Sec-Gemini to review this Solidity smart contract for common security issues"
- **Threat Modeling**: "Use Sec-Gemini to help create a threat model for this web application"
- **Security Best Practices**: "Query Sec-Gemini for best practices in securing this API endpoint"

## Web3 Security Use Cases

Sec-Gemini is particularly powerful for web3 security analysis through Claude Code:

### Smart Contract Auditing
```
Ask Sec-Gemini to audit this Solidity contract for:
- Reentrancy vulnerabilities
- Integer overflow/underflow
- Access control issues
- Front-running risks
```

### DeFi Protocol Analysis
```
Use Sec-Gemini to analyze this DeFi protocol for:
- Flash loan attack vectors
- Price oracle manipulation
- Liquidity pool vulnerabilities
```

### NFT Security
```
Query Sec-Gemini about:
- NFT minting vulnerabilities
- Metadata security
- Royalty enforcement issues
```

## Troubleshooting

### MCP Server Not Starting

If the Sec-Gemini MCP server doesn't start:

1. Verify Python is in your PATH
2. Check that `sec_gemini` package is installed: `python -m sec_gemini --version`
3. Ensure your API key is set correctly
4. Check Claude Desktop/Code logs for error messages

### Connection Issues

If Claude Code can't connect to Sec-Gemini:

1. Verify your API key is valid
2. Check your network connection
3. Try testing the SDK directly: `python -c "from sec_gemini import SecGemini; print('OK')"`

## Advanced Configuration

### Custom Endpoints

If you're running a local Sec-Gemini instance, you can configure custom endpoints:

```json
{
  "mcpServers": {
    "sec-gemini": {
      "command": "python",
      "args": ["-m", "sec_gemini.mcp_server"],
      "env": {
        "SEC_GEMINI_API_KEY": "your-api-key-here",
        "SEC_GEMINI_API_HTTP_URL": "http://localhost:8000",
        "SEC_GEMINI_API_WEBSOCKET_URL": "ws://localhost:8000"
      }
    }
  }
}
```

### Tool Permissions

You can configure which tools Sec-Gemini can access via the MCP server by adding tool-specific environment variables.

## Support

For issues or questions:
- GitHub Issues: https://github.com/google/sec-gemini/issues
- Documentation: https://secgemini.google

## See Also

- [Web3 Security Guide](WEB3_SECURITY_GUIDE.md)
- [Python SDK Documentation](sec-gemini-python/README.md)
- [TypeScript SDK Documentation](sec-gemini-ts/README.md)
