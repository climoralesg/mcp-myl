from fastmcp import FastMCP

from .getTools import getCards

mcp = FastMCP("myl-get")

def handleTools(mcp):
    getCards(mcp)

