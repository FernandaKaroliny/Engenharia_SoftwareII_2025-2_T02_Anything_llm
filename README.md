# Engenharia_SoftwareII_2025-2_T02_Anything_llm

## 📋 Sobre o Projeto
Este repositório destina-se a conter os dados necessários para a análise de padrões arquiteturais do repositório AnythingLLM utilizando modelos do Hugging Face para identificação de padrões e estruturas de software.

## 📚 Documentação
- **[Fundamentação Teórica e Metodologia](https://docs.google.com/document/d/1R-D4VtqfLO1I6LkJB5Rm5mj4UGxH5rFzmwhnGCyFdDc/edit?usp=sharing)** - Base teórica, metodologia e referências
- **[Tutorial Prático](https://docs.google.com/document/d/1IlnZnfeqwm33-1T7Oq_By6wTV-1whWtv88dz1jKWHtg/edit?usp=sharing)** - Guia passo a passo para testar os modelos

## 👥 Integrantes
- BRENO HENRIQUE DO CARMO SANTOS - [202200078737]
- CARLA STEFANY R. SANTOS - [202400060148]
- FERNANDA KAROLINY SANTOS SILVA - [202200092431]
- JOÃO PAULO MENEZES MACHADO - [202300038743]
- JOÃO VINÍCIUS DE ALMEIDA ARGOLO - [202200025573]
- JOSÉ ARTHUR CALIXTO DA ROCHA COSTA - [202300038770]
- VINÍCIUS AZEVEDO PEROBA - [201900076892]
- WENDEL ALEXSANDER GOMES MENEZES - [202300027740]

## 🔗 Repositório Original
- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** - Repositório analisado no projeto

- Utiliza-se os modelos 
- bart-large-cnn
- Llama-3.2-1B-Instruct
- Qwen2.5-Coder-1.5B-Instruct
- all-MiniLM-L6-v2

# Tutorial de Instalação e Execução do Modelo

## 1. Dependências Necessárias

Antes de iniciar, verifique se o ambiente possui os seguintes componentes instalados:

- Python 3.12
- transformers
- torch
- accelerate

---

## 2. Criando e Ativando o Ambiente Virtual (venv)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalando as Dependências

Com o ambiente virtual ativado:

```bash
pip install -q transformers torch accelerate
pip install torch torchvision torchaudio --index-url 
pip install transformers accelerate tokenizers sentencepiece bitsandbytes huggingface-hub safetensors
```

---

## 4. Importando as Bibliotecas

```python
import os
import torch
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

```
---
## 4.1 Colab (Adicional)
```
from IPython.display import clear_output
from google.colab import drive 
```
## 5. Executando o Script

```bash
python seu_script.py
```

Seu ambiente está pronto para rodar modelos!

