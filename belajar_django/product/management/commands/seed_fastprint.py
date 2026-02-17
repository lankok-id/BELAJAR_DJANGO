import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from product.models import Category, Product, Status


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    BASE_DIR = Path(__file__).resolve().parent

    def handle(self, *args, **options):
        self.stdout.write("Starting seed process...")

        seeder_file = f"{self.BASE_DIR}/raw.json"
        data = self._read_file(seeder_file)

        seeders = data["data"]
        for seeder in seeders:
            try:
                category = Category.objects.get_or_create(name=seeder["kategori"])[0]  # type: ignore
                status = Status.objects.get_or_create(name=seeder["status"])[0]  # type: ignore
                product = Product.objects.get_or_create(  # type: ignore
                    name=seeder["nama_produk"],
                    price=seeder["harga"],
                    category_id=category,
                    status_id=status,
                )[0]

                self.stdout.write(f"Product '{product.name}' created successfully")

            except Exception as e:
                raise CommandError(
                    f"Failed to create product '{seeder['nama_produk']}': {e}"
                )

    def _read_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            raise CommandError(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            raise CommandError(f"File '{file_path}' not found")
        except Exception as e:
            raise CommandError(f"Failed to load seeder data: {e}")

        return data
