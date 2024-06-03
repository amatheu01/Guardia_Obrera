from rest_framework import serializers

from .models import TbDpersona


class TbDpersona_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpersona
        fields = '__all__'