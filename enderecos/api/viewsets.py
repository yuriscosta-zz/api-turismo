from rest_framework.viewsets import ModelViewSet

from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_fields = ('cidade', 'estado', 'pais')
