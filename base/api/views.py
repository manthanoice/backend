from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .serializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
)
from base.models import Paragraph
from rest_framework import status
from .serializers import ParagraphSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view.
    """
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom token refresh view.
    """
    serializer_class = CustomTokenRefreshSerializer


@api_view(['GET'])
def get_routes(request):
    """
    API view for getting available routes.
    """
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)


@permission_classes([IsAuthenticated])
class MyView(APIView):
    """
    API view for adding paragraphs.
    """
    def post(self, request):
        """
        Method for adding paragraphs.
        """
        paragraphs = request.data.split('\n\n')  # Split input data by double new lines to get paragraphs.
        for paragraph in paragraphs:
            words = ' '.join(paragraph.split()).lower()  # Convert paragraph to lowercase words.
            p = Paragraph.objects.create(text=paragraph, words=words)  # Create a Paragraph object.
        return Response({"message": "Paragraph added successfully"}, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
class MyGetView(APIView):
    """
    API view for getting paragraphs.
    """
    def get(self, request):
        """
        Method for getting paragraphs.
        """
        word = request.query_params.get('word').lower()  # Get the search word from query parameters.
        paragraphs = Paragraph.objects.filter(words__contains=word).order_by('-created_at')[:10]  # Get 10 Paragraph objects containing the search word.
        serializer = ParagraphSerializer(paragraphs, many=True)  # Serialize the Paragraph objects.
        return Response(serializer.data)  # Return the serialized Paragraph objects as a response.
