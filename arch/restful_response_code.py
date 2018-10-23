# -*- coding: utf-8 -*-

__RESP_CODE_SUCCESS__ = '0000'
"""
请求成功
"""

__RESP_CODE_USER_INFO_INVALID__ = '1000'
"""
用户信息校验失败
请求的用户信息校验失败，可能是用户未登录，或token过期
"""

__RESP_CODE_SERVER_ERROR__ = '5000'
"""
服务器异常
5XX，4XX等异常状态码
"""

__RESP_CODE_RESTFUL_ERROR__ = '8000'
"""
自定义
业务逻辑异常。如请求参数不合法等，respMsg由开发人员指定，默认为“请求异常”
"""

__RESP_CODE_OTHER_ERROR__ = '9999'
"""
其他异常
"""
