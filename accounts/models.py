from django.db import models
from django.utils import timezone

class News(models.Model):
  title = models.CharField(max_length=200)  # Título de la noticia
  content = models.TextField()  # Contenido de la noticia
  image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Imagen opcional
  created_at = models.DateTimeField(default=timezone.now)  # Fecha de creación

  def __str__(self):
    return self.title

class Team(models.Model):
  name = models.CharField(max_length=100)  # Nombre del equipo
  city = models.CharField(max_length=100)  # Ciudad del equipo
  founded = models.IntegerField()  # Año de fundación
  logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)  # Logo del equipo
  points = models.IntegerField(default=0)  # Puntos en la tabla de posiciones
  matches_played = models.IntegerField(default=0)  # Partidos jugados
  wins = models.IntegerField(default=0)  # Partidos ganados
  draws = models.IntegerField(default=0)  # Partidos empatados
  losses = models.IntegerField(default=0)  # Partidos perdidos
  goals_for = models.IntegerField(default=0)  # Goles a favor
  goals_against = models.IntegerField(default=0)  # Goles en contra

  def __str__(self):
    return self.name

  def goal_difference(self):
    return self.goals_for - self.goals_against

class Player(models.Model):
  POSITION_CHOICES = [
    ('GK', 'Portero'),
    ('DF', 'Defensa'),
    ('MF', 'Mediocampista'),
    ('FW', 'Delantero'),
  ]

  name = models.CharField(max_length=100)  # Nombre del jugador
  position = models.CharField(max_length=2, choices=POSITION_CHOICES)  # Posición del jugador
  number = models.IntegerField()  # Número de camiseta
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')  # Relación con el equipo
  goals = models.IntegerField(default=0)  # Goles anotados por el jugador
  yellow_cards = models.IntegerField(default=0)  # Tarjetas amarillas
  red_cards = models.IntegerField(default=0)  # Tarjetas rojas

  def __str__(self):
    return f"{self.name} ({self.get_position_display()}) - {self.team.name}"

class Match(models.Model):
  #team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
  team_home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches', default=1)
  #team_away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
  team_away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches', default=1)
  date = models.DateTimeField()
  location = models.CharField(max_length=200, blank=True, null=True)  # Lugar del partido
  goals_home = models.IntegerField(default=0)
  goals_away = models.IntegerField(default=0)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.team_home.name} vs {self.team_away.name} - {self.date.strftime('%d/%m/%Y')}"

  def result(self):
    if self.completed:
      return f"{self.goals_home} - {self.goals_away}"
    return "Partido no jugado aún"

class Event(models.Model):
  EVENT_CHOICES = [
    ('goal', 'Gol'),
    ('yellow_card', 'Tarjeta Amarilla'),
    ('red_card', 'Tarjeta Roja'),
  ]

  match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='events')
  player = models.ForeignKey(Player, on_delete=models.CASCADE)
  event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
  minute = models.IntegerField()

  def __str__(self):
    return f"{self.get_event_type_display()} - {self.player.name} ({self.minute}')"
