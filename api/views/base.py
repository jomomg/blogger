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


def get_single_item(model_class, schema_class, item_id):
    obj_name = model_class.__name__.lower()
    item = model_class.get_or_404(item_id)
    schema = schema_class()
    ret = schema.dump(item).data
    return jsonify(success_(f'{obj_name} fetched', data=ret)), 200
