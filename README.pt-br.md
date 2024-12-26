# photos-backup

Ferramenta de código aberto para fazer backup de fotos e vídeos usando a API do Google Photos.

![License](https://img.shields.io/badge/license-GPLv3-blue)
![Python](https://img.shields.io/badge/python-3.13.1-blue)
![Python Linter](https://github.com/guilhermevini/photos-backup/actions/workflows/python-linter.yml/badge.svg)
![Docker Compose Validation](https://github.com/guilhermevini/photos-backup/actions/workflows/docker-compose-validation.yml/badge.svg)

- [English](README.en.md)

## Recursos

- **Backup organizado:** Fotos e vídeos são baixados e organizados por ano.
- **Compatibilidade ampla:** Suporte a formatos como `.jpg`, `.heic`, `.mp4`, `.mov`, entre outros.
- **Interface local:** Utilize o Photoview para visualizar suas fotos em uma interface moderna e responsiva.
- **Código aberto:** Distribuído sob a licença GPLv3.

## Como Rodar o Importador

Certifique-se de ter o [pyenv](https://github.com/pyenv/pyenv) instalado para gerenciar a versão do Python.

```bash
# Instale e configure a versão do Python
pyenv install 3.13.1
pyenv local 3.13.1 # ou use pyenv global 3.13.1

# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python main.py
```

## Como Rodar o Photoview

Certifique-se de ter o [Docker](https://www.docker.com/) e o [Docker Compose](https://docs.docker.com/compose/install/) instalados.

```bash
# Inicie o Photoview
make all

# Abra no navegador
open http://localhost:8000/
```

## Créditos e Arquivos Reutilizados

Os seguintes arquivos foram diretamente obtidos do repositório oficial do [Photoview](https://github.com/photoview/photoview):

- `.env`
- `docker-compose.yml`
- `Makefile`

Esses arquivos foram adaptados para uso neste projeto e mantêm a estrutura original do Photoview. Para mais informações, visite o repositório oficial do Photoview.

## Agradecimentos

Este projeto foi criado com a ajuda do [ChatGPT](https://openai.com/chatgpt), um modelo de linguagem desenvolvido pela OpenAI. A ferramenta foi utilizada para ajudar na geração de ideias, estruturação do código e documentação do projeto.

## Referências

- [pyenv](https://github.com/pyenv/pyenv) Gerenciador de versões Python.
- [google-api-python-client](https://github.com/googleapis/google-api-python-client) Cliente Python para APIs do Google.
- [photoview](https://github.com/photoview/photoview) Galeria de fotos e vídeos com suporte a metadados e IA.