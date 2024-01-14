from ossapi import Ossapi
from typing import List
import sys
import logging

class AppConfig:
    # path of text file containing client_id and client_secret
    # set these at https://osu.ppy.sh/home/account/edit#oauth
    SECRETS_FILE = "secret_data.txt" # change this before git push obviously
    # API callback URL
    CALLBACK_URL = "http://localhost:3914"


def read_secrets(secrets_file: str) -> List[str]:
    try:
        with open (secrets_file, 'r') as file:
            client_id = file.readline().strip()
            client_secret = file.readline().strip()

            if not client_id or not client_secret:
                raise ValueError(f"File {secrets_file} did not contain valid client_id or client_secret.")
                sys.exit(1)
    except FileNotFoundError:
        # log err if file isn't found
        logging.error("Error: File not found. Make sure the file {secrets_file} exists.")
        sys.exit(1)
    except Exception as e:
        # log other exceptions
        logging.error(f"Error: {e}")
        sys.exit(1)

    return [client_id, client_secret]

if __name__ == "__main__":
    # initialize API with secrets
    client_id, client_secret = read_secrets(AppConfig.SECRETS_FILE)
    api = Ossapi(client_id, client_secret)

    # main script logic to be implemented
    sys.exit(0)