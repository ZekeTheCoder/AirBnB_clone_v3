#!/usr/bin/python3
""" view for handling User objects in API """
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ retrieve all user objects """
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return (jsonify(list_users))


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves a user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404, description="user_id is not linked to any User object")

    return (jsonify(user.to_dict()))


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ delete user object """

    user = storage.get(User, user_id)

    if not user:
        abort(404, description="user_id is not linked to any User object")

    user.delete()
    storage.save()

    return (make_response(jsonify({}), 200))


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """ create user object """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    storage.new(instance)
    storage.save()
    return (make_response(jsonify(instance.to_dict()), 201))


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """ Update usr """
    user = storage.get(User, user_id)

    if not user:
        abort(404, description="user_id is not linked to any User object")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return (make_response(jsonify(user.to_dict()), 200))
