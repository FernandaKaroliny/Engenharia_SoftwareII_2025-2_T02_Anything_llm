import torch
import psutil
from transformers import AutoTokenizer, AutoModelForCausalLM
import listarestrutura as lt
import time
import os

prompts_testados = 0
#estrutura = lt.listar_estrutura("https://github.com/Mintplex-Labs/anything-llm") quando quiser listar a estrutura do repositório

# Exibe uso de memória
def mostrar_uso_memoria():
    processo = psutil.Process()
    mem_info = processo.memory_info().rss / (1024 ** 2)
    print(f" Memória RAM usada: {mem_info:.2f} MB")
    if device == "cuda":
        print(f"Memória GPU usada: {torch.cuda.memory_allocated(0) / (1024 ** 2):.2f} MB / "
              f"{torch.cuda.get_device_properties(0).total_memory / (1024 ** 2):.2f} MB totais")
        
def executarModelo(input_text):
   global prompts_testados
   prompts_testados += 1
   texto_avaliado = input_text
   inputs = tokenizer(texto_avaliado, return_tensors="pt").to(model.device)
  
   tempo_execucao = time.perf_counter()
   outputs = model.generate(**inputs, max_new_tokens=350, temperature=0.15, top_p=0.9)
   tempo_execucao = time.perf_counter() - tempo_execucao

   # Decodifica o texto completo
   decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
   print("\n_____________________________________________")
   print(f"Prompt testado nº: {prompts_testados}")
   print(f"\nTempo de execução do modelo: {tempo_execucao:.2f} segundos")
   mostrar_uso_memoria()
   print("\n" + decoded + "\n_____________________________________________ ")
   return decoded  # Extrai apenas a resposta gerada

# Caminho do modelo
model_path = r"F:\Windows 3.0\Downloads\Teste 1\Llama-3.2-1B-Instruct"  
# Utilizei um modelo baixado localmente, altere caso o modelo 
# esteja em outro diretorio ou no huggingface

print("Carregando modelo local:", model_path)
device = "cpu"
# Detecta GPU disponível
if torch.cuda.is_available():
   device = "cuda"
   print(f"GPU detectada: {torch.cuda.get_device_name(0)}")
else:
   device = "cpu"
   print("Nenhuma GPU detectada, rodando na CPU")


# Carrega modelo e tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto" if device == "cuda" else None
)

mostrar_uso_memoria()


for i in range(1, 4):
   with open(f"entradas/entrada{i}.txt", "r", encoding="utf-8") as f:
      arquivo = f.read()

      prompt = f"""

      {arquivo}

      Com base nas dependências, scripts e estrutura, descreva:
      1. Quais tecnologias principais o projeto utiliza (ex: Node.js, React, Express, Prisma, etc.).
      2. Qual o tipo de arquitetura que o projeto segue (ex: Monolítico, MVC, Microservices, Event-Driven, Client-Server, etc.).
      3. Quais diretórios ou pacotes indicam separação de responsabilidades (ex: 'server', 'frontend', 'collector').
      4. Como ocorre o fluxo de execução em desenvolvimento (baseando-se nos scripts `dev:*` e `setup`).
      5. Se o projeto parece voltado para execução local, em nuvem, ou ambos.
      6. Quais boas práticas ou convenções de arquitetura são evidentes (ex: uso de Prisma para ORM, divisão entre back e front, uso de Docker, etc.).
      7. Gere um pequeno resumo final explicando o propósito geral do projeto e seu padrão arquitetural principal.

      Responda em português de forma clara OBJETIVA, não repetitiva além de Avaliar a confiabilidade da sua resposta.
      """

      print(prompt)

      os.makedirs("respostas", exist_ok=True)

      arquivo = f"respostas/resposta{i}.txt"

      resposta = executarModelo(prompt)
      with open(arquivo, "w", encoding="utf-8") as f: 
         f.write(resposta)
      # Mostra uso de memória após geração

