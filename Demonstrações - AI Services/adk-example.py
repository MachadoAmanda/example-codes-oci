## Requirements : 
## pip install 'oci[adk]'
## endpoint de um agente já criado no serviço de Agent OCI (agent_endpoint_id)

from oci.addons.adk import Agent, AgentClient, tool
from typing import Dict, Any, List

# Adicionando uma nova tool
@tool
def get_weather(location: str) -> Dict[str, Any]:
    """Get the weather for a given location"""
    return {"location": location, "temperature": 72, "unit": "F"}

# Criando um client do agente
client = AgentClient(
        auth_type="api_key",
        profile="CHICAGO",
        region="us-chicago-1"
    )

# Inicializando o agente
agent = Agent(
    client=client,
    agent_endpoint_id="ocid1.genaiagentendpoint.oc1.us-chicago-1.amaaaaaad6nji3aa6rsojzjyjgqasnfntv4gcken7tcs6pfuaa5ni75554ja",
    instructions="Your are an assistant of the user, adress the question that the user has with the tools that you have available",
    tools=[get_weather]
)

# Sincronizando a tool ao agente
agent.setup()

# Chamando o agente
response = agent.run("Is it cold in Seattle?")
response.pretty_print()
