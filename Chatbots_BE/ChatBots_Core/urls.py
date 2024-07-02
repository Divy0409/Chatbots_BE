# ChatBots_Core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chatbots/', views.ChatbotListView.as_view(), name='chatbot-list'),
    # Add more API endpoints as needed
]
