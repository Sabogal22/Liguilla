from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accounts/signup/', accounts_views.signup, name='signup'),  # Descomentar si tienes una vista de registro
    # path('accounts/profile/', accounts_views.profile, name='profile'),  # Descomentar si tienes un perfil del usuario
    path('accounts/', include('accounts.urls')),  # Incluir las URLs de la aplicación accounts
    path('', accounts_views.home, name='home'),  # Página de inicio
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
