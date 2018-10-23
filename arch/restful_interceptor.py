# -*- coding: utf-8 -*-

from flask import Flask, request
from enum import Enum
from arch.raise_for_restful_exception import ResponseException, convert_exception
import json
from flask import Response
from werkzeug.exceptions import HTTPException


def _to_json(resp):
    return Response(json.dumps(resp, default=lambda o: o.__dict__, sort_keys=True, indent=4))


def _handle_after_request(key, path, exception):
    exception = convert_exception(exception)
    return _to_json(exception)
    pass


class Ext:
    def __init__(self, app, platforms,func_before=None):
        if Flask != type(app):
            raise Exception('Illegal arguments: the type of app must be Flask.')
        if isinstance(platforms,Enum):
            raise Exception('Illegal arguments: the type of flatforms must be Enum.')
        if func_before is None:
            raise Exception('Illegal arguments: the type of func_before must not be null.')

        self.app = app
        self.func_before = func_before

        self.platforms = {}
        for name, member in platforms.__members__.items():
            self.platforms.update({name: {}})

        @self.app.before_request
        def before_request():
            request_path = str(request.url_rule)
            for key in self.platforms.keys():
                for path in self.platforms[key]:
                    if path == request_path:
                        func_before(key, path, request)
                        break

        @self.app.errorhandler(ResponseException)
        def on_error(e):
            request_path = str(request.url_rule)
            for key in self.platforms.keys():
                for path in self.platforms[key]:
                    if path == request_path:
                        return _handle_after_request(key,path,e)
            pass

        @self.app.errorhandler(HTTPException)
        def on_http_error(e):
            request_path = str(request.url_rule)
            for key in self.platforms.keys():
                for path in self.platforms[key]:
                    if path == request_path:
                        return _handle_after_request(key, path, e)
            pass

    def annote(self, suffix, platform, check_login=False):
        def decorate(f):
            if platform.name not in self.platforms.keys():
                raise Exception('Illegal argument for platform')
            paths = self.platforms.get(platform.name)
            if suffix in paths.keys():
                raise Exception('Illegal argument for suffix: ' + suffix + " already exist")

            paths[suffix] = check_login

        return decorate

