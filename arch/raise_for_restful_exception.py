# -*- coding: utf-8 -*-
from arch.restful_response_code import __RESP_CODE_OTHER_ERROR__
from arch.restful_response_code import __RESP_CODE_RESTFUL_ERROR__
from arch.restful_response_code import __RESP_CODE_SERVER_ERROR__
from werkzeug.exceptions import HTTPException


class ResponseException(Exception):
    def __init__(self, error_code, error_msg):
        self.errorCode = error_code or __RESP_CODE_OTHER_ERROR__
        self.errorMsg = error_msg or '其他异常'


class RestfulException(ResponseException):
    """
    error_code=8000
    """

    def __init__(self, error_msg):
        self.errorMsg = error_msg
        self.errorCode = __RESP_CODE_RESTFUL_ERROR__
        self.errorMsg = error_msg or '其他异常'


def convert_exception(e):
    """
    判断当前异常的类型，如果不为RestfulException，则将其转换为 :type ResponseException
    :param e: Exception
    :return: ResponseException
    """
    if isinstance(e, RestfulException):
        return e
    elif isinstance(e, HTTPException):
        return ResponseException(__RESP_CODE_SERVER_ERROR__, '服务器异常')
    else:
        return ResponseException(__RESP_CODE_OTHER_ERROR__, '其他异常')
