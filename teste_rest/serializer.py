# ----------------- The serializer is resposible to transform the model into JSON ---------------- #
from rest_framework import serializers
from .models import Pessoas


class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields =  '__all__'