"""Tests for the local-fetch-server MCP server."""
import pytest
from unittest.mock import patch
from fetch_server import fetch_and_extract


class TestFetchServer:
    """Test cases for the fetch server functionality."""

    @pytest.mark.asyncio
    async def test_fetch_page_success(self):
        """Test successful page fetching."""
        mock_content = "<html><body><h1>Test Page</h1></body></html>"
        with patch('fetch_server.trafilatura.fetch_url', return_value=mock_content) as mock_fetch:
            with patch('fetch_server.trafilatura.extract', return_value="Test Page") as mock_extract:
                result = await fetch_and_extract("https://example.com")

                assert "Test Page" in result
                mock_fetch.assert_called_once_with("https://example.com")
                mock_extract.assert_called_once_with(mock_content, favor_precision=True)

    @pytest.mark.asyncio
    async def test_fetch_page_no_content(self):
        """Test fetching a page with no extractable content."""
        with patch('fetch_server.trafilatura.fetch_url', return_value=None):
            result = await fetch_and_extract("https://example.com")

            assert "unable to extract content" in result.lower()

    @pytest.mark.asyncio
    async def test_fetch_page_extraction_failure(self):
        """Test fetching a page where extraction fails."""
        mock_content = "<html><body><h1>Test Page</h1></body></html>"
        with patch('fetch_server.trafilatura.fetch_url', return_value=mock_content):
            with patch('fetch_server.trafilatura.extract', return_value=None):
                result = await fetch_and_extract("https://example.com")

                assert "unable to extract content" in result.lower()

    @pytest.mark.asyncio
    async def test_fetch_page_network_error(self):
        """Test handling of network errors during fetching."""
        with patch('fetch_server.trafilatura.fetch_url', side_effect=Exception("Network error")):
            result = await fetch_and_extract("https://example.com")

            assert "unexpected error" in result.lower()
            assert "Network error" in result
