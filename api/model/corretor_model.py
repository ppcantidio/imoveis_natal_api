from marshmallow import Schema


class CorretorSchema(Schema):
    nmNome = fields.String(required=True)
    nmEmail = fields.String(required=True)
    nmSenha = fields.String(required=True) # adicionar validacao extra para senha
    nmTelefone = fields.String(required=True)
    tpTipo = fields.String(required=True)
    tpStatus = fields.String(required=True)



 usuario = {
            '_id': uuid.uuid4().hex,
            'nome': nome,
            'email': email,
            'senha': pbkdf2_sha256.encrypt(senha),
            'telefone': telefone,
            'tipo': 'corretor',
            'status': 'ativo',
            'permissoes': {
                'criar_usuarios': False,
                'excluir_usuarios': False,
                'excluir_imoveis': False,
                'editar_imoveis': False,
                'inativar_imoveis': False,
                'ativar_imoveis': False,
                'editar_permissoes': False,
                'inativar_usuarios': False,
                'ativar_usuarios': False
            }
        }