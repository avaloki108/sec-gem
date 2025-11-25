#!/usr/bin/env python3
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example: Web3 Security Analysis with Sec-Gemini.

This example demonstrates how to use Sec-Gemini for analyzing smart contracts
and web3 security vulnerabilities.
"""

import asyncio
import os

from sec_gemini import SecGemini, Message, MessageType


# Example vulnerable smart contract
VULNERABLE_CONTRACT = """
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
    
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
"""


async def main():
  """Main function demonstrating web3 security analysis."""
  api_key = os.environ.get("SEC_GEMINI_API_KEY")
  if not api_key:
    print("Error: SEC_GEMINI_API_KEY environment variable not set")
    print("Please set your API key:")
    print("  export SEC_GEMINI_API_KEY='your-api-key-here'")
    return

  client = SecGemini(api_key=api_key)

  print("=" * 80)
  print("Sec-Gemini Web3 Security Analysis Example")
  print("=" * 80)

  prompt = f"""Conduct a comprehensive security audit of this smart contract.

Contract Code:
```solidity
{VULNERABLE_CONTRACT}
```

Please analyze for:
1. Critical Vulnerabilities (Reentrancy, overflow, etc.)
2. Access Control Issues
3. Best Practices compliance

For each issue, provide severity and recommended fix.
"""

  response = await client.generate(
    messages=[
      Message(
        message_type=MessageType.RESULT,
        content=prompt,
      )
    ]
  )

  print("\nSecurity Analysis Results:")
  print("-" * 80)
  for msg in response.messages:
    if msg.content:
      print(msg.content)


if __name__ == "__main__":
  asyncio.run(main())
