# OCI Enterprise AI - Policy minima para usar models, guardrails e tools com apikey

Documentação de referência do serviço:
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-started-agents.htm

## 1) Policy geral para usuarios 

```policy
allow group <your-group-name> to manage generative-ai-family in compartment <your-compartment-name>
```

Essa policy cobre o uso geral de Enterprise AI (incluindo modelos, guardrails e tools) no compartimento.

### Se quiser ser mais restritivo (não recomendado)

Ao invés de permitir que o usuário tenha acesso a todos os serviços da familia de AI generativa, você pode restringir por feature, utilizando o seguinte formato.

```policy
allow group <your-group-name> to manage generative-ai-apikey in compartment <your-compartment-name>
```

No caso do uso de modelos on-demand, e oci enterprise agents, habilite para todos os seguintes serviços:
- generative-ai-chat
- generative-ai-model
- generative-ai-apikey
- generative-ai-project
- generative-ai-vectorstore
- generative-ai-vectorstore-connector
- generative-ai-vectorstore-file
- generative-ai-file
- generative-ai-hosted-application
- generative-ai-hosted-deployment
- generative-ai-container

Referência:
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/iam-policies.htm

## 2) Policy minima para chamadas com API Key (obrigatório)

Para chamar modelos utilizando o padrão Openai Compatible, você precisa adicionar a seguinte permissão. Ela vai habilitar que os serviços da familia de AI generativa sejam chamados por meio de requisições do tipo `generativeaiapikey`.

```policy
allow any-user to use generative-ai-family
in compartment <your-compartment-name>
where ALL {request.principal.type='generativeaiapikey'}
```

## 3) Exceção: NL2SQL

Todos os serviços de chamada e tools de AI generativa estão contemplados nas policies anteriores, com exceção do NL2SQL, caso queira testar esse serviço, seria necessário adicionar policies para criar, alterar e manipular banco de dados, criar conexões, e criar e acessar secrets para autenticação.

Referências:
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/nl2sql.htm#top
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/semantic-store-permissions.htm


## 4) Exemplo de chamada OpenAI-compatible para modelos LLM OCI

```python
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  # API key criada no OCI Generative AI
    base_url="https://inference.generativeai.<available-region>.oci.oraclecloud.com/openai/v1"
)

response = client.responses.create(
    model="openai.gpt-oss-120b",  # troque pelo modelo disponivel na sua regiao
    input="Explique em uma frase o objetivo deste teste."
)

print(response)
```

Regiões disponíveis:
- https://docs.oracle.com/pt-br/iaas/Content/generative-ai/agentic-regions.htm#regions

Modelos suportados:
- https://docs.oracle.com/pt-br/iaas/Content/generative-ai/agentic-regions.htm#top

Referência:
- https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-compatible-api.htm
