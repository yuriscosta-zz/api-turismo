from rest_framework.serializers import ModelSerializer

from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'complemento', 'cidade',
                  'estado', 'pais', 'latitude', 'longitude')
