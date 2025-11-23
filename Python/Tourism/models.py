from django.db import models


class PlaceRecommendation(models.Model):

    place_name = models.CharField(max_length=100)  # Name of the place the user recommends
    description = models.TextField(max_length=200)  # Short description or reason why they recommend it
    your_name = models.CharField(max_length=100)  # User's name
    province = models.CharField(
        max_length=50,  # Droplist of provinces
        choices=[
            ('Buenos Aires', 'Buenos Aires'),
            ('Catamarca', 'Catamarca'),
            ('Chaco', 'Chaco'),
            ('Chubut', 'Chubut'),
            ('Ciudad Autónoma de Buenos Aires', 'Ciudad Autonoma de Buenos Aires'),
            ('Corrientes', 'Corrientes'),
            ('Córdoba', 'Cordoba'),
            ('Entre Ríos', 'Entre Rios'),
            ('Formosa', 'Formosa'),
            ('Jujuy', 'Jujuy'),
            ('La Pampa', 'La Pampa'),
            ('La Rioja', 'La Rioja'),
            ('Mendoza', 'Mendoza'),
            ('Misiones', 'Misiones'),
            ('Neuquen', 'Neuquen'),
            ('Rio Negro', 'Rio Negro'),
            ('Salta', 'Salta'),
            ('San Juan', 'San Juan'),
            ('San Luis', 'San Luis'),
            ('Santa Cruz', 'Santa Cruz'),
            ('Santa Fe', 'Santa Fe'),
            ('Santiago del Estero', 'Santiago del Estero'),
            ('Tierra del Fuego', 'Tierra del Fuego'),
            ('Tucumán', 'Tucuman'),
        ]
    )

    # Score
    score = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)],
        default=5,
    )

    def __str__(self):
        return f"{self.place_name} ({self.province}) - recommended by {self.your_name}"


