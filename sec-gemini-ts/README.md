# Sec-Gemini TypeScript SDK

## Installation

```bash
npm install sec-gemini
```

## Basic usage

### Streaming API

### Synchronous API


## Running the demo

The `demo/demo.js` code demonstrates how to use the SDK. You can run it as follows:

**Linux/Mac**
```bash
SEC_GEMINI_API_KEY="YOUR_ACTUAL_API_KEY" npm run demo
```

**Windows CMD**
```bash
set SEC_GEMINI_API_KEY=your_key_here && npm run demo
```
**Windows PowerShell**
```bash
$env:SEC_GEMINI_API_KEY="your_key_here" && npm run demo
```

## Web3 Security Analysis

For web3 and smart contract security analysis, see:
- `./examples/web3-security-analysis.ts` - Example of analyzing smart contracts for vulnerabilities

Run with:
```bash
SEC_GEMINI_API_KEY="your-key" npx ts-node examples/web3-security-analysis.ts
```

## Claude Code Integration

This SDK can be used with Claude Code via the Python MCP server. See [CLAUDE_CODE_SETUP.md](../CLAUDE_CODE_SETUP.md) for setup instructions.

## Developement

### Install dependencies

```bash
npm install
```

### Using the local package

Build and then use npm link to use the package from source

```bash
npm run build
npm link
```

in your project/app

```bash
npm link sec-gemini
```

### Build for release

```bash
npm run build
```

### Runing tests

```bash
npm run test
```
