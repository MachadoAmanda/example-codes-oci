# IA Tradicional na Prática – Telco, Marketing e Fraude

Este repositório contém uma série de **práticas hands-on de Inteligência Artificial Tradicional**, pensadas para públicos de **Marketing, Negócio e Tecnologia**, com foco em **casos reais**, linguagem acessível e resultados acionáveis.

O objetivo é mostrar **IA de ponta a ponta**, desde dados em CSV até modelos treinados, avaliados e interpretados — sem dependência de banco de dados ou infraestrutura complexa.

---



## Prática 1 – Classificação: Predição de Churn

Notebook: `01_churn_classificacao.ipynb`

### Pergunta de negócio
> Quais clientes têm maior probabilidade de cancelar o serviço?

### Técnicas utilizadas
- Regressão Logística
- Análise exploratória
- Correlação
- Métricas de classificação
- Interpretação de coeficientes
- Geração de lista acionável para Marketing

### Resultado
- Modelo treinado
- Probabilidade de churn por cliente
- Segmentação de risco (baixo, médio, alto)

### Dataset (Fictício)

Arquivo: `telco_churn.csv`

Cada linha representa um cliente Telco, com informações típicas de negócio.

#### Colunas principais:
- `tempo_contrato_meses`
- `valor_mensal`
- `uso_dados_gb`
- `qtd_reclamacoes`
- `atraso_pagamento`
- `recebeu_campanha`
- `churn` (0 = não cancelou, 1 = cancelou)

Os dados são **fictícios**, mas modelados para refletir padrões realistas de mercado.

---

## Prática 2 – Regressão: Previsão de Valor Mensal (ARPU)

Notebook: `02_regressao_valor_mensal.ipynb`

### Pergunta de negócio
> Quanto cada cliente tende a gerar de receita mensal?

### Técnicas utilizadas
- Regressão Linear
- Visualização Real vs Previsto
- Análise de erro (MAE, RMSE, R²)
- Interpretação da equação da regressão
- Análise de impacto das variáveis

### Resultado
- Previsão de valor mensal por cliente
- Identificação de oportunidades de upsell
- Base para planejamento de receita

---

## Prática 3 – AutoML Oracle: Detecção de Anomalias (Fraude de Crédito)

Notebook: `03_automl_anomalia_fraude.ipynb`

### Pergunta de negócio
> Quais transações fogem do comportamento normal e podem indicar fraude?

### Contexto
Neste cenário, utilizamos **AutoML da Oracle** para resolver um problema clássico de **detecção de anomalias**, muito comum em:
- Fraude de cartão de crédito
- Transações financeiras suspeitas
- Comportamento fora do padrão

### Abordagem
- Dataset de transações financeiras (CSV)
- Modelo **não supervisionado**
- AutoML escolhe:
  - Algoritmo
  - Parâmetros
  - Estratégia de detecção

### O que o AutoML entrega
- Score de anomalia por transação
- Ranking de transações suspeitas
- Visualização de outliers
- Modelo pronto para produção

### Valor para o negócio
- Redução de fraude
- Priorização de investigação
- Menos regras manuais
- Escalabilidade

---

## Comparação

| Caso | Tipo de IA | Pergunta |
|----|----|----|
| Churn | Classificação | Vai sair ou não? |
| Valor Mensal | Regressão | Quanto vale o cliente? |
| Fraude | Anomalia / AutoML | Isso é comportamento normal? |

---


## ⚠️ Observações Importantes

- Todos os dados são fictícios
- Objetivo educacional e demonstrativo
- Não utilizar modelos ou dados diretamente em produção

---

> **IA tradicional resolve problemas reais de negócio.  
Não precisa ser complexa para ser poderosa.**
