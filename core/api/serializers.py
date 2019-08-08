from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico
from enderecos.models import Endereco
from atracoes.models import Atracao

from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(many=False)

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'endereco',
                  'descricao_completa')
        # ready_only_fields = ('comentarios', 'avaliacoes', 'atracoes')

    def create_endereco(self, endereco, ponto):
        novo_endereco = Endereco.objects.create(**endereco)
        ponto.endereco = novo_endereco

    def create_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']
        
        ponto = PontoTuristico.objects.create(**validated_data)

        self.create_atracoes(atracoes, ponto)
        self.create_endereco(endereco, ponto)

        return ponto

    def get_descricao_completa(self, obj):
        return '{}: {}'.format(obj.nome, obj.descricao)
