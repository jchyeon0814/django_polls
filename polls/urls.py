from django.urls import path
from . import views

app_name = 'polls' #URL 네임스페이스 설정

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', views.ResultsView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]