import re
import uuid
import random
from datetime import date, datetime
from flask.json import jsonify
from bson.objectid import ObjectId
from pymongo.common import validate
from utils.exceptions import PermissaoInvalida
from models.validacoes import Validacoes
from utils.exceptions import ImovelNaoEncontrado
from utils.database.database import Database

class Imoveis_Models():

    def __init__(self):
        self.db = Database()

        self.validacoes = Validacoes()

    
    def criar_imovel(self, usuario, titulo, descricao, categoria, tipo, cidade, bairro, valor, tamanho, quartos,
     suites, banheiros, vagas_garagem, elevador_servico, piscina_infantil, interfone, quadra_esportes,
     jardim, playground, academia, espaco_gourmet, lavanderia, portaria24h, salao_festas, link_youtube):
        corretor = self.db.select_one_object('usuarios', {'_id': usuario['_id']})
        codigo_imovel = ''
        verify = False

        while verify == False:
            for x in range(5):
                numero = random.randrange(0,9)
                codigo_imovel += str(numero)

            imovel = self.db.select_one_object('imoveis', {'codigo': codigo_imovel})

            if imovel  ==  None:
                verify = True
        
        tipos = ['apartamento', 'casa', 'casa_comercial', 'casa_condominio', 'cobertura', 'flat', 'ponto_comercial']
        categorias = ['venda', 'locacao']

        if categoria not in categorias:
            return jsonify({
                'status': 'erro',
                'menssagem': 'categoria invalida',
                'codigo-requisicao': 'in303'
            })

        if tipo not in tipos:
            return jsonify({
                'status': 'erro',
                'menssagem': 'tipo invalido',
                'codigo-requisicao': 'in303'
            })

        

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

        self.db.insert_object(imovel, 'imoveis')

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel criado com sucesso',
            'imovel': imovel

        })


    def exibir_todos_imoveis(self):
        imoveis_ativos = self.db.select_object('imoveis', {'status': 'ativo'})
        imoveis_inativos = self.db.select_object('imoveis', {'status': 'inativo'})
        
        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imoveis encontrados com sucesso',
            'codigo-requisicao': 'in200',
            'imoveis_ativos': imoveis_ativos,
            'imoveis_inativos': imoveis_inativos
        })

    
    def editar_imovel(self, imovel_id, usuario, titulo, descricao, categoria, tipo, cidade, bairro, valor, tamanho, quartos,
     suites, banheiros, vagas_garagem, elevador_servico, piscina_infantil, interfone, quadra_esportes,
     jardim, playground, academia, espaco_gourmet, lavanderia, portaria24h, salao_festas, link_youtube):
        imovel = self.db.select_one_object('imovies', {'_id': imovel_id})
        if usuario['_id'] != imovel['corretor_id']:
            raise PermissaoInvalida()

        tipos = ['apartamento', 'casa', 'casa_comercial', 'casa_condominio', 'cobertura', 'flat', 'ponto_comercial']
        categorias = ['venda', 'locacao']

        if categoria not in categorias:
            return jsonify({
                'status': 'erro',
                'menssagem': 'categoria invalida',
                'codigo-requisicao': 'in303'
            })

        if tipo not in tipos:
            return jsonify({
                'status': 'erro',
                'menssagem': 'tipo invalido',
                'codigo-requisicao': 'in303'
            })

        if tipo is not None:
            imovel['tipo'] = tipo

        if categoria is not None:
            imovel['categoria'] =  categoria

        if cidade is not None:
            imovel['cidade'] = cidade

        if bairro is not None:
            imovel['bairro'] = bairro

        titulo= self.validacoes.string(titulo, 50, 'titulo')
        if titulo is not None:
            imovel['titulo'] = titulo

        descricao = self.validacoes.string(descricao, 2000, 'descricao')
        if descricao is not None:
            imovel['descricao'] = descricao

        valor = self.validacoes.int(valor, 9, 'valor')
        if valor is not None:
            imovel['valor'] = valor

        tamanho = self.validacoes.int(tamanho, 9, 'tamanho')
        if tamanho is not None:
            imovel['tamanho'] = tamanho

        quartos = self.validacoes.int(quartos, 2, 'quartos')
        if quartos  is not None:
            imovel['quartos'] = quartos

        suites = self.validacoes.int(suites, 2, 'suites')
        if suites is not None:
            imovel['suites'] = suites

        banheiros = self.validacoes.int(banheiros, 2, 'banheiuros')
        if banheiros is not None:
            imovel['banheiros'] = banheiros

        vagas_garagem = self.validacoes.int(vagas_garagem, 2, 'vagas_garagem')
        if vagas_garagem is not None:
            imovel['vagas_garagem'] = vagas_garagem
        #extras
        piscina_infantil = self.validacoes.booleano(piscina_infantil)
        if piscina_infantil is not None:
            imovel['extras']['piscina_infantil'] = piscina_infantil

        interfone = self.validacoes.booleano(interfone)
        if interfone is not None:
            imovel['extras']['interfone'] = None

        quadra_esportes = self.validacoes.booleano(quadra_esportes)
        if quadra_esportes is not None:
            imovel['extras']['quadra_esportes'] = quadra_esportes

        jardim = self.validacoes.booleano(jardim)
        if jardim is not None:
            imovel['extras']['jardim'] = jardim

        playground = self.validacoes.booleano(playground)
        if playground is not None:
            imovel['extras']['playground'] = playground

        academia = self.validacoes.booleano(academia)
        if academia is not None:
            imovel['extras']['academia'] = academia

        espaco_gourmet = self.validacoes.booleano(espaco_gourmet)
        if espaco_gourmet is not None:
            imovel['extras']['espaco_gourmet'] = espaco_gourmet

        lavanderia = self.validacoes.booleano(lavanderia)
        if lavanderia is not None:
            imovel['extras']['lavanderia'] = lavanderia

        portaria24h = self.validacoes.booleano(portaria24h)
        if portaria24h is not None:
            imovel['extras']['portaria24h'] = portaria24h

        elevador_servico = self.validacoes.booleano(elevador_servico)
        if elevador_servico is not None:
            imovel['extras']['elevador_servico'] = elevador_servico

        salao_festas= self.validacoes.booleano(salao_festas)
        if salao_festas is not None:
            imovel['extras']['salao_festas'] = salao_festas

        if link_youtube is not None:
            imovel['link_youtube'] = link_youtube

        self.db.update_object(imovel, 'imoveis', {'_id': imovel_id})

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel editado com sucesso',
            'codigo-requisicao': 'in200',
            'imovel': imovel
        })


    def excluir_imovel(self, imovel_id, usuario):
        usuario = self.db.select_one_object('usuarios', {'_id': usuario['_id']})

        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel['corretor_id'] != usuario['_id']:
            if usuario['permissoes']['excluir_imoveis'] != True:
                raise PermissaoInvalida()
        
        self.db.delete_one('imoveis', {'_id': imovel_id})

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel deletado com sucesso',
            'codigo-requisicao': 'in200'
        })


    def inativar_imovel(self, imovel_id, usuario):
        usuario = self.db.select_one_object('usuarios', {'_id': usuario['_id']})

        imovel = self.db.select_one_object('imoveis', {'_id': imovel_id})

        if imovel['corretor_id'] != usuario['_id']:
            if usuario['permissoes']['inativar_imoveis'] != True:
                raise PermissaoInvalida()
        
        imovel['status'] = 'inativado'

        self.db.update_object(imovel, 'imoveis', {'_id': imovel_id})
        imovel['_id'] = str(imovel['_id'])

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imovel inativado com sucesso',
            'codigo-requisicao': 'in200',
            'imovel': imovel
        })

    
    def ativar_imovel(self):
        pass


    def busca_personalizada(self, tipo, categoria, bairro, valor, quartos, imovel_id, corretor_id):
        query = {'status': 'ativo'}

        print(categoria)
        if categoria is not  None:
            categoria = categoria.lower()
            categorias = ['venda', 'aluguel', 'aluguel_temporada']

            if  categoria not in categorias:
                return jsonify({
                    'status': 'erro',
                    'menssagem': 'esse tipo  de imovel n??o existe',
                    'codigo-requisicao': 'in404'
                })

            query['categoria'] = categoria

        if tipo is not None:
            query['tipo'] = tipo

        if bairro is not None:
            query['bairro'] = bairro

        if valor is not  None:
            valor = re.search(r'(?P<min>\d*)-(?P<max>\d*)', valor)
            min = int(valor.group('min'))
            max = int(valor.group('max'))

            valores = []

            for x in range(max - min + 1):
                valores.append(x + min)

            query['valor'] = { "$in" : valores }

        if quartos is not None:
            query['quartos'] = int(quartos)

        if imovel_id is not  None:
            query['_id'] = imovel_id

        if corretor_id is not None:
            query['corretor_id'] = corretor_id

        print(query)
        imoveis =  self.db.select_object('imoveis',  query)

        if imoveis == []:
            raise ImovelNaoEncontrado()

        return  jsonify({
            'codigo-requisicao': 'in200',
            'menssagem': 'imoveis encontrados com sucesso',
            'imoveis': imoveis
            })

    
    def meus_imoveis(self, corretor_id):
        imoveis_ativos = self.db.select_object('imoveis', {'corretor_id': corretor_id, 'status': 'ativo'})
        imoveis_inativos = self.db.select_object('imoveis', {'corretor_id': corretor_id, 'status': 'inativo'})

        return jsonify({
            'status': 'sucesso',
            'menssagem': 'imoveis encontrados com sucesso',
            'codigo-requisicao': 'in200',
            'imoveis_ativos': imoveis_ativos,
            'imoveis_inativos': imoveis_inativos
        })