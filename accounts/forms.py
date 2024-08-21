from django import forms
from .models import News, Team, Player, Match, Event

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'city', 'founded']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'position', 'number', 'team']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['team_home', 'team_away', 'date', 'location', 'goals_home', 'goals_away', 'completed']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_type', 'player', 'minute']
