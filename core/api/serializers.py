from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico

from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    avaliacoes = AvaliacaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa')

    def get_descricao_completa(self, obj):
        return '{}: {}'.format(obj.nome, obj.descricao)
