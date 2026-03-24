from fastmcp import FastMCP
from tools.indexTools import handleTools

mcp = FastMCP("myl-get")

handleTools(mcp)


if __name__ == "__main__":
    mcp.run()