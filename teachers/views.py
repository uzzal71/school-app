from rest_framework.response import Response 
from rest_framework import status
from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer

from profiles import permissions

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = (IsAuthenticated,)
