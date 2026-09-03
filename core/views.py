from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import BlockedCall
from .serializers import BlockedCallSerializer, UserSerializer, ChatSerializer

class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            # Aquí iría la lógica real con Gemini. Por ahora simulamos:
            response_text = f"He recibido tu mensaje: '{message}'. Estoy aquí para ayudarte con el bloqueo de llamadas."
            return Response({'response': response_text})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class BlockedCallViewSet(viewsets.ModelViewSet):
    serializer_class = BlockedCallSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BlockedCall.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
