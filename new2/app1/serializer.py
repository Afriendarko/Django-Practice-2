from rest_framework import serializers
from .models import feedback, students

class feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = "__all__"

class studentsserializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = "__all__"