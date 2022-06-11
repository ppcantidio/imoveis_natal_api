def retorna_mongodb_object(object):
    object['_id'] = str(object['_id'])
    return object