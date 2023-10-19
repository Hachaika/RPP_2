from flask import Flask, request, jsonify, Blueprint
from tax_rates import tax_rates

add_app = Blueprint('add_app', __name__)



@add_app.route('/v1/add/tax', methods=['POST'])
def add_tax():
    data = request.json

    region_code = data.get('region_code')
    if region_code in tax_rates:
        return jsonify({'error': 'I’m a teapot '}), 418

    tax_rate = data.get('tax_rate')
    tax_rates[region_code] = tax_rate

    return jsonify({'message': 'Налоговая ставка успешно добавлена'}), 201