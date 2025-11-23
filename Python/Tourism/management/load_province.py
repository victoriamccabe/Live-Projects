from django.core.management.base import BaseCommand
from Tourism.models import Province

class Command(BaseCommand):
    help = 'Load Argentine provinces with latitude and longitude'

    def handle(self, *args, **options):
        provinces = [
            ("Buenos Aires", -34.6037, -58.3816),
            ("Catamarca", -28.4696, -65.7852),
            ("Chaco", -27.4516, -58.9867),
            ("Chubut", -43.3002, -65.1023),
            ("Córdoba", -31.4201, -64.1888),
            ("Corrientes", -27.4712, -58.8321),
            ("Entre Ríos", -31.3929, -58.0177),
            ("Formosa", -26.1854, -58.1759),
            ("Jujuy", -24.1858, -65.2995),
            ("La Pampa", -36.6167, -64.2833),
            ("La Rioja", -29.4131, -66.8558),
            ("Mendoza", -32.8908, -68.8272),
            ("Misiones", -27.3627, -55.9009),
            ("Neuquén", -38.9516, -68.0591),
            ("Río Negro", -40.8135, -62.9967),
            ("Salta", -24.7821, -65.4232),
            ("San Juan", -31.5375, -68.5364),
            ("San Luis", -33.295, -66.3356),
            ("Santa Cruz", -51.6333, -69.2167),
            ("Santa Fe", -31.6333, -60.7000),
            ("Santiago del Estero", -27.7951, -64.2615),
            ("Tierra del Fuego", -54.8019, -68.3029),
            ("Tucumán", -26.8083, -65.2176),
        ]

        for name, lat, lon in provinces:
            obj, created = Province.objects.get_or_create(
                name=name,
                defaults={'latitude': lat, 'longitude': lon}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Added: {name}'))
            else:
                self.stdout.write(f'Exists: {name}')