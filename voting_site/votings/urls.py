from django.urls import path
from . import views
app_name='votings'

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /votings/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /votings/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]