from flask import request, jsonify, Blueprint

from tax_rates import tax_rates

update_app = Blueprint('update_app', __name__)


@update_app.route('/v1/update/tax', methods=['POST'])
def update_tax():
    data = request.json

    region_code = data.get('region_code')
    new_tax_rate = data.get('tax_rate')

    if region_code in tax_rates:
        tax_rates[region_code] = new_tax_rate
        return jsonify({'message': 'Налоговая ставка успешно обновлена'}), 200
    else:
        return jsonify({'error': 'Not Found'}), 404
