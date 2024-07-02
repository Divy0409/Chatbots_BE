from rest_framework import viewsets
from ..models.chatbots import Chatbots
from ..serializers.chatbots import ChatbotSerializer

class ChatbotViewSet(viewsets.ModelViewSet):
    queryset = Chatbots.objects.all()
    serializer_class = ChatbotSerializer
