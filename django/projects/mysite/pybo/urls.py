from django.urls import path, re_path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_>/', views.detail, name="detail"),
    path('<int:id_>/answer/', views.answer_create, name="answer_create"),
    path('question/create/', views.question_create, name="question_create"),
    path('question/modify/<int:id_>/', views.question_update, name="question_update"),
    path('question/delete/<int:id_>/', views.question_delete, name="question_delete"),
    path('answer/modify/<int:id_>', views.answer_update, name="answer_update"),
    path('answer/delete/<int:id_>', views.answer_delete, name="answer_delete"),
]
