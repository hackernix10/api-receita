from rest_framework import serializers
from .models import Cpf

class CpfSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cpf
        fields = '__all__'