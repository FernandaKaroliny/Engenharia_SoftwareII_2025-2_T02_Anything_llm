import json
from collections import Counter, defaultdict

# =========================
# CONFIGURAÇÕES
# =========================
ARQUIVO_JSON = "avalia_md.json"   # JSON de entrada
ARQUIVO_TXT_SAIDA = "avalia_md.txt"  # TXT de saída

# =========================
# LEITURA DO JSON
# =========================
try:
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        dados = json.load(f)
except FileNotFoundError:
    print(f"Arquivo {ARQUIVO_JSON} não encontrado.")
    exit()
except json.JSONDecodeError as e:
    print(f"Erro ao ler JSON: {e}")
    exit()

if not dados:
    print("Nenhum dado encontrado no arquivo JSON.")
    exit()

# =========================
# CÁLCULOS ESTATÍSTICOS
# =========================
contagem_padroes = Counter()
soma_confiancas = defaultdict(float)

for item in dados:
    padrao = item.get("padrao_arquitetural", "Desconhecido")
    confianca = item.get("confianca", 0)
    contagem_padroes[padrao] += 1
    soma_confiancas[padrao] += confianca

total_arquivos = len(dados)
padrao_mais_comum = contagem_padroes.most_common(1)[0]
padrao_nome = padrao_mais_comum[0]
padrao_qtd = padrao_mais_comum[1]
padrao_confianca_media = soma_confiancas[padrao_nome] / padrao_qtd if padrao_qtd > 0 else 0

# =========================
# GRAVAÇÃO DO TXT
# =========================
with open(ARQUIVO_TXT_SAIDA, "w", encoding="utf-8") as f:
    f.write("=== RESULTADOS DA CLASSIFICAÇÃO DE PADRÕES ARQUITETURAIS ===\n\n")

    for item in dados:
        f.write(f"Arquivo: {item.get('arquivo', 'N/A')}\n")
        f.write(f"Padrão Arquitetural: {item.get('padrao_arquitetural', 'N/A')}\n")
        f.write(f"Confiança: {item.get('confianca', 0):.2%}\n")
        resumo = item.get('resumo', '').strip().replace("\n", " ")
        f.write(f"Resumo: {resumo}\n")
        f.write("-" * 60 + "\n")

    f.write("\n=== ESTATÍSTICAS GERAIS ===\n")
    f.write(f"Total de arquivos analisados: {total_arquivos}\n\n")
    f.write("Distribuição de padrões detectados:\n")

    for padrao, qtd in contagem_padroes.most_common():
        confianca_media = soma_confiancas[padrao] / qtd
        f.write(f" - {padrao}: {qtd} ocorrências (média {confianca_media:.1%})\n")

    f.write("\n=== PADRÃO MAIS PROVÁVEL ===\n")
    f.write(f"Padrão predominante: {padrao_nome}\n")
    f.write(f"Ocorrências: {padrao_qtd}\n")
    f.write(f"Confiança média: {padrao_confianca_media:.1%}\n")

print(f"✅ Conversão concluída!")
print(f"📁 Resultados salvos em: {ARQUIVO_TXT_SAIDA}")