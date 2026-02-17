import os
from pathlib import Path

import environ
import requests
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Get products from fastprint"

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
    env = environ.Env(FASTPRINT_USER=(str, ""), FASTPRINT_PASS=(str, ""))

    username = env("FASTPRINT_USER")
    password = env("FASTPRINT_PASS")

    def handle(self, *args, **options):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

        payload = f"username={self.username}&password={self.password}"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        if response.status_code != 200:
            raise CommandError(
                f"Failed to get products from fastprint\nresponse.status_code: {response.status_code}\n{response.text}"
            )

        with open("raw.json", "w") as f:
            f.write(response.text)
