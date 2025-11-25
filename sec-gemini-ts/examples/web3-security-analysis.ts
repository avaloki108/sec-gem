/**
 * Copyright 2025 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Example: Web3 Security Analysis with Sec-Gemini
 * 
 * This example demonstrates how to use Sec-Gemini TypeScript SDK
 * for analyzing smart contracts and web3 security vulnerabilities.
 */

import { SecGemini, MessageType } from 'sec-gemini';

// Example vulnerable smart contract
const VULNERABLE_CONTRACT = `
pragma solidity ^0.8.0;

contract VulnerableBank {
    mapping(address => uint256) public balances;
    
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Vulnerability: Reentrancy attack
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
        
        balances[msg.sender] -= amount;
    }
}
`;

async function analyzeContract() {
  const apiKey = process.env.SEC_GEMINI_API_KEY;
  
  if (!apiKey) {
    console.error('Error: SEC_GEMINI_API_KEY environment variable not set');
    console.error('Please set your API key:');
    console.error('  export SEC_GEMINI_API_KEY="your-api-key-here"');
    process.exit(1);
  }

  const client = new SecGemini({ apiKey });

  console.log('=' .repeat(80));
  console.log('Sec-Gemini Web3 Security Analysis Example');
  console.log('='.repeat(80));

  const prompt = `Conduct a comprehensive security audit of this smart contract.

Contract Code:
\`\`\`solidity
${VULNERABLE_CONTRACT}
\`\`\`

Please analyze for:
1. Critical Vulnerabilities (Reentrancy, overflow, etc.)
2. Access Control Issues
3. Best Practices compliance

For each issue, provide severity and recommended fix.
`;

  try {
    const response = await client.generate({
      messages: [
        {
          message_type: MessageType.RESULT,
          content: prompt,
        },
      ],
    });

    console.log('\nSecurity Analysis Results:');
    console.log('-'.repeat(80));
    
    for (const msg of response.messages) {
      if (msg.content) {
        console.log(msg.content);
      }
    }
  } catch (error) {
    console.error('Error during analysis:', error);
  }
}

// Run the analysis
analyzeContract().catch(console.error);
