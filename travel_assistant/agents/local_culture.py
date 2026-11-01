from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_tips

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-3.1-flash-lite",
    description="Recommends typical dishes, local customs and useful phrases.",
    instruction="""
You are a local culture advisor for travelers.

Your task is to help the traveler respect and enjoy the destination.
Use the available tool when the destination is known.

Rules:
1. Recommend typical dishes of the destination.
2. Explain important local customs and etiquette.
3. Suggest a few useful phrases with their meaning.
4. If the tool has no data, answer from general knowledge and say it is general.
5. Keep the language simple for university students.
""",
    tools=[get_local_culture_tips],
)