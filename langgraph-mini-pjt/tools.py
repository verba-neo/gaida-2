from langchain_core.tools import tool
import aiohttp

@tool
def get_weather(city: str) -> str:
    """get weather info tool"""
    return '좋은 날씨'