from django.db import models
from django.utils import timezone

class News(models.Model):
  title = models.CharField(max_length=200)  # Título de la noticia
  content = models.TextField()  # Contenido de la noticia
  created_at = models.DateTimeField(default=timezone.now)  # Fecha de creación

  def __str__(self):
    return self.title

class Team(models.Model):
  name = models.CharField(max_length=100)  # Nombre del equipo
  city = models.CharField(max_length=100)  # Ciudad del equipo
  founded = models.IntegerField()  # Año de fundación

  def __str__(self):
    return self.name

class Player(models.Model):
  POSITION_CHOICES = [
    ('GK', 'Goalkeeper'),
    ('DF', 'Defender'),
    ('MF', 'Midfielder'),
    ('FW', 'Forward'),
  ]

  name = models.CharField(max_length=100)  # Nombre del jugador
  position = models.CharField(max_length=2, choices=POSITION_CHOICES)  # Posición del jugador
  number = models.IntegerField()  # Número de camiseta
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')  # Relación con el equipo

  def __str__(self):
    return f"{self.name} ({self.get_position_display()}) - {self.team.name}"
