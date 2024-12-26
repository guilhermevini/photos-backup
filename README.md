# photos-backup

Open-source tool for backing up photos and videos using the Google Photos API.

![License](https://img.shields.io/badge/license-GPLv3-blue)
![Python](https://img.shields.io/badge/python-3.13.1-blue)
![Python Linter](https://github.com/guilhermevini/photos-backup/actions/workflows/python-linter.yml/badge.svg)
![Docker Compose Validation](https://github.com/guilhermevini/photos-backup/actions/workflows/docker-compose-validation.yml/badge.svg)

- [Português (Brasil)](README.pt-br.md)

## Features

- **Organized backups:** Photos and videos are downloaded and organized by year.
- **Wide compatibility:** Supports formats such as `.jpg`, `.heic`, `.mp4`, `.mov`, and more.
- **Local interface:** Use Photoview to browse your photos through a modern and responsive UI.
- **Open source:** Distributed under the GPLv3 license.

## How to Run the Importer

Make sure you have [pyenv](https://github.com/pyenv/pyenv) installed to manage your Python version.

```bash
# Install and set up Python version
pyenv install 3.13.1
pyenv local 3.13.1 # or use pyenv global 3.13.1

# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```

## How to Run Photoview

Make sure you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

```bash
# Start Photoview
make all

# Open in browser
open http://localhost:8000/
```

## Credits and Reused Files

The following files were directly obtained from the official [Photoview repository](https://github.com/photoview/photoview):

- `.env`
- `docker-compose.yml`
- `Makefile`

These files have been adapted for use in this project and retain the original structure from Photoview. For more information, visit the official Photoview repository.

## Acknowledgments

This project was created with the help of [ChatGPT](https://openai.com/chatgpt), a language model developed by OpenAI. The tool was used to assist with idea generation, code structuring, and project documentation.

## References

- [pyenv](https://github.com/pyenv/pyenv): Python version manager.
- [google-api-python-client](https://github.com/googleapis/google-api-python-client): Python client for Google APIs.
- [photoview](https://github.com/photoview/photoview): Photo and video gallery with metadata and AI support.
