
from typing import List

def getCards(mcp):
    
    @mcp.tool()
    def get_cards() -> str:

        """
        Obtiene algunas cartas disponibles en la BD
        Util para saber que cartas necesitamos
        """
        return "buenas"
