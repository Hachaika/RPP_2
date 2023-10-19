from flask import Blueprint, request, jsonify
from app.models import Region, AreaTaxParam
from app import db

area_bp = Blueprint('area_route', __name__)


@area_bp.route('/v1/area/tax-param/add', methods=['POST'])
def add_area_tax_param():
    data = request.get_json()
    id = data.get('id')
    city_id = data.get('city_id')
    rate = data.get('rate')

    region = Region.query.filter_by(id=city_id).first()
    if not region:
        return jsonify({'error': 'Region does not exist'}), 400

    area_tax_param = AreaTaxParam(id=id, city_id=city_id, rate=rate)
    db.session.add(area_tax_param)
    db.session.commit()

    return jsonify({'message': 'Area tax param added'}), 200


@area_bp.route('/v1/area/tax-param/update', methods=['POST'])
def update_area_tax_param():
    data = request.get_json()
    city_id = data.get('city_id')
    rate = data.get('rate')

    region = Region.query.filter_by(id=city_id).first()
    if not region:
        return jsonify({'error': 'Region does not exist'}), 400

    area_tax_param = AreaTaxParam.query.filter_by(city_id=city_id).first()
    if not area_tax_param:
        return jsonify({'error': 'Area tax param does not exist'}), 400

    area_tax_param.rate = rate
    db.session.commit()

    return jsonify({'message': 'Area tax param updated'}), 200


@area_bp.route('/v1/area/tax-param/delete', methods=['POST'])
def delete_area_tax_param():
    data = request.get_json()
    city_id = data.get('city_id')

    region = Region.query.filter_by(id=city_id).first()
    if not region:
        return jsonify({'error': 'Region does not exist'}), 400

    area_tax_param = AreaTaxParam.query.filter_by(city_id=city_id).first()
    if not area_tax_param:
        return jsonify({'error': 'Area tax param does not exist'}), 400

    db.session.delete(area_tax_param)
    db.session.commit()

    return jsonify({'message': 'Area tax param deleted'}), 200


@area_bp.route('/v1/area/tax-param/get', methods=['GET'])
def get_area_tax_param():
    area_tax_param_id = request.args.get('area_tax_param_id')

    area_tax_param = AreaTaxParam.query.filter_by(city_id=area_tax_param_id).first()
    if not area_tax_param:
        return jsonify({'error': 'Area tax param does not exist'}), 404

    return jsonify({'area_tax_param': area_tax_param.serialize()}), 200


@area_bp.route('/v1/area/tax-param/get/all', methods=['GET'])
def get_all_area_tax_params():
    area_tax_params = AreaTaxParam.query.all()

    area_tax_params_data = [area_tax_param.serialize() for area_tax_param in area_tax_params]
    return jsonify({'area_tax_params': area_tax_params_data}), 200


@area_bp.route('/v1/area/tax/calc', methods=['GET'])
def calculate_area_tax():
    city_id = request.args.get('city_id')
    cadastral_value = request.args.get('cadastral_value')

    region = Region.query.filter_by(id=city_id).first()
    if not region:
        return jsonify({'error': 'Region does not exist'}), 400

    area_tax_param = AreaTaxParam.query.filter_by(city_id=city_id).first()
    if not area_tax_param:
        return jsonify({'error': 'Area tax param does not exist'}), 400

    tax_amount = int(cadastral_value) * int(area_tax_param.rate)

    return jsonify({'tax_amount': tax_amount}), 200
