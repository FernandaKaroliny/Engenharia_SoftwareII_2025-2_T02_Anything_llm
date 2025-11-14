import os
import re
import json
import unicodedata
import time
from transformers import pipeline
import subprocess

# =========================
# CONFIGURAÇÕES
# =========================

CAMINHO_REPO = "anything-llm"  # Substitua pelo caminho do repositório
LIMITE_CARACTERES = 3000  # Limite máximo por análise
ARQUIVO_SAIDA = "avalia_md.json"
ARQUIVO_SAIDA_TXT = "avalia_md.txt"

PADROES = [
    "Client-Server (a centralized server provides resources or services to multiple clients over a network)",
    "Blackboard (components work cooperatively by reading and writing shared data on a common knowledge base)",
    "Shared-Data (components communicate indirectly through shared data repositories or databases)",
    "Data-Model (the architecture centers around structured data schemas and access layers)",
    "Publish-Subscribe (components communicate asynchronously through message topics or events)",
    "Service-Oriented Architecture (system organized into reusable services communicating via standardized interfaces)",
    "Peer-to-Peer (decentralized network where each node can act as both client and server)",
    "Pipe-Filter (data flows through a sequence of processing steps, each transforming the input into output)",
    "Layers (system organized into hierarchical layers like presentation, logic, and data access)",
    "Microservices (independently deployable small services communicating via APIs or messaging)",
    "Blockchain (distributed ledger storing transactions in cryptographically linked blocks)"
]

# =========================
# MODELOS
# =========================

print("🧠 Carregando modelos...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# =========================
# FUNÇÕES AUXILIARES
# =========================

def limpar_markdown(texto):
    """Remove partes irrelevantes de arquivos .md"""
    texto = unicodedata.normalize("NFKD", texto)
    texto = re.sub(r"```.*?```", "", texto, flags=re.DOTALL)  # blocos de código
    texto = re.sub(r"!\[.*?\]\(.*?\)", "", texto)  # imagens
    texto = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", texto)  # links [texto](url)
    texto = re.sub(r"http\S+", "", texto)  # urls soltas
    texto = re.sub(r"(^|\n)[#>\-\*\+]+\s*", "\n", texto)  # títulos, listas
    texto = re.sub(r"\n\s*\n+", "\n", texto)  # espaços múltiplos
    texto = re.sub(r" +", " ", texto)  # espaços duplos
    return texto.strip()

def dividir_texto(texto, limite):
    """Divide texto em partes menores respeitando o limite de caracteres"""
    partes = []
    while len(texto) > limite:
        corte = texto[:limite].rfind(".")
        if corte == -1:
            corte = limite
        partes.append(texto[:corte])
        texto = texto[corte:]
    if texto.strip():
        partes.append(texto.strip())
    return partes

# =========================
# PROCESSAMENTO
# =========================

resultados = []

tempo_execucao = time.perf_counter()

for raiz, _, arquivos in os.walk(CAMINHO_REPO):

    for nome_arquivo in arquivos:
        if nome_arquivo.endswith(".md"):
            caminho = os.path.join(raiz, nome_arquivo)
            print(f"\n📄 Lendo {caminho}")

            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                conteudo = f.read()

            conteudo_limpo = limpar_markdown(conteudo)


            # Salvar entrada original limpa em TXT
            with open("entradas_processadas.txt", "a", encoding="utf-8") as entrada_saida:
                entrada_saida.write(f"\n\n===== {caminho} =====\n")
                entrada_saida.write(conteudo_limpo)
                entrada_saida.write("\n")

            if not conteudo_limpo.strip():
                print("⚪ Ignorado (sem conteúdo relevante)")
                continue

            partes = dividir_texto(conteudo_limpo, LIMITE_CARACTERES)
            resumo_final = ""

            for i, parte in enumerate(partes):

                input_length = len(parte.split())
                # Ajusta automaticamente os limites de resumo com base no tamanho da entrada
                max_len = max(40, int(input_length * 0.8))  # 80% do tamanho original, mínimo 40 tokens
                min_len = max(20, int(input_length * 0.3))  # 30% do tamanho original, mínimo 20 tokens
                
                try:
                    resumo = summarizer(parte,max_length=max_len,min_length=min_len, do_sample=False)[0]["summary_text"]
                    resumo_final += resumo + " "
                except Exception as e:
                    print(f"⚠️ Erro ao resumir parte {i+1}: {e}")

            if resumo_final.strip():
                try:
                    classificacao = classifier(
                        resumo_final,
                        candidate_labels=PADROES,
                        hypothesis_template="This project follows the following software architecture pattern: {}."
                    )
                    padrao_predito = classificacao["labels"][0]
                    confianca = classificacao["scores"][0]

                    print(f"🔹 {nome_arquivo}: {padrao_predito} ({confianca:.1%})")

                    resultados.append({
                        "arquivo": nome_arquivo,
                        "resumo": resumo_final.strip(),
                        "padrao_arquitetural": padrao_predito,
                        "confianca": round(confianca, 3)
                    })
                except Exception as e:
                    print(f"⚠️ Erro ao classificar {nome_arquivo}: {e}")

# =========================
# SALVAR RESULTADOS
# =========================

with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

try:
    subprocess.run(["python", "json_to_txt.py"], check=True)
    print("✅ Conversão concluída com sucesso!")
except subprocess.CalledProcessError as e:
    print(f"⚠️ Erro ao converter para txt: {e}")

tempo_execucao = time.perf_counter() - tempo_execucao    

print("\n✅ Análise concluída!")
print(f"📁 Resultados salvos em: {ARQUIVO_SAIDA_TXT} {ARQUIVO_SAIDA}")

print(f"⏱️ Tempo de execução {tempo_execucao}")

