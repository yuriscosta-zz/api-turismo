from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # filter_fields = ('nome', 'descricao', 'aprovado')
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')
    # lookup_field = 'nome'

    # def get_queryset(self):
    #     return PontoTuristico.objects.all()
    #    id = self.request.query_params.get('id', None)
    #    nome = self.request.query_params.get('nome', None)
    #    descricao = self.request .query_params.get('descricao', None)

    #    queryset = PontoTuristico.objects.all()

    #    if id:
    #         return queryset.filter(id=id)
    #     if nome:
    #         queryset = queryset.filter(nome__iexact=nome)
    #     if descricao:
    #         queryset = queryset.filter(descricao__iexact=descricao)

    #     return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # @action(methods=['POST'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
