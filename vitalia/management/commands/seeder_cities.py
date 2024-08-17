from django.core.management import BaseCommand

from doctors.models.city import City


class Command(BaseCommand):
    help = "Seeder of the database. Cities are filled with data."
    CITIES = [
        'Madrid',
        'Barcelona',
        'Valencia',
        'Sevilla',
        'Zaragoza',
        'Málaga',
        'Murcia',
        'Palma',
        'Las Palmas de Gran Canaria',
        'Bilbao',
        'Alicante',
        'Córdoba',
        'Valladolid',
        'Vigo',
        'Gijón',
        'Granada',
        'Oviedo',
        'San Sebastián',
        'Huelva',
        'Jerez de la Frontera',
        'Lérida',
        'Tarragona',
        'Albacete',
        'León',
        'Salamanca',
        'Cáceres',
        'Toledo',
        'Segovia',
        'Soria',
        'Huesca',
        'Jaén',
        'Ciudad Real',
        'Santa Cruz de Tenerife',
        'San Fernando',
        'Algeciras',
        'Ponferrada',
        'Melilla',
        'Ceuta',
        'Ronda',
        'Guadalajara',
        'Cádiz',
        'Pontevedra',
        'La Coruña',
        'Ourense'
        ]

    def add_arguments(self, parser):
        pass

    def handle (self, *args, **options):
        print("SEEDER STARTED")
        print("Creating cities")
        for city in self.CITIES:
            try:
                City.objects.create(name=city)
                print(f"{city} created")
            except Exception as e:
                pass
        print("SEEDER FINISHED")