from rest_framework import serializers
from turne.models import Cantor, Pais, Turne

class CantorSerializer(serializers.ModelSerializer):
    """Modelo e campos a serem utilizados"""
    class Meta:
        model = Cantor
        fields = ['id','nome','estilo']


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['pais', 'continente', 'populacao', 'data_criacao']


class TurneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turne
        fields = '__all__'


class TurneCantorSerializer(serializers.ModelSerializer):
    """
    Defino objeto 'pais' e 'modelo' para que a API mostre os nomes completos e não apenas o id.
    """
    pais = serializers.ReadOnlyField(source='pais.pais')
    modelo = serializers.SerializerMethodField()
    class Meta:
        model = Turne
        fields = ['pais','modelo']
    def get_modelo(self, obj):
        return obj.get_modelo_display()


class TurnesPaisSerializer(serializers.ModelSerializer):
    cantor_nome = serializers.ReadOnlyField(source='cantor.nome')
    modelo = serializers.SerializerMethodField()
    class Meta:
        model = Turne
        fields = ['cantor_nome', 'modelo']
    def get_modelo(self, obj):
        return obj.get_modelo_display()