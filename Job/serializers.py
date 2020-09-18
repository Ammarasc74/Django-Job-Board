### geting data from model ---->> json

from rest_framework import  serializers
from .models import job


class jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'