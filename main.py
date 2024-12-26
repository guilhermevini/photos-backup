import argparse
import datetime
import logging
import os
import time

import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import requests
from google.auth.transport.requests import Request

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuração da API Google Photos
SCOPES = ["https://www.googleapis.com/auth/photoslibrary.readonly"]
API_SERVICE_NAME = "photoslibrary"
API_VERSION = "v1"
CLIENT_SECRET_FILE = "client_secret.json"
TOKEN_FILE = "token.json"

# Diretório para salvar fotos
PHOTO_DIR = "photos"
if not os.path.exists(PHOTO_DIR):
    os.makedirs(PHOTO_DIR)


def get_credentials():
    """Autentica o usuário e retorna as credenciais."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file(
            TOKEN_FILE
        )
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds


def download_photo(photo):
    """Baixa uma foto do Google Photos e organiza por ano/mês/dia."""
    mime_type = photo.get("mimeType", "Desconhecido")
    filename = photo.get("filename", "Desconhecido")
    url = photo["baseUrl"]

    # Verifica se é um vídeo e ajusta o URL
    if mime_type.startswith("video/"):
        url += "=dv"  # Sufixo para baixar vídeos em tamanho completo
    else:
        url += "=d"  # Sufixo para baixar fotos em tamanho completo

    # Pegue a data de criação e formate
    creation_time = photo.get("mediaMetadata", {}).get("creationTime", "unknown_date")
    if creation_time == "unknown_date":
        logger.warning(
            "Data de criação não encontrada para a foto: %s", photo["filename"]
        )
        return

    # Extraia ano, mês e dia
    creation_date = datetime.datetime.fromisoformat(creation_time.replace("Z", ""))
    year = creation_date.year
    # month = f"{creation_date.month:02d}"  # Adiciona zero à esquerda se necessário
    # day = f"{creation_date.day:02d}"

    # Crie o diretório com base na data
    date_dir = os.path.join(PHOTO_DIR, str(year))
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)

    # Caminho completo do arquivo
    filepath = os.path.join(date_dir, photo["filename"])

    logger.info(
        "Nome: %s, Tipo: %s, Data de Criação: %s", filename, mime_type, creation_time
    )

    if os.path.exists(filepath):
        logger.info("Arquivo já existe e será mantido: %s", filepath)
        return

    try:
        logger.info("Baixando: %s", filepath)
        response = requests.get(url)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)

        creation_datetime = datetime.datetime.fromisoformat(
            creation_time.replace("Z", "")
        )
        timestamp = creation_datetime.timestamp()
        os.utime(filepath, (timestamp, timestamp))  # Ajusta o acesso e modificação
    except requests.RequestException as e:
        logger.error("Erro ao baixar %s: %s", filepath, e)


def get_photos_and_download():
    """Obtém e baixa fotos por página."""
    creds = get_credentials()
    service = googleapiclient.discovery.build(
        API_SERVICE_NAME,
        API_VERSION,
        credentials=creds,
        static_discovery=False,
    )
    page_token = None

    while True:
        try:
            response = (
                service.mediaItems().list(pageSize=100, pageToken=page_token).execute()
            )
            photos = response.get("mediaItems", [])
            if not photos:
                logger.info("Nenhuma foto encontrada na página.")
                break

            # Baixe as fotos da página atual
            for photo in photos:
                download_photo(photo)

            # Verifique se há mais páginas
            page_token = response.get("nextPageToken")
            if not page_token:
                break

            # Timeout para evitar limites de taxa
            time.sleep(5)
        except googleapiclient.errors.HttpError:
            logger.warning("Atingido limite de taxa. Esperando 60 segundos...")
            time.sleep(60)
        except Exception as e:
            logger.error("Erro ao processar página: %s", e)
            break


def main():
    get_photos_and_download()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download photos from Google Photos")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    main()
