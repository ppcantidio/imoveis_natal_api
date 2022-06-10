from marshmallow import Schema, fields
from fields.marshmallow imagens String, Nested, List, Boolean


class ImovelSchema(Schema):
    corretor_id = fields.String(required=True)
    nmTitulo = fields.String(required=True)
    nmDescricao = fields.String(required=True)
    tpCategoria = fields.String(required=True) # validar categorias validas
    tpTipo = fields.String(required=True) # validar tipo valido
    obEndereco = fields.Nested(Endereco)
    lsExtras = fields.Nested(Extras)
    imagens = fields.List(fields.String)



class EnderecoSchema(Schema):
    pass

class ExtrasSchema(Schema):
    pass
imovel = {
            '_id': codigo_imovel,
            'corretor_id': corretor['_id'],
            'titulo': self.validacoes.string(titulo, 50, 'titulo'),
            'descricao': self.validacoes.string(descricao, 2000, 'descricao'),
            'categoria': categoria,
            'tipo': tipo,
            'cidade': cidade,
            'bairro': bairro,
            'valor': self.validacoes.int(valor, 9, 'valor'),
            'tamanho': self.validacoes.int(tamanho, 9, 'tamanho'),
            'quartos': self.validacoes.int(quartos, 2, 'quartos'),
            'suites': self.validacoes.int(suites, 2, 'suites'),
            'banheiros': self.validacoes.int(banheiros, 2, 'banheiuros'),
            'vagas_garagem': self.validacoes.int(vagas_garagem, 2, 'vagas_garagem'),
            'extras':{
                'piscina_infantil': self.validacoes.booleano(piscina_infantil),
                'interfone': self.validacoes.booleano(interfone),
                'quadra_esportes': self.validacoes.booleano(quadra_esportes),
                'jardim': self.validacoes.booleano(jardim),
                'playground': self.validacoes.booleano(playground),
                'academia': self.validacoes.booleano(academia),
                'espaco_gourmet': self.validacoes.booleano(espaco_gourmet),
                'lavanderia': self.validacoes.booleano(lavanderia),
                'portaria24h': self.validacoes.booleano(portaria24h),
                'elevador_servico': self.validacoes.booleano(elevador_servico),
                'sala_festas': self.validacoes.booleano(salao_festas)
            },
            'imagens': [],
            'link_youtube': link_youtube,
            'data_criacao': datetime.now(),
            'ultima_atualizacao':  datetime.now(),
            'status': 'inativo'
        }