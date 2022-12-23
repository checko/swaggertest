# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from . import userslist

class newuser(Resource):

    def post(self, userid):
        print(userid)
        user = {
                'email': request.get_json().get('email'),
                'realname': request.get_json().get('realname')
                }
        userslist.append(user)
        print(userslist)

        return None, 200, None
