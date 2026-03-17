# Local Fetch MCP Server

A free, private web content fetcher for AI development environments that extracts clean text from web pages. This MCP server gives AI assistants the ability to access real-time web content while keeping all processing local for complete privacy.

Compatible with:
- **Claude Desktop** - Anthropic's official desktop app
- **Claude Code** - Anthropic's CLI tool for developers
- **Gemini CLI** - Gemini's CLI tool
- **Cline** - VS Code extension for AI-powered coding
- **Any MCP-compatible client**

## Features

- 🔗 **Direct URL Fetching**: Fetches content directly from provided URLs
- 📄 **Content Extraction**: Intelligently extracts clean text from web pages
- 🔒 **Privacy-First**: All processing happens locally on your machine
- ⚡ **Fast Integration**: Works seamlessly with Claude Desktop via MCP
- 🛠️ **Zero External Dependencies**: No external services or subscriptions required

## Quick Start

### Prerequisites

- Python 3.10 or higher
- One of the compatible AI environments:
  - Claude Desktop, Claude Code, Google CLI, Cline, or other MCP client
- Basic command line knowledge

### Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/dimitri-rebrikov/local-fetch-server.git
   cd local-fetch-server
   ```

2. **Set up the environment:**
   ```bash
   uv init
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv add "mcp[cli]" trafilatura
   ```

4. **Test the server:**
   ```bash
   python fetch_server.py
   ```

### Configuration

Choose your AI environment:

#### Claude Desktop
Add this to your config file:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "local-fetcher": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/local-fetch-server",
        "run",
        "python",
        "fetch_server.py"
      ]
    }
  }
}
```

#### Claude Code
Add this to your `CLAUDE.md` file or use the CLI:
```bash
claude --mcp-server local-fetcher="uv --directory /path/to/your/local-fetch-server run python fetch_server.py"
```

#### Google AI Studio / Gemini CLI
Configure via your MCP client settings or environment variables.

#### Cline (VS Code)
Add to your Cline MCP server configuration in VS Code settings.

Replace `/path/to/your/local-fetch-server` with the full path to this directory.

## Usage

After configuration, restart your AI environment. Connection indicators vary by platform:
- **Claude Desktop**: Look for the plug icon (🔌)
- **Claude Code**: Server status shown in CLI output
- **Other platforms**: Check your MCP client's connection status

Ask your AI assistant to fetch content from specific URLs like:
- "Fetch the content from https://example.com/article"
- "Extract text from this URL: https://news-site.com/story"
- "Get the main content from https://blog.example.com/post"

Your AI assistant will automatically use the local server to fetch and extract clean text from the provided URLs.

## How It Works

The server implements a single MCP tool that:

1. **Fetches** the web page from the provided URL
2. **Extracts** clean, readable text using Trafilatura
3. **Returns** the formatted content to Claude for analysis

All processing happens locally with no data sent to external services except for the direct web requests.

## Architecture

```
AI Client (Claude Desktop/Code/Gemini/Cline)
    ↓ (MCP Protocol)
Local Fetch Server
    ↓ (HTTP Request)
Target Website
    ↓ (Content Extraction)
Clean Text → AI Assistant
```

## Configuration Options

The server accepts these parameters for the fetch tool:

- `url` (string): The URL of the web page to fetch and extract content from

## Security Features

- **Input Validation**: Sanitizes URLs
- **Rate Limiting**: Polite delays between requests
- **Error Handling**: Graceful failure handling
- **Local Processing**: No external data dependencies

## Business Applications

This fetch server is ideal for:

- **Content Analysis**: Extracting and analyzing web content
- **Research**: Gathering information from specific sources
- **Data Collection**: Automated content extraction
- **Compliance Monitoring**: Checking web content for regulatory requirements

## Extending the Server

Consider these enhancements:

- Add multiple URL support
- Implement content caching
- Add domain filtering capabilities
- Include publication date extraction
- Add multiple extraction methods

## Troubleshooting

### Common Issues

**Server not connecting:**
- Verify the absolute path in your AI client config
- Restart your AI environment completely
- Check that Python dependencies are installed

**No content extracted:**
- Some websites block scraping
- Try different URLs
- Check the console output for specific errors

**Content extraction failing:**
- Verify the URL is accessible
- Some websites require JavaScript rendering
- Check the console output for specific errors

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Projects

- [Local Research MCP Server](https://github.com/Unlock-MCP/local-research-server) - Web search and content scraping
- [MCP Docs Server](https://github.com/Unlock-MCP/mcp-docs-server) - Local documentation access
- [Remote MCP Server](https://github.com/Unlock-MCP/remote-mcp-server) - Enterprise database access
- [UnlockMCP Website](https://unlockmcp.com) - MCP tutorials and resources

## Support

- [Tutorial Guide](https://unlockmcp.com/guides/getting-started-mcp)
- [MCP Documentation](https://unlockmcp.com/guides/getting-started-mcp)
- [Issue Tracker](https://github.com/dimitri-rebrikov/local-fetch-server/issues)