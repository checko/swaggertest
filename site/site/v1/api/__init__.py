# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter

userslist=    [
        {
            'email' : 'abc@abc',
            'realname' : 'abc.lin'
        }
    ]
class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]
