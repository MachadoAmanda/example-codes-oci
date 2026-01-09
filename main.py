import oci
from langchain_oci import ChatOCIGenAI

# -----------------------------------------------------------
# 1. Criar signer que renova Security Token automaticamente
# -----------------------------------------------------------

signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# OU, se estiver em Azure com federated workload identity:
# signer = oci.auth.signers.WorkloadIdentityFederationSigner(
#     session_token_path="<caminho_do_token_oidc_azure>",
#     private_key_path="<sua_chave_local>",
#     certificate_path="<seu_certificado>"
# )

# -----------------------------------------------------------
# 2. Configurar o endpoint e modelo
# -----------------------------------------------------------

endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"
model_id = "ocid1.generativeaimodel.oc1.us-chicago-1.amaaaaaask7dceyavwbgai5nlntsd5hngaileroifuoec5qxttmydhq7mykq"

# -----------------------------------------------------------
# 3. Criar o modelo usando auth_type=SECURITY_TOKEN
# -----------------------------------------------------------

model = ChatOCIGenAI(
    model_id=model_id,
    service_endpoint=endpoint,
    provider="meta",
    auth_type="SECURITY_TOKEN",
    signer=signer,  # <--- ESSENCIAL: passa o signer que renova token
    model_kwargs={
        "temperature": 0,
        "max_tokens": 600
    }
)

# -----------------------------------------------------------
# 4. Teste
# -----------------------------------------------------------

print(model.invoke("Hello, how are you?"))
