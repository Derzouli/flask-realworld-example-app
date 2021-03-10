# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from conduit.user.models import User  # noqa
from flask_jwt_extended.internal_utils import user_lookup
from flask_jwt_extended.internal_utils import has_user_lookup
from flask_jwt_extended.exceptions import UserLookupError
from flask_jwt_extended.config import config

def jwt_identity(jwt_header, jwt_data):
    if not has_user_lookup():
        return None

    # https://flask-jwt-extended.readthedocs.io/en/stable/_modules/flask_jwt_extended/view_decorators/
    identity = jwt_data[config.identity_claim_key]
    return User.get_by_id(identity)


def identity_loader(user):
    print(user)
    return user.id
