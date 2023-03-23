from rest_framework import serializers
from .models import Award


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'picture', 'description', 'conditions', 'entry', 'rank', 'necessary_docs')
