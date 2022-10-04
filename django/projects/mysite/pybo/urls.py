from django.urls import path, re_path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_>/', views.detail, name="detail"),
    path('<int:id_>/answer/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name="question_create")
]
