# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from .mymodule.newuser import newuser

class UserUseridNew(Resource):

    def post(self, userid):
        my = newuser()

        return my.post(userid) 
