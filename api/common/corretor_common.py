from api.mapper.corretor_mapper import CorretorMapper

class CorretorCommon:
    def insere_corretor(corretor_request):
        try:
            corretor = CorretorMapper().insere_corretor_mapper(corretor_request)
            CorretorDB().insere_corretor(corretor)
            corretor = CorretorMapper().retorna_corretor_mapper()
        except:
            pass