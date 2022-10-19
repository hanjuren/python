from django.urls import path, re_path
from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name="index"),
    path('<int:id_>/', base_views.detail, name="detail"),

    # question_views.py
    path('question/create/', question_views.question_create, name="question_create"),
    path('question/modify/<int:id_>/', question_views.question_update, name="question_update"),
    path('question/delete/<int:id_>/', question_views.question_delete, name="question_delete"),
    path('question/vote/<int:id_>/', question_views.question_vote, name="question_vote"),

    # answer_views.py
    path('<int:id_>/answer/', answer_views.answer_create, name="answer_create"),
    path('answer/modify/<int:id_>', answer_views.answer_update, name="answer_update"),
    path('answer/delete/<int:id_>', answer_views.answer_delete, name="answer_delete"),
    path('answer/vote/<int:id_>/', answer_views.answer_vote, name="answer_vote"),
]
