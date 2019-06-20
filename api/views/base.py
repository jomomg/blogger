from flask import jsonify

from api.utils.response import success_


def create(model_class, schema_class, request):
    obj_name = model_class.__name__.lower()
    schema = schema_class()
    obj_data = schema.load_json(request.data)
    obj = model_class(**obj_data)
    obj.save()
    payload = schema.dump(obj).data
    return jsonify(success_(f'{obj_name} created', data=payload)), 201


def list_all(model_class, schema_class):
    obj_name = model_class.__name__.lower()
    schema = schema_class(many=True)
    objects = model_class.query.all()
    payload = schema.dump(objects).data
    return jsonify(success_(f'{obj_name}s fetched', data=payload)), 200
