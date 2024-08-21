from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import News, Team, Player, Match, Event
from .forms import NewsForm, TeamForm, PlayerForm, MatchForm, EventForm
from django.contrib import messages

def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

def home(request):
    return render(request, 'home.html')

@login_required
def admin_dashboard(request):
    # Obtener datos relevantes
    num_matches = Match.objects.count()
    num_teams = Team.objects.count()
    num_players = Player.objects.count()
    num_news = News.objects.count()

    # Pasar datos a la plantilla
    context = {
        'num_matches': num_matches,
        'num_teams': num_teams,
        'num_players': num_players,
        'num_news': num_news,
    }
    
    return render(request, 'accounts/admin_dashboard.html', context)

def news(request):
    news_list = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_list, 10)  # Muestra 10 noticias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accounts/news/index.html', {'page_obj': page_obj})

@login_required
def news_list(request):
    # Obtiene todas las noticias ordenadas por fecha de creación
    news = News.objects.all().order_by('-created_at')
    return render(request, 'accounts/news/news_list.html', {'news': news})

@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'accounts/news/news_form.html', {'form': form})

@login_required
def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'accounts/news/news_form.html', {'form': form})

@login_required
def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'accounts/news/news_confirm_delete.html', {'news': news})

### Nuevas Vistas para Equipos y Jugadores

def team_list(request):
    teams = Team.objects.all()

    # Añadir la diferencia de goles a cada equipo
    for team in teams:
        team.goal_difference = team.goals_for - team.goals_against

    return render(request, 'accounts/teams/team_list.html', {'teams': teams})

@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'accounts/teams/team_form.html', {'form': form})

@login_required
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'accounts/teams/team_form.html', {'form': form})

@login_required
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'accounts/teams/team_confirm_delete.html', {'team': team})

def player_list(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = team.players.all().order_by('number')
    return render(request, 'accounts/players/player_list.html', {'team': team, 'players': players})

@login_required
def player_create(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            # Mensaje de éxito
            messages.success(request, 'Jugador creado exitosamente.')
            return redirect('player_list', team_id=team.id)
        else:
            # Mensaje de error
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = PlayerForm()
    return render(request, 'accounts/players/player_form.html', {'form': form, 'team': team})

@login_required
def player_update(request, team_id, pk):
    team = get_object_or_404(Team, pk=team_id)
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list', team_id=team.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'accounts/players/player_form.html', {'form': form, 'team': team})

@login_required
def player_delete(request, team_id, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list', team_id=team_id)
    return render(request, 'accounts/players/player_confirm_delete.html', {'player': player})

### Nuevas Vistas para Partidos y Eventos

def match_list(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'accounts/matches/match_list.html', {'matches': matches})

@login_required
def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'accounts/matches/match_form.html', {'form': form})

@login_required
def match_update(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm(instance=match)
    return render(request, 'accounts/matches/match_form.html', {'form': form})

@login_required
def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('match_list')
    return render(request, 'accounts/matches/match_confirm_delete.html', {'match': match})

@login_required
def event_create(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.match = match
            event.save()
            return redirect('match_list')
    else:
        form = EventForm()
    return render(request, 'accounts/events/event_form.html', {'form': form, 'match': match})

### Vista para la Tabla de Posiciones

def standings(request):
    teams = Team.objects.all().order_by('-points', '-goal_difference', '-goals_for')
    return render(request, 'accounts/standings.html', {'teams': teams})
