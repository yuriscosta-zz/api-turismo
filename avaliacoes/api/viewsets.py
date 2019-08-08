from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    filter_fields = ('usuario', 'comentario', 'nota', 'data')
