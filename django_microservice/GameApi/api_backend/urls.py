from django.urls import path
from .views import GamesListView

module_list = {
    'get': 'list',
}

urlpatterns = [
    path('games/', GamesListView.as_view(module_list), name='games-list'),
]