from bilibili_api import search,sync
from bilibili_api.search import SearchObjectType, OrderUser
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Bilibili Mcp Server")

@mcp.tool()
def search_user(keyword: str, page: int = 1) -> dict:
    """
    Search Bilibili API with the given keyword.
    
    Args:
        keyword: Search term to look for on Bilibili
        
    Returns:
        Dictionary containing the search results from Bilibili
    """
    return sync(search.search(keyword))

if __name__ == "__main__":
    mcp.run(transport="stdio")
