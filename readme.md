# MCP Server for mxHERO Multi-Account Email Search

## Description

This MCP (model context protocol) server is a Python project that provides access to mxHERO's multi-account email search service.

The Model Context Protocol (MCP) is a framework designed to standardize the way models interact with various data sources and services. In this project, MCP is used to facilitate seamless integration to emails captured by mxHERO Mail2Cloud. Mail2Cloud is designed to selectively capture emails from one or more accounts. The selection of emails can be finely controlled by powerful filters examining almost any aspect of messages and their attachments.

For more information about mxHERO's multi-email account service, including architecture, optimizations, etc. [read here](https://mxhero.com).

## Alternate versions

A Go version (plus prebuilt binaries) can be found [here](https://github.com/mxaiorg/mxmcp).


## Tools implemented

## `email_search`
Search stored emails

**Parameters**
- `query` (str): Email search query

**Returns** JSON of search results

## Requirements

- Python 3.13 or higher
- mxHERO Vector Search credentials (token)
  - A demo token can be obtained at https://lab4-api.mxhero.com/demo_signup
  - For production tokens, contact mxHERO.

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
                    "src/mcp_server_box.py"
                ]
            }
        }
    }
    ```


## MCP library

https://gofastmcp.com/servers/tools
