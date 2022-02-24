from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('voie/', views.VoieView.as_view(), name='voie'),
    path('sites/', views.SiteView.as_view(), name='sites'),
    path('secteurs/', views.SecteurView.as_view(), name='secteurs'),
]

