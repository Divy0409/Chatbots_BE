from rest_framework import generics
from ..models.chatbots import Chatbots
from ..serializers.chatbots import ChatbotSerializer

class ChatbotListView(generics.ListAPIView):
    queryset = Chatbots.objects.all()
    serializer_class = ChatbotSerializer
