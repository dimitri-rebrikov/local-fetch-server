# fetch_server.py
from mcp.server.fastmcp import FastMCP
import trafilatura

# Initialize the MCP server with a descriptive name
mcp = FastMCP("LocalFetch")

@mcp.tool(
    title="Web Content Fetcher and Extractor",
    description="Fetches content from a provided URL and extracts clean text."
)
async def fetch_and_extract(url: str) -> str:
    """
    Fetches and extracts content from a web page.

    Args:
        url: The URL of the web page to fetch and extract content from.
    """
    print(f"INFO: Starting fetch for: '{url}'")

    try:
        # Use Trafilatura to fetch and extract the main article text
        downloaded_page = trafilatura.fetch_url(url)
        if downloaded_page:
            main_text = trafilatura.extract(downloaded_page, favor_precision=True)
            if main_text:
                print("INFO: Content extraction successful.")
                return main_text
            else:
                return "I was unable to extract content from the provided URL."
        else:
            return "I was unable to extract content from the provided URL."

    except Exception as e:
        return f"An unexpected error occurred during fetching: {e}"

# Allow the server to be run directly from the command line
if __name__ == "__main__":
    mcp.run()