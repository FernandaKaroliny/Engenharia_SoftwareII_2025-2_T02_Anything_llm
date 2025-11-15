# Anything-LLM – Análise de Padrões Arquiteturais

Este repositório contém a implementação completa da Atividade 1 de Engenharia de Software II (2025.2), cujo objetivo é **analisar padrões arquiteturais ao longo da evolução de um projeto real do GitHub utilizando modelos de linguagem (LLMs)**.

A equipe desenvolveu um pipeline automatizado capaz de:
- Baixar e analisar um repositório alvo;
- Processar seu conteúdo (código-fonte, documentação e estrutura);
- Executar **3+ modelos Hugging Face** para identificar padrões arquiteturais;
- Comparar a eficácia dos modelos;
- Gerar resultados reproducíveis em JSON/CSV.

---

## 📌 1. Projeto Analisado
Este estudo utiliza como alvo o repositório:
> **[Anything-LLM](https://github.com/Mintplex-Labs/anything-llm)**

O projeto foi escolhido por apresentar:
- Estrutura modular clara;
- Utilização de diversas camadas arquiteturais;
- Evolução consistente ao longo do tempo;
- Relação direta com processamento de linguagem natural.

---

## 📌 2. Estrutura do Repositório
```
├── entradas/            # Arquivos de entrada utilizados pela equipe
│
├── src/                 # Código-fonte principal
│   ├── Modelos/         # Scripts dos modelos utilizados
│   └── RunModels.py     # Execução central dos modelos
│
├── resultados/          # Resultados gerados pelos modelos
│   ├── modelos.csv
│   ├── padroes.json
│   └── logs/
│
├── docs/                # Documentação do projeto
│   └── tutorial.pdf
│
├── requirements.txt     # Dependências do projeto
└── README.md            # Este documento

```
## 📌 3. Modelos Utilizados
O estudo utilizou **cinco modelos** do Hugging Face para ampliar a diversidade de análise:

Modelos utilizados:
- **bart-large-cnn** – sumarização e auxílio na compreensão estrutural
- **bart-large-mnli** – classificação e verificação de correspondência entre padrões
- **Llama-3.2-1B-Instruct** – análise arquitetural orientada a prompts
- **Qwen2.5-Coder-1.5B-Instruct** – excelente para análise de arquivos de código
- **all-MiniLM-L6-v2** – geração de embeddings para similaridade e agrupamento

Cada modelo recebeu como entrada fragmentos do projeto alvo e produziu como saída:
- Classes detectadas
- Categorias (Controller, Service, Repository, Utils...)
- Justificativa textual
- Relações arquiteturais

Os Resultados estão disponíveis em `resultados`.

## 📌 4. Requisitos do Sistema
### ✔️ Dependências
Instale todas as dependências com:
```
pip install -r requirements.txt
```
Principais libs:
- transformers
- sentence-transformers
- torch
- accelerate
- bitsandbytes
- tqdm
- scikit-learn
- GitPython

### ✔️ Infraestrutura
Este projeto foi executado com os seguintes recursos:
- GPU: **NVIDIA GeForce RTX 3070 (8 GB VRAM)**
- CPU: **Ryzen 7 5700x3d**
- RAM: **32 GB**
- Ambiente Python 3.12

> A infraestrutura é importante pois modelos maiores podem estourar a memória

---

## 📌 5. Como Executar o Projeto
### **1️⃣ Clonar o repositório**
```
git clone https://github.com/FernandaKaroliny/Engenharia_SoftwareII_2025-2_T02_Anything_llm
cd Engenharia_SoftwareII_2025-2_T02_Anything_llm
```

### **2️⃣ Instalar dependências**
```
pip install -r requirements.txt
```

### **3️⃣ Rodar o pipeline principal**
```
python src/run.py
```

Este script realiza:
1. Clonagem do projeto alvo;
2. Extração de arquivos relevantes;
3. Processamento e limpeza;
4. Execução dos modelos Hugging Face;
5. Salvamento dos resultados em `results/`.

---

## 📌 6. Resultados
Os resultados são gerados automaticamente:
- `results/padroes.json` → Lista de padrões arquiteturais detectados
- `results/modelos.csv` → Comparação dos modelos
- `results/logs/` → Execuções detalhadas

Além disso, o PDF do tutorial contém uma análise aprofundada, incluindo:
- Comportamento dos modelos
- Vantagens e limitações
- Impacto da arquitetura do Anything-LLM

---

## 📌 7. Tutorial (Documento Escrito)
O arquivo PDF completo está em:
```
docs/tutorial.pdf
```
Ele contém:
- Introdução
- Metodologia
- Análise dos modelos
- Discussão dos padrões identificados
- Conclusões

## 📌 8. Equipe
baixo está a tabela detalhada de contribuição dos integrantes:

| Nome                                   | Matrícula    | Contribuição                                                                                                |
| -------------------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| **Breno Henrique Do Carmo Santos**     | 202200078737 | Pesquisa, teste de modelos, padronização dos modelos, elaboração do tutorial e edição do vídeo e documento. |
| **Carla Stefany R. Santos**            | 202400060148 | Pesquisa, teste de modelos, elaboração do tutorial, edição e formatação do documento.                       |
| **Fernanda Karoliny Santos Silva**     | 202200092431 | Pesquisa, edição do documento, formatação do documento.                                                     |
| **João Paulo Menezes Machado**         | 202300038743 | Pesquisa, análise do projeto, edição do documento.                                                          |
| **João Vinícius De Almeida Argolo**    | 202200025573 | Pesquisa, teste de modelos, elaboração do tutorial e edição do documento.                                   |
| **José Arthur Calixto Da Rocha Costa** | 202300038770 | Pesquisa, teste de modelos, elaboração do tutorial e edição do documento.                                   |
| **Vinícius Azevedo Peroba**            | 201900076892 | Pesquisa, análise do projeto, apuração dos testes, edição do documento.                                     |
| **Wendel Alexsander Gomes Menezes**    | 202300027740 | Pesquisa, análise do projeto, apuração dos testes, edição do documento.                                     |
---


