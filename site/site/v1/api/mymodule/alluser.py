# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from .. import Resource
from ... import schemas
from .. import userslist


class alluser(Resource):

    def get(self):
        msg = {
                'data' : userslist
            }
        print(msg)

        return make_response(msg, 200)
