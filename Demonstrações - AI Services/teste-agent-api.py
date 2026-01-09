import oci
import requests
import json

# Caminho e perfil do seu config_file OCI
config = oci.config.from_file("~/.oci/config", "SAOPAULO")

# Cria o signer (gera assinatura automática)
signer = oci.signer.Signer(
    tenancy=config["tenancy"],
    user=config["user"],
    fingerprint=config["fingerprint"],
    private_key_file_location=config["key_file"]
)
agentEndpointId = "ocid1.genaiagentendpoint.oc1.sa-saopaulo-1.amaaaaaad6nji3aatd554eg2bm32u3u47ep4jwso3l5cc6n2w3por3j47yna"
# Endpoint base do serviço (exemplo)
endpoint = f"https://agent-runtime.generativeai.sa-saopaulo-1.oci.oraclecloud.com/20240531/agentEndpoints/{agentEndpointId}/sessions"

# Exemplo de payload para criar uma sessão de agente
payload = {
    "compartmentId": "ocid1.compartment.oc1..aaaaaaaaev2ipyek53f7sck5ibvtnqrp5w2k54qiuk2cikbfati5bk54yhka",
    "displayName": "MeuAgenteGPT",
    "agentType": "GENERIC"
}

# Envia a requisição assinada
response = requests.post(
    endpoint,
    json=payload,
    auth=signer  
)

# Session criada
res = response.json()
print(res['id'])


########### chat com agente
endpoint = f"https://agent-runtime.generativeai.sa-saopaulo-1.oci.oraclecloud.com/20240531/agentEndpoints/{agentEndpointId}/actions/chat"

# Exemplo de payload para criar uma sessão de agente
payload = {
    "compartmentId": "ocid1.compartment.oc1..aaaaaaaaev2ipyek53f7sck5ibvtnqrp5w2k54qiuk2cikbfati5bk54yhka",
    "performedActions": [],
    "sessionId": res['id'],
    "shouldStream": False,
    "toolParameters": {    },
    "userMessage": "Qual produto mais tenho no estoque?"
}

# Envia a requisição assinada
response = requests.post(
    endpoint,
    json=payload,
    auth=signer  
)

res = response.json()
print(res['message']['content']['text'])
