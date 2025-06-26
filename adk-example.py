from oci.addons.adk import Agent, AgentClient, tool
from typing import Dict, Any, List

@tool
def get_weather(location: str) -> Dict[str, Any]:
    """Get the weather for a given location"""
    return {"location": location, "temperature": 72, "unit": "F"}

client = AgentClient(
        auth_type="api_key",
        profile="NEW",
        region="sa-saopaulo-1"
    )

agent = Agent(
    client=client,
    agent_endpoint_id="ocid1.genaiagent.oc1.sa-saopaulo-1.amaaaaaafioir7ia2hqi5mukcnmliuevdajcbipilddvsv5e7ay3sdpy7x7q",
    instructions="Your are an assistant of the user, adress the question that the user has with the tools that you have available",
    tools=[get_weather]
)


agent.setup()


response = agent.run("Is it cold in Seattle?")
response.pretty_print()
