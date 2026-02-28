# IA-LLM-Providers

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

Camada de *adapters* em Python para integrar múltiplos provedores de LLM no mesmo projeto (OpenAI, Anthropic, Groq, Ollama, xAI, etc.).  
O foco aqui é organização: cada provedor fica isolado em `providers/`, com credenciais via `.env` e exemplos simples no `main.py`.

## Estrutura

```text
.
├─ providers/
│  ├─ openai.py
│  ├─ anthropic.py
│  ├─ google.py
│  ├─ groq.py
│  ├─ ollama.py
│  └─ xai.py
├─ main.py
├─ requirements.txt
├─ .env
├─ .gitignore
└─ README.md
```

## Requisitos

- Python 3.10+
- Um ambiente virtual (recomendado)

## Instalação

```bash
git clone https://github.com/0dayig0r/IA-LLM-Providers.git
cd IA-LLM-Providers
python -m venv venv
```

**Windows (PowerShell)**
```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/macOS**
```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um `.env` na raiz:

```env
OPENAI_API_KEY=...
# ANTHROPIC_API_KEY=...
# GROQ_API_KEY=...
# GOOGLE_API_KEY=...
# XAI_API_KEY=...
```

> Não comite o `.env`. Deixe ele no `.gitignore`.

## Como rodar

```bash
python main.py
```

## Exemplos

Os exemplos variam de acordo com o provider, mas a ideia é sempre a mesma: importar a função do adapter e chamar.

### Visão / leitura de imagem por URL (ex.: OpenAI)

```py
from providers.openai import image_reader

result = image_reader("https://site.com/imagem.png")
print(result)
```

### Resposta estruturada com Pydantic (ex.: OpenAI)

```py
from providers.openai import book_finder

book = book_finder("Clean Code")
print(book.title, book.author)
```

## Adicionando um novo provider

1. Crie um arquivo em `providers/<nome>.py`
2. Leia a chave do `.env`
3. Exponha uma função simples (ex.: `generate_text`, `vision`, `parse_structured`)
4. Mantenha detalhes do SDK dentro do adapter (o resto do projeto não deve “sentir” o provider)

## License

MIT — veja [LICENSE](./LICENSE).
