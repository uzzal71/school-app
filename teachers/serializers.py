from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('id', 'user_profile', 'first_name', 'last_name', 'email', 'mobile', 'address')