# -*- coding: utf-8 -*-
from flask import jsonify

from .messages import MSG_ALREADY_EXISTS, MSG_SUCCESS
from .messages import MSG_INVALID_DATA, MSG_DOES_NOT_EXIST, MSG_EXCEPTION


def resp_data_invalid(resource: str, errors: object, msg: str = MSG_INVALID_DATA):
    '''
    Responses 400 Unprocessable Entity
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })

    resp.status_code = 400

    return resp


def resp_exception(resource: str, description: str = '', msg: str = MSG_EXCEPTION):
    '''
    Responses 500
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })

    resp.status_code = 500

    return resp


def resp_does_not_exist(resource: str, description: str, message=None):
    '''
    Responses 404 Not Found
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    if not message:
        message = MSG_DOES_NOT_EXIST.format(description)

    resp = jsonify({
        'resource': resource,
        'message': message,
    })
    resp.status_code = 404

    return resp


def resp_already_exists(resource: str, description: str):
    '''
    Responses 400
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description),
    })
    resp.status_code = 400

    return resp


def resp_ok(resource: str, message: str, data=None, **extras):
    '''
    Responses 200
    '''
    if not resource:
        resource = ''

    if not message:
        message = MSG_SUCCESS

    response = {'status': 200, 'message': message, 'resource': resource}

    if data:
        response['dados'] = data

    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 200

    return resp


def resp_error(resource: str, errors: object, msg: str = MSG_INVALID_DATA):
    '''
    Responses 400
    '''

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma string.')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })

    resp.status_code = 400

    return resp
