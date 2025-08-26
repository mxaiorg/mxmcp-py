# MCP Server for mxHERO Multi-Account Email Search

## Description

This MCP (model context protocol) server is a Python project that provides access to mxHERO's Mail2Cloud Advanced multi-account email search service.

The Model Context Protocol (MCP) is a framework designed to standardize the way models interact with various data sources and services. In this project, MCP is used to facilitate seamless integration to mxHERO Mail2Cloud Advanced. Mail2Cloud Advanced is a high performance data service for a company's email data. Mail2Cloud Advanced connects to company email services and optimizes the content for fast, scalable and secure access by AI solutions. 

### Architecture
Mail2Cloud is designed to selectively capture emails from one or more accounts. The selection of emails can be finely controlled by powerful filters examining any aspect of messages and their attachments. Captured emails are then optimized and stored into an isolated tenant in a vector database designed for email related searches. This MCP accesses the stored emails in the tenant through authenticated access credentials.

### Advantages
Solutions built with Mail2Cloud Advanced MCP outperforms other AI solutions with regards to email data search & knowledge recovery ([study](https://medium.com/datadriveninvestor/ai-email-retrieval-benchmark-how-purpose-built-ai-tools-outperform-generic-solutions-6fcd6d560c8f))
* Provides secure links to original emails (safe from accidental user deletion, etc.)
* Allows LLMs to search massive email repositories, far beyond their context window restraints.

### Demo Accounts

To facilitate exploration of this MCP, mxHERO provides demo accounts that are pre-loaded with thousands of emails. More about the demo emails can be found [here](https://mxhero.helpjuice.com/en_US/mxhero-ai/demo-account-for-ai-testing).

> See 'Access Tokens' below to get a token.

For more information see: [mxHERO Mail2Cloud Advanced](https://www.mxhero.com/advanced-ai) multi-email account service, including [architecture](https://mxhero.helpjuice.com/en_US/mxhero-ai/mxmcp#architecture-8), and optimizations.

## Alternate versions

A Go version (plus prebuilt binaries) can be found [here](https://github.com/mxaiorg/mxmcp).

### Streamable HTTP
This MCP repo is the 'stdio' variant. HTTP options exist at the following addresses:
* [https://lab4-api.mxhero.com/mcp/connect](https://lab4-api.mxhero.com/mcp/connect) (streamable HTTP)
* [https://lab4-api.mxhero.com/mcp/sse](https://lab4-api.mxhero.com/mcp/sse) (Legacy SSE)


## Tools implemented

## `email_search`
Search stored emails

**Parameters**
- `query` (str): Email search query

**Returns** JSON of search results

## Requirements

- Python 3.13 or higher
- mxHERO Vector Search **token**

### Access Tokens 
- A demo token can be obtained at https://lab4-api.mxhero.com/demo_signup
- For production tokens, uncheck "Demo" and Request an account (or contact mxHERO at contact@mxhero.com).

## Installation

1. Clone the repository

```sh
git clone https://github.com/mxaiorg/mxmcp-py
```

2. Install `uv` if not installed yet:

    2.1 MacOS+Linux

    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    2.2 Windows

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
    
3. Create and set up our project:

    3.1 MacOS+Linux

    ```sh
    # Create virtual environment and activate it
    uv venv
    source .venv/bin/activate

    # Lock the dependencies
    uv lock
    ```

    3.2 Windows

    ```sh
    # Create virtual environment and activate it
    uv venv
    .venv\Scripts\activate

    # Lock the dependencies
    uv lock
    ```

## Usage

### Running the MCP Server

To start the MCP server, run the following command:

```sh
uv --directory /fullpath/PycharmProjects/mxmcp-py run src/mxmcp.py --token "my_token"
```

Typically you don't need to start the server, your client will do it, but it is useful to make sure things are working.

### Using Claude as the client

1. Edit your `claude_desktop_config.json`:

    ```sh
    code ~/Library/Application\ Support/Claude/claude_desktop_config.json
    ```
   
   ...or use your favorite json editor.
    * You may need to create the file if it does not already exist.


2. Add the configuration:

* Replace the --directory argument value ('/Users/...') with the absolute (full) path to the python script.

    ```json
    {
        "mcpServers": {
            "mxhero-mcp-server": {
                "command": "uv",
                "args": [
                    "--directory",
                    "/Users/your_user/Desktop/mxmcp-py",
                    "run",
                    "src/mxmcp.py",
                    "--token",
                    "<copy_your_token_here>"
                ]
            }
        }
    }
    ```


## MCP library

https://gofastmcp.com/servers/tools
