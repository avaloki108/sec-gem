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

"""Entry point for running sec_gemini as a module."""

import sys


def main():
  """Main entry point."""
  if len(sys.argv) > 1 and sys.argv[1] == "mcp_server":
    # Run MCP server
    from .mcp_server import main as mcp_main
    import asyncio

    asyncio.run(mcp_main())
  else:
    print("Usage: python -m sec_gemini mcp_server")
    sys.exit(1)


if __name__ == "__main__":
  main()
