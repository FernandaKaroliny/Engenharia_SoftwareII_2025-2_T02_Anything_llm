import json
import requests

def listar_estrutura(repo_url):
    parts = repo_url.strip("/").split("/")
    user, repo = parts[-2], parts[-1]

    repo_info_url = f"https://api.github.com/repos/{user}/{repo}"
    repo_info = requests.get(repo_info_url).json()
    if "default_branch" not in repo_info:
        print("Erro ao acessar repositório:", repo_info)
        return None

    branch = repo_info["default_branch"]

    api_url = f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(api_url)

    if response.status_code != 200:
        print("Erro ao acessar árvore de diretórios:", response.json())
        return None

    data = response.json()
    arquivos = [item["path"] for item in data["tree"] if item["type"] == "blob"]
    pastas = sorted(set("/".join(path.split("/")[:-1]) for path in arquivos if "/" in path))

    return pastas
