from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import get_connection, EmailMessage
from rest_framework.views import APIView


from .models import Car, Color, Material, CarImage, FAQ, ContactMessage
from .serializers import (
    CarSerializer, ColorSerializer, MaterialSerializer,
    CarImageSerializer, FAQSerializer, ContactMessageSerializer
)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category", "transmission", "drive_type", "fuel_type", "status", "year"]
    search_fields = ["brand", "model", "description"]
    ordering_fields = ["price", "year", "max_speed", "acceleration"]


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()

        # Отправляем email при создании сообщения
        send_mail(
            subject=f"New contact message from {message.name}",
            message=f"Email: {message.email}\n\nMessage:\n{message.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],  # куда будут приходить сообщения
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ContactMessageAPIView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.save()

            try:
                # Создаём соединение с SMTP сервером
                connection = get_connection(
                    host='bereketlilogistika.com',
                    port=465,
                    username='dev@bereketlilogistika.com',
                    password='(;fjlr&([yn6',
                    use_ssl=True
                )

                # Формируем письмо
                email = EmailMessage(
                    subject=f"New message from {message.name}",
                    body=f"Email: {message.email}\n\nMessage:\n{message.message}",
                    from_email='dev@bereketlilogistika.com',
                    to=['sanjarberdiyew66@gmail.com'],
                    connection=connection
                )

                # Отправка письма
                email.send()
            except Exception as e:
                return Response(
                    {"error": f"Ошибка при отправке письма: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FAQListAPIView(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)