from rest_framework import serializers
from ..models.chatbots import Chatbots

class ChatbotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatbots
        fields = '__all__'
