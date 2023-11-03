from flask import Blueprint, request, jsonify, render_template
from __init__ import db
from app.models import CarTaxParam, Region

car_2_bp = Blueprint('car_2', __name__)


@car_2_bp.route('/v1/car/tax-param/add', methods=['POST'])
def add_car_tax_param():
    data = request.json
    id = data.get('id')
    city_id = data.get('city_id')
    from_hp_car = data.get('from_hp_car')
    to_hp_car = data.get('to_hp_car')
    start_year = data.get('start_year')
    end_year = data.get('end_year')
    rate = data.get('rate')

    if not id or not city_id or not from_hp_car or not to_hp_car or not start_year or not end_year or not rate:
        return jsonify({'error': 'Missing data in the request'}), 400

    if not Region.query.filter_by(id=city_id).first():
        return jsonify({'error': 'Region does not exist'}), 400

    if CarTaxParam.query.filter_by(
        id=id,
        city_id=city_id,
        from_hp_car=from_hp_car,
        to_hp_car=to_hp_car,
        from_production_year_car=start_year,
        to_production_year_car=end_year
    ).first():
        return jsonify({'error': 'Car tax param already exists for this region and parameters'}), 400

    car_tax_param = CarTaxParam(
        id=id,
        city_id=city_id,
        from_hp_car=from_hp_car,
        to_hp_car=to_hp_car,
        from_production_year_car=start_year,
        to_production_year_car=end_year,
        rate=rate
    )

    db.session.add(car_tax_param)
    db.session.commit()

    return jsonify({'message': 'Car tax param added successfully'}), 200


@car_2_bp.route('/v1/car/tax-param/update', methods=['POST'])
def update_car_tax_param():
    data = request.json
    id = data.get('id')
    city_id = data.get('city_id')
    from_hp_car = data.get('from_hp_car')
    to_hp_car = data.get('to_hp_car')
    start_year = data.get('start_year')
    end_year = data.get('end_year')
    rate = data.get('rate')

    if not id or not city_id or not from_hp_car or not to_hp_car or not start_year or not end_year or not rate:
        return jsonify({'error': 'Missing data in the request'}), 400

    car_tax_param = CarTaxParam.query.get(id)
    if not car_tax_param:
        return jsonify({'error': 'Car tax param not found'}), 400

    if not Region.query.filter_by(id=city_id).first():
        return jsonify({'error': 'Region does not exist'}), 400

    car_tax_param.city_id = city_id
    car_tax_param.from_hp_car = from_hp_car
    car_tax_param.to_hp_car = to_hp_car
    car_tax_param.from_production_year_car = start_year
    car_tax_param.to_production_year_car = end_year
    car_tax_param.rate = rate

    db.session.commit()

    return jsonify({'message': 'Car tax param updated successfully'}), 200


@car_2_bp.route('/v1/car/tax-param/delete', methods=['POST'])
def delete_car_tax_param():
    id = request.json.get('id')

    if not id:
        return jsonify({'error': 'ID is required'}), 400

    car_tax_param = CarTaxParam.query.get(id)
    if not car_tax_param:
        return jsonify({'error': 'Car tax param not found'}), 400

    db.session.delete(car_tax_param)
    db.session.commit()

    return jsonify({'message': 'Car tax param deleted successfully'}), 200


@car_2_bp.route('/v1/car/tax-param/get/all', methods=['GET'])
def get_all_car_tax_params():
    car_tax_params = CarTaxParam.query.all()
    car_tax_params_list = [
        {
            'id': param.id,
            'city_id': param.city_id,
            'min_horsepower': param.from_hp_car,
            'max_horsepower': param.to_hp_car,
            'start_year': param.from_production_year_car,
            'end_year': param.to_production_year_car,
            'tax_rate': param.rate
        }
        for param in car_tax_params
    ]

    return jsonify(car_tax_params_list), 200


@car_2_bp.route('/web/car/tax-param/add', methods=['GET', 'POST'])
def add_car_tax_param_web():
    if request.method == 'POST':
        id = request.form.get('id')
        city_id = request.form.get('city_id')
        from_hp_car = request.form.get('from_hp_car')
        to_hp_car = request.form.get('to_hp_car')
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        rate = request.form.get('rate')

        if not id or not city_id or not from_hp_car or not to_hp_car or not start_year or not end_year or not rate:
            return render_template('tax-param-add.html', result='Missing data in the request')

        if CarTaxParam.query.filter_by(
            id=id,
            city_id=city_id,
            from_hp_car=from_hp_car,
            to_hp_car=to_hp_car,
            from_production_year_car=start_year,
            to_production_year_car=end_year
        ).first():
            return render_template('tax-param-add.html', result='Car tax param already exists for this region and '
                                                                'parameters')

        car_tax_param = CarTaxParam(
            id=id,
            city_id=city_id,
            from_hp_car=from_hp_car,
            to_hp_car=to_hp_car,
            from_production_year_car=start_year,
            to_production_year_car=end_year,
            rate=rate
        )

        db.session.add(car_tax_param)
        db.session.commit()

        return render_template('tax-param-add.html', result='Car tax param added successfully')

    return render_template('tax-param-add.html', result=None)


@car_2_bp.route('/web/car/tax-param/update', methods=['GET', 'POST'])
def update_car_tax_param_web():
    if request.method == 'POST':
        id = request.form.get('id')
        city_id = request.form.get('city_id')
        from_hp_car = request.form.get('from_hp_car')
        to_hp_car = request.form.get('to_hp_car')
        start_year = request.form.get('start_year')
        end_year = request.form.get('end_year')
        rate = request.form.get('rate')

        if not id or not city_id or not from_hp_car or not to_hp_car or not start_year or not end_year or not rate:
            return render_template('tax-param-update.html', result='Missing data in the request')

        car_tax_param = CarTaxParam.query.get(id)
        if not car_tax_param:
            return render_template('tax-param-update.html', result='Car tax param not found')

        if not Region.query.filter_by(id=city_id).first():
            return render_template('tax-param-update.html', result='Region does not exist')

        car_tax_param.city_id = city_id
        car_tax_param.from_hp_car = from_hp_car
        car_tax_param.to_hp_car = to_hp_car
        car_tax_param.from_production_year_car = start_year
        car_tax_param.to_production_year_car = end_year
        car_tax_param.rate = rate

        db.session.commit()

        return render_template('tax-param-update.html', result='Car tax param updated successfully')

    return render_template('tax-param-update.html', result=None)


@car_2_bp.route('/web/car/tax-param/delete', methods=['GET', 'POST'])
def delete_car_tax_param_web():
    if request.method == 'POST':
        id = request.form.get('id')

        if not id:
            return render_template('tax-param-delete.html', result='ID is required')

        car_tax_param = CarTaxParam.query.get(id)
        if not car_tax_param:
            return render_template('tax-param-delete.html', result='Car tax param not found')

        db.session.delete(car_tax_param)
        db.session.commit()

        return render_template('tax-param-delete.html', result='Car tax param deleted successfully')

    return render_template('tax-param-delete.html', result=None)


@car_2_bp.route('/web/car/tax-param/get/all', methods=['GET'])
def get_all_car_tax_params_web():
    car_tax_params = CarTaxParam.query.all()
    car_tax_params_list = [
        {
            'id': param.id,
            'city_id': param.city_id,
            'min_horsepower': param.from_hp_car,
            'max_horsepower': param.to_hp_car,
            'start_year': param.from_production_year_car,
            'end_year': param.to_production_year_car,
            'tax_rate': param.rate
        }
        for param in car_tax_params
    ]

    return render_template('tax-param-list.html', car_tax_params=car_tax_params_list)
