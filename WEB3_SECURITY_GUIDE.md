# Web3 Security Guide for Sec-Gemini

This guide provides comprehensive information on using Sec-Gemini for web3 and blockchain security analysis.

## Table of Contents

1. [Introduction](#introduction)
2. [Smart Contract Security](#smart-contract-security)
3. [DeFi Security](#defi-security)
4. [NFT Security](#nft-security)
5. [Blockchain Infrastructure Security](#blockchain-infrastructure-security)
6. [Web3 Application Security](#web3-application-security)
7. [Examples and Use Cases](#examples-and-use-cases)

## Introduction

Sec-Gemini is designed to help security professionals, developers, and auditors identify and mitigate security vulnerabilities in web3 applications, smart contracts, and blockchain infrastructure.

### Key Capabilities

- **Smart Contract Analysis**: Identify vulnerabilities in Solidity, Rust (Solana), and other smart contract languages
- **DeFi Protocol Security**: Analyze decentralized finance protocols for economic and technical vulnerabilities
- **NFT Security**: Review NFT contracts and marketplaces for security issues
- **Blockchain Infrastructure**: Security assessment of nodes, validators, and network components
- **Web3 dApp Security**: Frontend and backend security for decentralized applications

## Smart Contract Security

### Common Vulnerabilities

Sec-Gemini can help identify and explain these common smart contract vulnerabilities:

#### Reentrancy
The classic vulnerability where external calls can recursively call back into the contract before state updates are complete.

**Example Query:**
```
Analyze this Solidity contract for reentrancy vulnerabilities:

contract Vulnerable {
    mapping(address => uint) public balances;
    
    function withdraw() public {
        uint amount = balances[msg.sender];
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success);
        balances[msg.sender] = 0;
    }
}
```

#### Access Control Issues
Improper or missing access controls that allow unauthorized access to critical functions.

**Example Query:**
```
Review this contract for access control vulnerabilities and suggest improvements:

contract MyToken {
    address public owner;
    
    function mint(address to, uint amount) public {
        // Missing onlyOwner modifier
        _mint(to, amount);
    }
}
```

#### Integer Overflow/Underflow
Arithmetic operations that can overflow or underflow (especially in Solidity < 0.8.0).

#### Front-Running
Vulnerabilities where transaction ordering can be exploited for profit.

#### Denial of Service
Patterns that can make contracts unusable or cause excessive gas consumption.

#### Unchecked External Calls
Failures to handle return values from external calls properly.

### Solidity Security Analysis

**Example Prompts:**

1. **Full Contract Audit:**
```
Please conduct a comprehensive security audit of this Solidity contract. Identify all potential vulnerabilities, gas optimization opportunities, and best practice violations.

[Paste your contract code here]
```

2. **Specific Vulnerability Check:**
```
Check this ERC-20 token implementation for:
- Reentrancy vulnerabilities
- Integer overflow/underflow
- Access control issues
- Approval race conditions

[Paste your ERC-20 code here]
```

3. **Upgrade Safety:**
```
I'm upgrading this contract using a proxy pattern. Analyze:
- Storage layout compatibility
- Function selector collisions
- Initialization security

[Paste old and new contract versions]
```

### Rust/Solana Smart Contract Security

Sec-Gemini also supports Solana smart contracts written in Rust:

**Example Query:**
```
Analyze this Solana program for security issues:
- Account validation
- Signer checks
- PDA (Program Derived Address) security
- Arithmetic overflow
- Integer casting issues

[Paste your Rust/Anchor code here]
```

## DeFi Security

### Protocol-Level Vulnerabilities

#### Flash Loan Attacks
Understanding and mitigating risks from flash loan exploits.

**Example Query:**
```
Analyze this lending protocol for flash loan attack vectors:
1. Price oracle manipulation
2. Reentrancy in flash loan callbacks
3. Collateral ratio manipulation

[Paste your DeFi protocol code]
```

#### Price Oracle Manipulation
Identifying weaknesses in price feed mechanisms.

**Example Query:**
```
Review this DEX's price oracle implementation for:
- TWAP (Time-Weighted Average Price) manipulation
- Sandwich attacks
- Low liquidity exploitation
- Multi-block MEV attacks

[Paste oracle code]
```

#### Liquidity Pool Vulnerabilities
Security issues in AMMs (Automated Market Makers) and liquidity pools.

**Example Query:**
```
Audit this AMM implementation for:
- Impermanent loss edge cases
- Pool draining attacks
- Fee calculation errors
- Slippage manipulation

[Paste AMM code]
```

### Economic Security

**Example Queries:**

1. **Tokenomics Analysis:**
```
Analyze the economic security of this token model:
- Inflation/deflation mechanisms
- Incentive alignment
- Game theory attack vectors
- Governance risks

[Paste tokenomics design]
```

2. **Yield Farming Security:**
```
Review this yield farming contract for:
- Reward calculation errors
- Stake/unstake exploits
- Emergency withdrawal issues
- Time-based vulnerabilities

[Paste staking contract]
```

## NFT Security

### NFT Contract Vulnerabilities

**Example Queries:**

1. **Minting Security:**
```
Analyze this NFT minting contract for:
- Reentrancy in minting functions
- Integer overflow in token IDs
- Access control on minting
- Whitelist bypass vulnerabilities
- Randomness manipulation (for generative NFTs)

[Paste NFT contract]
```

2. **Royalty Enforcement:**
```
Review this ERC-2981 royalty implementation for:
- Royalty bypass methods
- Calculation errors
- Edge cases in royalty distribution

[Paste royalty code]
```

3. **Metadata Security:**
```
Assess the security of this NFT metadata system:
- Centralization risks
- Metadata mutability
- IPFS pinning reliability
- Metadata injection vulnerabilities

[Paste metadata handling code]
```

### NFT Marketplace Security

**Example Query:**
```
Audit this NFT marketplace for:
- Reentrancy in buy/sell functions
- Price manipulation
- Escrow security
- Signature verification issues
- Order matching vulnerabilities

[Paste marketplace contract]
```

## Blockchain Infrastructure Security

### Node Security

**Example Queries:**

1. **Node Configuration Review:**
```
Review this blockchain node configuration for:
- Exposed RPC endpoints
- Weak authentication
- Rate limiting issues
- DDoS protection

[Paste configuration]
```

2. **Validator Security:**
```
Analyze this validator setup for:
- Key management security
- Slashing risks
- Network partition handling
- Failover mechanisms

[Paste validator config]
```

### Wallet Security

**Example Query:**
```
Review this web3 wallet implementation for:
- Private key storage
- Seed phrase generation
- Transaction signing security
- Phishing protection
- Hardware wallet integration

[Paste wallet code]
```

## Web3 Application Security

### Frontend Security

**Example Queries:**

1. **Web3 Integration Security:**
```
Analyze this web3 frontend for:
- Wallet connection security
- Transaction parameter validation
- Contract interaction safety
- XSS vulnerabilities in blockchain data display
- CSRF protection for wallet operations

[Paste frontend code]
```

2. **dApp Security:**
```
Review this dApp for:
- Smart contract interaction security
- Off-chain signature verification
- Event listening security
- Malicious contract detection

[Paste dApp code]
```

### Backend Security

**Example Query:**
```
Audit this web3 backend API for:
- Private key management
- Nonce management for transactions
- Gas price oracle security
- Rate limiting
- Blockchain data validation

[Paste backend code]
```

## Examples and Use Cases

### Example 1: Complete Smart Contract Audit

```
I need a comprehensive security audit of this ERC-721 NFT contract with minting functionality. 
Please analyze for:

1. Reentrancy vulnerabilities
2. Access control issues
3. Integer overflow/underflow
4. Gas optimization opportunities
5. Best practice violations
6. Compliance with ERC-721 standard

[Paste your complete contract]

Please provide:
- Severity ratings for each issue (Critical/High/Medium/Low)
- Specific line numbers where issues occur
- Detailed explanations of each vulnerability
- Recommended fixes with code examples
```

### Example 2: DeFi Protocol Security Review

```
Analyze this DeFi lending protocol for security vulnerabilities:

Context:
- Users can deposit collateral and borrow against it
- Liquidations occur when collateral ratio drops below threshold
- Uses Chainlink price oracles

Focus areas:
1. Flash loan attack vectors
2. Oracle manipulation risks
3. Liquidation mechanism security
4. Interest rate calculation accuracy
5. Reentrancy protection

[Paste protocol contracts]
```

### Example 3: Upgrade Safety Analysis

```
I'm upgrading this contract using UUPS proxy pattern. Analyze:

Old Contract Version:
[Paste old version]

New Contract Version:
[Paste new version]

Please check:
1. Storage layout compatibility
2. Function selector collisions
3. Initialization security
4. Access control on upgrade function
5. State migration safety
```

### Example 4: Web3 Frontend Security

```
Review this React component that interacts with a smart contract:

[Paste React component with web3 integration]

Security concerns:
1. User input validation before sending to contract
2. Transaction parameter verification
3. Proper error handling
4. Protection against malicious contract responses
5. Wallet signature verification
```

### Example 5: Cross-Chain Bridge Security

```
Audit this cross-chain bridge implementation for:

1. Message verification between chains
2. Replay attack protection
3. Race conditions in cross-chain transfers
4. Oracle security for chain state verification
5. Emergency pause mechanisms

Source Chain Contract:
[Paste source contract]

Destination Chain Contract:
[Paste destination contract]
```

## Best Practices for Web3 Security with Sec-Gemini

1. **Provide Context**: Always include relevant context about your protocol, tokenomics, and business logic
2. **Be Specific**: Ask targeted questions about specific vulnerability types or code sections
3. **Iterative Analysis**: Start with high-level review, then deep-dive into specific areas
4. **Include Tests**: Share your test suite for more comprehensive analysis
5. **Follow Up**: Ask for clarification or alternative solutions for identified issues
6. **Stay Updated**: Web3 security is evolving; ask about recent vulnerability patterns

## Additional Resources

- [Ethereum Security Best Practices](https://consensys.github.io/smart-contract-best-practices/)
- [SWC Registry](https://swcregistry.io/) - Smart Contract Weakness Classification
- [DeFi Security Summit](https://defisecuritysummit.org/)
- [Trail of Bits Blog](https://blog.trailofbits.com/)
- [OpenZeppelin Security](https://www.openzeppelin.com/security-audits)

## Getting Help

For specific web3 security questions:
1. Use Sec-Gemini through the CLI, SDKs, or Claude Code integration
2. Provide as much context as possible
3. Include relevant code snippets
4. Specify the blockchain platform (Ethereum, Solana, etc.)
5. Mention any specific standards (ERC-20, ERC-721, etc.)

## Contributing

If you have web3 security examples or use cases to share, please contribute to this guide via pull requests.

## Disclaimer

Sec-Gemini is a tool to assist in security analysis. It should not be the only method used for securing production smart contracts. Always:
- Conduct multiple independent audits
- Use formal verification where possible
- Have bug bounty programs
- Implement comprehensive testing
- Follow industry best practices
