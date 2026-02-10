# CampaignSense

**CRM Analytics para Otimização de Campanhas de Marketing**

![Author](https://img.shields.io/badge/author-Jhonathan%20Domingues-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Em%20desenvolvimento-yellow)

![Python](https://img.shields.io/badge/python-3.12.5-blue?logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ml-scikit--learn-orange?logo=scikitlearn&logoColor=white)
![Data](https://img.shields.io/badge/data-Pandas%20%7C%20NumPy-blue)
![Stats](https://img.shields.io/badge/stats-SciPy-informational)
![Viz](https://img.shields.io/badge/viz-Matplotlib%20%7C%20Seaborn-purple)

![CampainSense](imagens/thumbnail.png)

---

## Visão Geral

A **CampaignSense** é uma Proof of Concept (POC) de **CRM Analytics** voltada à **otimização de campanhas de marketing**, com foco explícito em **decisão de negócio** e **impacto financeiro**.

A proposta da POC é demonstrar como dados de clientes e histórico de campanhas podem ser utilizados para **priorizar contatos**, reduzindo desperdício de orçamento e maximizando o **lucro esperado** de uma campanha.

O projeto trata modelos de Machine Learning como **componentes de suporte à decisão**, e não como um fim em si mesmos. O valor central da solução está na conexão clara entre:

* dados de clientes;
* estimativa de propensão à resposta;
* regras de decisão;
* impacto financeiro esperado.

---

## Problema de Negócio

Em campanhas de marketing tradicionais, é comum que empresas impactem grandes parcelas da base de clientes sem distinção clara de potencial de retorno, o que leva a:

* desperdício de orçamento com clientes de baixa propensão;
* baixo retorno incremental das campanhas;
* dificuldade de justificar decisões de targeting com base em critérios objetivos.

A **CampaignSense** endereça esse problema ao propor uma abordagem orientada a **profit targeting**, na qual apenas clientes com **retorno esperado positivo** são priorizados para contato.

---

## Escopo da POC

No estado atual, a CampaignSense contempla:

* análise exploratória orientada à decisão de negócio;
* segmentação de clientes para identificação de perfis comportamentais;
* modelagem preditiva de propensão à resposta;
* definição explícita de regras de decisão baseadas em ganho e custo;
* geração de artefatos analíticos que suportam decisões de campanha.

---

## Fonte dos Dados

A POC utiliza um **dataset público**, originalmente disponibilizado como parte de um **case técnico de CRM Analytics**.

Esse case foi proposto no contexto de um processo seletivo conduzido por uma **grande empresa do setor de delivery no Brasil**, com o objetivo de avaliar abordagens analíticas para otimização de campanhas de marketing.

O dataset circulou por meio de repositórios públicos de código, hoje indisponíveis, e é amplamente conhecido e utilizado como referência prática em estudos e demonstrações de **CRM Analytics**.

Nesta POC, os dados são utilizados exclusivamente como base analítica para demonstrar a construção de uma solução orientada à decisão e ao impacto financeiro, sem qualquer vínculo institucional ou comercial com a empresa que originou o case.

---

## Estrutura do Projeto

```
campainsense/
│
├── data/
│   ├── raw/
│   └── processed/
├── imagens/
│   └── thumbnail.png
├── src/
│   └── paths.py
├── notebooks/
│   ├── 01-data_audit_eda.ipynb
│   └── 02-eda_decision.ipynb
├── references/
│   └── 01_dicionario_de_dados.md
├── reports/
├── requirements.txt
└── README.md
```

---

## Como Rodar o Projeto

Criação do ambiente virtual e instalação das dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Status

**Em desenvolvimento**

Este README representa o estado inicial do projeto e será consolidado ao final da execução da POC, refletindo com precisão o pipeline implementado, os artefatos gerados e os resultados alcançados.

---

## Pipeline Atual

A solução segue um pipeline lógico de alto nível:

1. Preparação e análise dos dados de clientes e campanhas
2. Identificação de padrões comportamentais relevantes
3. Estimativa de propensão à resposta
4. Conversão do score em decisão de negócio
5. Avaliação do impacto financeiro esperado

Os detalhes técnicos de cada etapa serão consolidados ao final da execução da POC.

---

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Disclaimer

A **CampaignSense** é uma Proof of Concept desenvolvida com fins demonstrativos, voltada à documentação e avaliação de abordagens analíticas para otimização de campanhas de marketing.

Os dados utilizados são públicos e não contêm informações pessoais, sensíveis ou sigilosas.
Este projeto **não deve ser utilizado em ambientes produtivos**.

---

## Onde me encontrar

[![Website](https://img.shields.io/badge/🌐%20Website-Portfólio-black)](https://jhonathan.me)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue?logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/jhonathandomingues)
[![Email](https://img.shields.io/badge/Email-Contato-success?logo=minutemailer\&logoColor=white)](mailto:hello@jhonathan.me)

