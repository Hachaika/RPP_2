from flask import Flask, request, jsonify, Blueprint
from tax_rates import tax_rates

fetch_app = Blueprint('fetch_app', __name__)



@fetch_app.route('/v1/fetch/taxes', methods=['GET'])
def fetch_taxes():
    return jsonify(tax_rates)


@fetch_app.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    region_code = request.args.get('region_code')
    if region_code not in tax_rates:
        return jsonify({'error': 'Not Found'}), 404

    return jsonify({'region_code': region_code, 'tax_rate': tax_rates[region_code]})


@fetch_app.route('/v1/fetch/calc', methods=['GET'])
def calculate_tax():
    region_code = request.args.get('region_code')
    if region_code not in tax_rates:
        return jsonify({'error': 'Регион с этим кодом не найден'}), 400

    cadastre_value = float(request.args.get('cadastre_value'))
    months_owned = int(request.args.get('months_owned'))
    annual_tax = (cadastre_value * tax_rates[region_code] * months_owned) / 12

    return jsonify({'region_code': region_code, 'annual_tax': annual_tax})