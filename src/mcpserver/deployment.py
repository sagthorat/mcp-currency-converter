from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("Currency Converter")

@mcp.tool()
async def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert currency from one type to another."""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            return "Error: API_KEY environment variable not set"
            
        url = f"https://api.exchangerate.host/convert?from={from_currency.upper()}&to={to_currency.upper()}&amount={amount}&access_key={api_key}"
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10)
            data = response.json()

        if data.get("success"):
            result = data.get("result")
            return f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}"
        else:
            return "Currency conversion failed"
            
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
   
