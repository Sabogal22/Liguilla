from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import News
from .forms import NewsForm

def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')

def home(request):
    return render(request, 'home.html')

@login_required
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

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
        form = NewsForm(request.POST, instance=news)
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
