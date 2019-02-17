from django.urls import path

from . import views

app_name = "weather"
urlpatterns = [
    path('', views.index, name='index'),
    path('comfortAsk/', views.comfortAsk, name='comfortAsk'),
    path('submission/', views.submission, name='submission')
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]