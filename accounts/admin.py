from django.contrib import admin
from .models import News, Team, Player, Match, Event

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded', 'points', 'matches_played', 'wins', 'draws', 'losses', 'goals_for', 'goals_against', 'goal_difference')
    search_fields = ('name', 'city')
    list_filter = ('founded',)
    ordering = ('-points',)

    def goal_difference(self, obj):
        return obj.goals_for - obj.goals_against
    goal_difference.short_description = 'Goal Difference'

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'number', 'position', 'goals', 'yellow_cards', 'red_cards')
    search_fields = ('name',)
    list_filter = ('team', 'position')
    ordering = ('team', 'number')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_home', 'team_away', 'date', 'location', 'goals_home', 'goals_away', 'completed', 'result')
    search_fields = ('team_home__name', 'team_away__name')
    list_filter = ('date', 'team_home', 'team_away', 'completed')
    ordering = ('-date',)

    def result(self, obj):
        return obj.result()
    result.short_description = 'Result'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('match', 'player', 'event_type', 'minute')
    search_fields = ('match__team_home__name', 'match__team_away__name', 'player__name')
    list_filter = ('event_type', 'minute')
    ordering = ('match', 'minute')
