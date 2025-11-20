# Sec-Gemini SDKs and CLI

This repository hosts SDKs and a CLI for Sec-Gemini, an experimental cybersecurity-focused AI from
Google.

**🆕 Now compatible with Claude Code!** See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide or [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md) for detailed integration instructions.

**🔒 Web3 Security Supported!** Check out [WEB3_SECURITY_GUIDE.md](WEB3_SECURITY_GUIDE.md) for comprehensive web3 and blockchain security analysis.

## SDKs

SDKs are available for:

* Python in `sec-gemini-python/`
* TypeScript in `sec-gemini-ts/`

We also have a web component to ease integration on your website. Here's how to load it:

```html
<sec-gem-chat
      incognito="true"
      session-id=""
      session-name="TestName"
      session-description="TestDescription"
      session-prompt=""
      theme="dark"
      api-key="..."
    >
    </sec-gem-chat>
<script src='https://cdn.jsdelivr.net/npm/sec-gemini-web-component/dist/swc.iife.js'>
```

## CLI

The CLI can be installed on Linux and macOS:

```shell
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/google/sec-gemini/releases/download/cli/sec-gemini-v0.0.4/sec-gemini-installer.sh | sh
```

And for Windows:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://github.com/google/sec-gemini/releases/download/cli/sec-gemini-v0.0.4/sec-gemini-installer.ps1 | iex"
```

[![asciicast](cli/demo.gif)](https://asciinema.org/a/0pwF96A6XCqutg3RidlSP6dyD)

## Claude Code Integration

Sec-Gemini integrates seamlessly with Claude Code via the Model Context Protocol (MCP):

- **Easy Setup**: Configure Sec-Gemini as an MCP server in minutes
- **Web3 Security**: Specialized support for smart contract auditing, DeFi protocol analysis, and NFT security
- **Interactive Analysis**: Use Claude Code to interactively analyze security vulnerabilities

See [CLAUDE_CODE_SETUP.md](CLAUDE_CODE_SETUP.md) for detailed setup instructions.

## Web3 Security

Sec-Gemini provides comprehensive security analysis for web3 applications:

- **Smart Contract Auditing**: Solidity, Rust/Solana, and other smart contract languages
- **DeFi Security**: Flash loan vulnerabilities, oracle manipulation, liquidity pool security
- **NFT Security**: Minting vulnerabilities, royalty enforcement, metadata security
- **Cross-Chain Security**: Bridge security, cross-chain message verification

See [WEB3_SECURITY_GUIDE.md](WEB3_SECURITY_GUIDE.md) for examples and best practices.

## Website

For more information on Sec-Gemini, visit [https://secgemini.google](https://secgemini.google).

## Disclaimer

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards
Program](https://bughunters.google.com/open-source-security).
