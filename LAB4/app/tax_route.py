from flask import Blueprint, request, jsonify, render_template
from __init__ import db
from app.models import CarTaxParam, Region

car_bp = Blueprint('car', __name__)


@car_bp.route('/v1/car/tax/calc', methods=['GET', 'POST'])
def calculate_car_tax():
    city_id = request.form.get('city_id')
    horsepower = request.form.get('horsepower')
    year = request.form.get('year')

    if not city_id or not horsepower or not year:
        return render_template('index.html', result={'error': 'Missing data in the request'}), 400

    car_tax_param = CarTaxParam.query.filter(
        CarTaxParam.city_id == city_id,
        CarTaxParam.from_hp_car <= horsepower,
        CarTaxParam.from_production_year_car <= year,
        CarTaxParam.to_production_year_car >= year
    ).first()

    if not car_tax_param:
        return render_template('index.html', result={'error': 'No applicable car tax param found'}), 400

    tax = int(car_tax_param.rate) * int(horsepower)
    return render_template('index.html', result=f'Налог: {tax}')


@car_bp.route('/')
def index():
    return render_template('index.html')