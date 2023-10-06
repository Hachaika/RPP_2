from flask import Flask, request, jsonify

app = Flask(__name__)

tax_rates = {}


@app.route('/v1/add/tax', methods=['POST'])
def add_tax():
    data = request.json

    region_code = data.get('region_code')
    if region_code in tax_rates:
        return jsonify({'error': 'I’m a teapot '}), 418

    tax_rate = data.get('tax_rate')
    tax_rates[region_code] = tax_rate

    return jsonify({'message': 'Налоговая ставка успешно добавлена'}), 201


@app.route('/v1/fetch/taxes', methods=['GET'])
def fetch_taxes():
    return jsonify(tax_rates)


@app.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    region_code = request.args.get('region_code')
    if region_code not in tax_rates:
        return jsonify({'error': 'Not Found'}), 404

    return jsonify({'region_code': region_code, 'tax_rate': tax_rates[region_code]})


@app.route('/v1/fetch/calc', methods=['GET'])
def calculate_tax():
    region_code = request.args.get('region_code')
    if region_code not in tax_rates:
        return jsonify({'error': 'Регион с этим кодом не найден'}), 400

    cadastre_value = float(request.args.get('cadastre_value'))
    months_owned = int(request.args.get('months_owned'))
    annual_tax = (cadastre_value * tax_rates[region_code] * months_owned) / 12

    return jsonify({'region_code': region_code, 'annual_tax': annual_tax})


@app.route('/v1/update/tax', methods=['POST'])
def update_tax():
    data = request.json

    region_code = data.get('region_code')
    new_tax_rate = data.get('tax_rate')

    if region_code in tax_rates:
        tax_rates[region_code] = new_tax_rate
        return jsonify({'message': 'Налоговая ставка успешно обновлена'}), 200
    else:
        return jsonify({'error': 'Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
