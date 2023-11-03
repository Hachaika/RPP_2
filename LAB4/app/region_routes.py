from flask import Blueprint, request, jsonify, render_template
from __init__ import db
from app.models import Region
import jinja2

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


@region_bp.route('/web/region', methods=['GET'])
def get_region_web():
    regions = Region.query.all()
    return render_template('region-list.html', regions=regions)


@region_bp.route('/web/region/add', methods=['GET', 'POST'])
def add_region_web():
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')

        if not name:
            return render_template('region-add.html', result='Name is required')

        if not number:
            return render_template('region-add.html', result='Number is required')

        region = Region.query.filter_by(name=name).first()
        if region:
            return render_template('region-add.html', result='Region with this name already exists')

        region_2 = Region.query.filter_by(id=number).first()
        if region_2:
            return render_template('region-add.html', result='Region with this number already exists')

        region = Region(id=number, name=name)
        db.session.add(region)
        db.session.commit()

        return render_template('region-add.html', result='Region added successfully')

    return render_template('region-add.html', result=None)


@region_bp.route('/web/region/update', methods=['GET', 'POST'])
def update_region_web():
    if request.method == 'POST':
        id = request.form.get('id')
        new_id = request.form.get('new_id')

        if not id or not new_id:
            return render_template('region-update.html', result='ID and new_id are required')

        region = Region.query.get(id)
        if not region:
            return render_template('region-update.html', result='Region not found')

        region.id = new_id
        db.session.commit()

        return render_template('region-update.html', result='Region updated successfully')

    return render_template('region-update.html', result=None)


@region_bp.route('/web/region/delete', methods=['GET', 'POST'])
def delete_region_web():
    if request.method == 'POST':
        id = request.form.get('id')

        if not id:
            return render_template('region-delete.html', result='ID is required')

        region = Region.query.get(id)
        if not region:
            return render_template('region-delete.html', result='Region not found')

        db.session.delete(region)
        db.session.commit()

        return render_template('region-delete.html', result='Region deleted successfully')

    return render_template('region-delete.html', result=None)
