# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.api import Api
from .api.users import Users
from .api.user_userid_new import UserUseridNew


routes = [
    dict(resource=Api, urls=['/api'], endpoint='api'),
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=UserUseridNew, urls=['/user/<userid>/new'], endpoint='user_userid_new'),
]