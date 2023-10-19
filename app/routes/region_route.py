from flask import Blueprint, request, jsonify
from app import db
from app.models import Region

region_bp = Blueprint('region_bp', __name__)


@region_bp.route('/v1/region/add', methods=['POST'])
def add_region():
    data = request.json
    name = data.get('name')
    id = data.get('id')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    if not id:
        return jsonify({'error': 'id is required'}), 400

    region = Region.query.filter_by(name=name).first()
    if region:
        return jsonify({'error': 'Region with this name already exists'}), 400

    region_2 = Region.query.filter_by(id=id).first()
    if region_2:
        return jsonify({'error': 'Region with this id already exists'}), 400

    region = Region(id=id, name=name)
    db.session.add(region)
    db.session.commit()

    return jsonify({'message': 'Region added successfully'}), 200


@region_bp.route('/v1/region/update', methods=['POST'])
def update_region():
    data = request.json
    id = data.get('id')
    new_id = data.get('new_id')

    if not id or not new_id:
        return jsonify({'error': 'ID and new_id are required'}), 400

    region = Region.query.get(id)
    if not region:
        return jsonify({'error': 'Region not found'}), 400

    region.id = new_id
    db.session.commit()

    return jsonify({'message': 'Region updated successfully'}), 200


@region_bp.route('/v1/region/delete', methods=['POST'])
def delete_region():
    id = request.json.get('id')

    if not id:
        return jsonify({'error': 'ID is required'}), 400

    region = Region.query.get(id)
    if not region:
        return jsonify({'error': 'Region not found'}), 400

    db.session.delete(region)
    db.session.commit()

    return jsonify({'message': 'Region deleted successfully'}), 200


@region_bp.route('/v1/region/get', methods=['GET'])
def get_region():
    id = request.json.get('id')

    if not id:
        return jsonify({'error': 'ID is required'}), 400

    region = Region.query.get(id)
    if not region:
        return jsonify({'error': 'Region not found'}), 400

    return jsonify({'id': region.id, 'name': region.name}), 200


@region_bp.route('/v1/region/get/all', methods=['GET'])
def get_all_regions():
    regions = Region.query.all()
    region_list = [{'id': region.id, 'name': region.name} for region in regions]

    return jsonify(region_list), 200
