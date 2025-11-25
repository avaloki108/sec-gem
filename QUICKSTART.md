# Quick Start: Claude Code + Web3 Security

This quick start guide gets you up and running with Sec-Gemini in Claude Code for web3 security analysis in under 5 minutes.

## Prerequisites

- Python 3.10+
- Claude Desktop or Claude Code (VS Code extension)
- A Sec-Gemini API key

## Installation (3 steps)

### 1. Install Sec-Gemini Python SDK

```bash
pip install sec_gemini
```

### 2. Set Your API Key

**macOS/Linux:**
```bash
export SEC_GEMINI_API_KEY="your-api-key-here"
```

**Windows PowerShell:**
```powershell
$env:SEC_GEMINI_API_KEY="your-api-key-here"
```

### 3. Configure Claude Code

**For Claude Desktop:**

Open your `claude_desktop_config.json` and add:

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

**For VS Code Claude Code Extension:**

Add to your VS Code `settings.json`:

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

## Usage Examples

Once configured, you can ask Claude Code to use Sec-Gemini for security tasks:

### Smart Contract Audit

```
Use Sec-Gemini to audit this smart contract for security vulnerabilities:

pragma solidity ^0.8.0;

contract MyToken {
    mapping(address => uint256) public balances;
    
    function transfer(address to, uint256 amount) public {
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }
}
```

### DeFi Security Analysis

```
Ask Sec-Gemini to analyze this DeFi protocol for:
- Flash loan attack vectors
- Oracle manipulation risks
- Reentrancy vulnerabilities

[Paste your DeFi code]
```

### Security Best Practices

```
Query Sec-Gemini: What are the top 10 security best practices 
for developing a decentralized NFT marketplace on Ethereum?
```

## Common Use Cases

1. **Pre-Audit Review**: Quick security check before formal audit
2. **Code Review**: Security-focused code review during development
3. **Learning**: Understanding vulnerabilities and mitigations
4. **Threat Modeling**: Identifying attack vectors in web3 systems
5. **Best Practices**: Learning industry-standard security patterns

## Available Tools

When Sec-Gemini MCP server is running, Claude Code can use these tools:

- `analyze_security`: Analyze code for vulnerabilities
- `query_security`: Ask security questions
- `audit_contract`: Comprehensive smart contract audit

## Troubleshooting

**MCP server not connecting?**
- Verify Python is in PATH: `python --version`
- Check API key is set: `echo $SEC_GEMINI_API_KEY`
- Test the module: `python -m sec_gemini mcp_server --help`

**Need more help?**
- [Full Setup Guide](CLAUDE_CODE_SETUP.md)
- [Web3 Security Guide](WEB3_SECURITY_GUIDE.md)
- [GitHub Issues](https://github.com/google/sec-gemini/issues)

## Next Steps

- Read the [Web3 Security Guide](WEB3_SECURITY_GUIDE.md) for comprehensive examples
- Try the [Python example](sec-gemini-python/examples/web3_security_analysis.py)
- Try the [TypeScript example](sec-gemini-ts/examples/web3-security-analysis.ts)
- Check out the [full documentation](https://secgemini.google)

## Security Reminder

Sec-Gemini is a powerful assistant but should not be your only security measure:

- ✅ Use for initial analysis and learning
- ✅ Combine with manual audits
- ✅ Have multiple independent reviews
- ✅ Implement comprehensive testing
- ❌ Don't rely solely on AI for production security
- ❌ Don't skip professional audits for critical contracts
