# CampaignSense

**CRM Analytics para Otimização de Campanhas de Marketing**

![Author](https://img.shields.io/badge/author-Jhonathan%20Domingues-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Concluída-green)

![Python](https://img.shields.io/badge/python-3.12.5-blue?logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ml-scikit--learn-orange?logo=scikitlearn&logoColor=white)
![Model](https://img.shields.io/badge/model-LightGBM-black)
![Model](https://img.shields.io/badge/model-XGBoost-black)
![Data](https://img.shields.io/badge/data-Pandas%20%7C%20NumPy-blue)
![Stats](https://img.shields.io/badge/stats-SciPy-informational)
![Viz](https://img.shields.io/badge/viz-Matplotlib%20%7C%20Seaborn-purple)
![Persistence](https://img.shields.io/badge/persistence-Joblib-gray)

![CampaignSense](imagens/thumbnail.png)

---

## Visão Geral

A **CampaignSense** é uma Proof of Concept (POC) de **CRM Analytics** voltada à **otimização de campanhas de marketing**, com foco explícito em **decisão de negócio** e **impacto financeiro**.

A proposta da POC é demonstrar como dados de clientes e histórico de campanhas podem ser utilizados para **priorizar contatos**, reduzindo desperdício de orçamento e maximizando o **lucro esperado** de uma campanha.

O projeto trata modelos de Machine Learning como **componentes de suporte à decisão**, e não como um fim em si mesmos. O valor central da solução está na conexão clara entre:

- dados de clientes;
- estimativa de propensão à resposta;
- regras de decisão;
- impacto financeiro esperado.

---

## Problema de Negócio

Em campanhas de marketing tradicionais, é comum que empresas impactem grandes parcelas da base de clientes sem distinção clara de potencial de retorno, o que leva a:

- desperdício de orçamento com clientes de baixa propensão;
- baixo retorno incremental das campanhas;
- dificuldade de justificar decisões de targeting com base em critérios objetivos.

A **CampaignSense** endereça esse problema ao propor uma abordagem orientada a **profit targeting**, na qual apenas clientes com **retorno esperado positivo** são priorizados para contato.

---

## Escopo da POC

A CampaignSense contempla:

- análise exploratória orientada à decisão de negócio;
- segmentação de clientes para identificação de perfis comportamentais;
- modelagem preditiva de propensão à resposta;
- definição explícita de regras de decisão baseadas em ganho e custo;
- geração de artefatos analíticos e executivos que suportam decisões de campanha.

---

## Fonte dos Dados

A POC utiliza um **dataset público**, originalmente disponibilizado como parte de um **case técnico de CRM Analytics**, proposto no contexto de um processo seletivo conduzido por uma grande empresa do setor de delivery no Brasil.

O dataset circulou por meio de repositórios públicos de código, hoje indisponíveis, e é amplamente utilizado como referência prática em estudos e demonstrações de **CRM Analytics**.

Nesta POC, os dados são utilizados exclusivamente como base analítica para demonstrar a construção de uma solução orientada à decisão e ao impacto financeiro, sem qualquer vínculo institucional ou comercial com a empresa que originou o case.

---

## Estrutura do Projeto

```
campaignsense/
│
├── data/
│   ├── raw/                    # dados brutos de campanhas e clientes
│   └── processed/              # dados tratados e splits (train/valid/test/segment)
│
├── imagens/
│   └── thumbnail.png           # imagem de capa da POC
│
├── src/
│   ├── evaluation.py           # funções auxiliares para avaliação e agregação de resultados
│   └── paths.py                # centralização de caminhos e diretórios do projeto
│
├── notebooks/
│   ├── 01-data_audit_eda.ipynb # ingestão, auditoria e EDA inicial da base
│   ├── 02-eda_decision.ipynb   # EDA orientada à decisão de negócio
│   ├── 03-segmentation.ipynb   # segmentação comportamental de clientes
│   ├── 04-modeling.ipynb       # modelagem preditiva de propensão à resposta
│   └── 05-profit_targeting.ipynb # definição de política de decisão e profit targeting
│
├── references/
│   └── 01_dicionario_de_dados.md # dicionário e descrição das variáveis do dataset
│
├── reports/
│   ├── plots/                  # visualizações analíticas e executivas
│   ├── metrics/                # métricas e políticas de decisão (JSON)
│   ├── tables/                 # listas priorizadas e quebras analíticas
│   └── campaignsense_summary.md # relatório executivo final da POC
│
├── requirements.txt            # dependências do projeto
└── README.md                   # documentação principal da POC
```

---

## Pipeline da Solução

A CampaignSense segue um pipeline analítico orientado à decisão:

1. Preparação e auditoria dos dados de clientes e campanhas  
2. Análise exploratória com foco em alavancas de negócio  
3. Segmentação comportamental de clientes  
4. Estimativa de propensão à resposta por meio de modelos preditivos  
5. Conversão do score em **regra objetiva de priorização**  
6. Estimativa de impacto financeiro esperado da campanha  

O ciclo se encerra com a geração de artefatos acionáveis, incluindo listas priorizadas de clientes e um **Campaign Summary** executivo.

---

## Conclusão

A CampaignSense demonstra como análises de CRM podem ser estruturadas para apoiar decisões de campanha orientadas a valor, indo além da previsão isolada de resposta.

Ao longo da POC, dados de clientes, segmentação comportamental e modelos preditivos foram integrados a uma lógica explícita de decisão, permitindo a definição de regras objetivas de priorização e a estimativa de impacto financeiro esperado.

Mais do que maximizar métricas de modelo, a proposta da CampaignSense é evidenciar que o papel do Machine Learning em contextos de marketing está na **tradução de sinais analíticos em decisões justificáveis, rastreáveis e acionáveis**, alinhadas a custo, retorno e eficiência operacional.

Embora os resultados numéricos dependam de hipóteses e do contexto específico de cada campanha, a estrutura apresentada é diretamente aplicável a cenários reais de CRM Analytics, oferecendo um framework claro para priorização de clientes e avaliação de trade-offs de negócio.

---

## Status

**POC concluída**

Este repositório representa uma entrega fechada e consolidada, demonstrando a aplicação de CRM Analytics para suporte estruturado à decisão em campanhas de marketing.

---

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Disclaimer

A **CampaignSense** é uma Proof of Concept desenvolvida com fins demonstrativos, voltada à documentação e avaliação de abordagens analíticas para otimização de campanhas de marketing.

Os dados utilizados são públicos e não contêm informações pessoais, sensíveis ou sigilosas.  
Este projeto não deve ser utilizado diretamente em ambientes produtivos sem as devidas adaptações.

---

## Onde me encontrar

[![Website](https://img.shields.io/badge/🌐%20Website-Portfólio-black)](https://jhonathan.me)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jhonathandomingues)
[![Email](https://img.shields.io/badge/Email-Contato-success?logo=minutemailer&logoColor=white)](mailto:hello@jhonathan.me)
