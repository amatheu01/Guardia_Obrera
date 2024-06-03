from rest_framework import serializers

from .models import TbDplanificacion, TbDregionGuardia, TbDposta, TbDgrupoGuardia, TbNtipoIncidencia, TbDvariable, TbNhorario, TbRregionHorarioTurno, TbDpatron


class Planificacion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDplanificacion
        fields = '__all__'


class RegionGuardia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDregionGuardia
        fields = '__all__'


class Posta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDposta
        fields = '__all__'


class GrupoGuardia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDgrupoGuardia
        fields = '__all__'


class TipoIncidencia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbNtipoIncidencia
        fields = '__all__'


class Variable_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDvariable
        fields = '__all__'


class Horario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbNhorario
        fields = '__all__'


class Turno_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbRregionHorarioTurno
        fields = '__all__'


class Patron_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TbDpatron
        fields = '__all__'
