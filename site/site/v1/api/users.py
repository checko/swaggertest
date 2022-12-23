# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response

from . import Resource
from .. import schemas
from .mymodule.alluser import alluser

class Users(Resource):

    def get(self):
        my = alluser()

        return my.get()
