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

"""MCP server for Sec-Gemini integration with Claude Code."""

import asyncio
import os
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .secgemini import SecGemini
from .models.message import Message
from .models.enums import MessageType


# Initialize MCP server
mcp_server = Server("sec-gemini")


@mcp_server.list_tools()
async def list_tools() -> list[Tool]:
  """List available Sec-Gemini tools for Claude Code."""
  return [
    Tool(
      name="analyze_security",
      description="""Analyze code, smart contracts, or security configurations for vulnerabilities.
      
      Specializes in:
      - Smart contract security (Solidity, Rust/Solana)
      - Web3 security (DeFi, NFT, cross-chain)
      - General cybersecurity analysis
      - Vulnerability detection and remediation
      """,
      inputSchema={
        "type": "object",
        "properties": {
          "code": {
            "type": "string",
            "description": "The code or configuration to analyze",
          },
          "language": {
            "type": "string",
            "description": "Programming language (solidity, rust, python, javascript, etc.)",
          },
          "focus_areas": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Specific security concerns to focus on (e.g., reentrancy, access_control, oracle_manipulation)",
          },
          "context": {
            "type": "string",
            "description": "Additional context about the code or system",
          },
        },
        "required": ["code"],
      },
    ),
    Tool(
      name="query_security",
      description="""Ask security-related questions or get guidance on cybersecurity topics.
      
      Useful for:
      - Security best practices
      - Threat modeling
      - Vulnerability explanations
      - Security architecture guidance
      - Web3 security patterns
      """,
      inputSchema={
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "The security question or topic to explore",
          },
          "domain": {
            "type": "string",
            "description": "Security domain (web3, defi, nft, infrastructure, application, etc.)",
          },
        },
        "required": ["query"],
      },
    ),
    Tool(
      name="audit_contract",
      description="""Perform comprehensive security audit of smart contracts.
      
      Covers:
      - Common vulnerabilities (reentrancy, overflow, access control)
      - Gas optimization
      - Best practice compliance
      - Standard compliance (ERC-20, ERC-721, etc.)
      """,
      inputSchema={
        "type": "object",
        "properties": {
          "contract_code": {
            "type": "string",
            "description": "Smart contract source code",
          },
          "contract_type": {
            "type": "string",
            "description": "Type of contract (token, nft, defi, dao, etc.)",
          },
          "blockchain": {
            "type": "string",
            "description": "Target blockchain (ethereum, solana, polygon, etc.)",
            "default": "ethereum",
          },
        },
        "required": ["contract_code"],
      },
    ),
  ]


@mcp_server.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
  """Execute Sec-Gemini tool calls from Claude Code."""
  api_key = os.environ.get("SEC_GEMINI_API_KEY")
  if not api_key:
    return [
      TextContent(
        type="text",
        text="Error: SEC_GEMINI_API_KEY environment variable not set",
      )
    ]

  client = SecGemini(api_key=api_key)

  try:
    if name == "analyze_security":
      code = arguments.get("code", "")
      language = arguments.get("language", "unknown")
      focus_areas = arguments.get("focus_areas", [])
      context = arguments.get("context", "")

      prompt = f"""Analyze the following {language} code for security vulnerabilities.

Code:
```{language}
{code}
```

Context: {context}

Focus on these areas: {', '.join(focus_areas) if focus_areas else 'all security aspects'}

Please provide:
1. Identified vulnerabilities with severity ratings
2. Detailed explanations of each issue
3. Recommended fixes with code examples
4. Best practice recommendations
"""

      response = await client.generate(
        messages=[
          Message(
            message_type=MessageType.RESULT,
            content=prompt,
          )
        ]
      )

      result = ""
      for msg in response.messages:
        if msg.content:
          result += msg.content + "\n"

      return [TextContent(type="text", text=result.strip())]

    elif name == "query_security":
      query = arguments.get("query", "")
      domain = arguments.get("domain", "general")

      prompt = f"""Security Domain: {domain}

Question: {query}

Please provide a comprehensive answer including:
1. Detailed explanation
2. Best practices
3. Common pitfalls to avoid
4. Examples or code snippets where applicable
"""

      response = await client.generate(
        messages=[
          Message(
            message_type=MessageType.RESULT,
            content=prompt,
          )
        ]
      )

      result = ""
      for msg in response.messages:
        if msg.content:
          result += msg.content + "\n"

      return [TextContent(type="text", text=result.strip())]

    elif name == "audit_contract":
      contract_code = arguments.get("contract_code", "")
      contract_type = arguments.get("contract_type", "unknown")
      blockchain = arguments.get("blockchain", "ethereum")

      prompt = f"""Conduct a comprehensive security audit of this {contract_type} smart contract for {blockchain}.

Contract Code:
```solidity
{contract_code}
```

Please provide:
1. **Critical Vulnerabilities**: Issues that could lead to loss of funds or contract compromise
2. **High Severity Issues**: Significant security concerns
3. **Medium Severity Issues**: Important but less critical problems
4. **Low Severity Issues**: Minor issues and recommendations
5. **Gas Optimization**: Opportunities to reduce gas costs
6. **Best Practices**: Compliance with security standards
7. **Code Quality**: General code quality observations

For each issue:
- Severity rating
- Line numbers (if applicable)
- Detailed explanation
- Proof of concept (if relevant)
- Recommended fix with code example
"""

      response = await client.generate(
        messages=[
          Message(
            message_type=MessageType.RESULT,
            content=prompt,
          )
        ]
      )

      result = ""
      for msg in response.messages:
        if msg.content:
          result += msg.content + "\n"

      return [TextContent(type="text", text=result.strip())]

    else:
      return [
        TextContent(
          type="text",
          text=f"Error: Unknown tool '{name}'",
        )
      ]

  except Exception as e:
    return [
      TextContent(
        type="text",
        text=f"Error executing tool: {str(e)}",
      )
    ]


async def main():
  """Run the MCP server."""
  async with stdio_server() as (read_stream, write_stream):
    await mcp_server.run(
      read_stream,
      write_stream,
      mcp_server.create_initialization_options(),
    )


if __name__ == "__main__":
  asyncio.run(main())
