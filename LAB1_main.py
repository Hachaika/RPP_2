from flask import Flask, request, jsonify
import psycopg2 as pg

conn = pg.connect(user='postgres', password='admin', port='5432', database='LAB1')
cursor = conn.cursor()

cursor.execute("SELECT * from auto")
rows_currency_rates = cursor.fetchall()
print(rows_currency_rates)

app = Flask(__name__)


@app.route('/v1/add/region', methods=['POST'])
def add_region():
    if request.is_json:
        data = request.get_json()
        city_id = data.get('id')
        region_name = data.get('name')

        cursor.execute("SELECT * FROM region WHERE id = %s", (city_id,))
        existing_region = cursor.fetchone()

        if existing_region:
            return jsonify({'error': 'BAD REQUEST'}), 400

        cursor.execute("INSERT INTO region (id, name) VALUES (%s, %s)", (city_id, region_name))
        conn.commit()

        return jsonify({'message': 'Region added successfully'}), 201
    else:
        return jsonify({'error': 'BAD REQUEST'}), 400


@app.route('/v1/add/tax-param', methods=['POST'])
def add_tax_param():
    if request.is_json:
        data = request.get_json()
        city_id = data.get('city_id')
        from_hp_car = data.get('from_hp_car')
        to_hp_car = data.get('to_hp_car')
        from_production_year_car = data.get('from_production_year_car')
        to_production_year_car = data.get('to_production_year_car')
        rate = data.get('rate')

        cursor.execute(
            "SELECT * FROM tax_param WHERE city_id = %s AND from_hp_car = %s AND to_hp_car = %s AND "
            "from_production_year_car = %s AND to_production_year_car = %s",
            (city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car)
        )
        existing_tax_param = cursor.fetchone()

        if existing_tax_param:
            return jsonify({'error': 'BAD REQUEST'}), 400

        cursor.execute(
            "INSERT INTO tax_param (city_id, from_hp_car, to_hp_car, from_production_year_car, "
            "to_production_year_car, rate) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (city_id, from_hp_car, to_hp_car, from_production_year_car, to_production_year_car, rate)
        )
        conn.commit()

        return jsonify({'message': 'Tax parameter added successfully'}), 201
    else:
        return jsonify({'error': 'BAD REQUEST'}), 400


@app.route('/v1/add/auto', methods=['POST'])
def add_auto():
    if request.is_json:
        data = request.get_json()
        city_id = data.get('city_id')
        tax_id = data.get('tax_id')
        name_car = data.get('name_car')
        hp_car = data.get('hp_car')
        production_year_car = data.get('production_year_car')

        cursor.execute("SELECT * FROM region WHERE id = %s", (city_id,))
        existing_city = cursor.fetchone()

        if not existing_city:
            return jsonify({'error': 'BAD REQUEST'}), 400

        cursor.execute(
            "SELECT rate FROM tax_param WHERE city_id = %s AND from_hp_car <= %s AND to_hp_car >= %s AND from_production_year_car <= %s AND to_production_year_car >= %s",
            (existing_city[0], hp_car, hp_car, production_year_car, production_year_car)
        )
        tax_param = cursor.fetchone()

        if not tax_param:
            return jsonify({'error': 'BAD REQUEST'}), 400

        tax_rate = tax_param[0]
        auto_tax = hp_car * tax_rate

        cursor.execute(
            "INSERT INTO auto (city_id, name, tax_id, horse_power, production_year, tx) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (existing_city[0], name_car, tax_id, hp_car, production_year_car, auto_tax)
        )
        conn.commit()

        return jsonify({'message': 'Automobile added successfully', 'auto_tax': auto_tax}), 201
    else:
        return jsonify({'error': 'BAD REQUEST'}), 400

@app.route('/v1/auto', methods=['GET'])
def get_auto():
    auto_id = request.args.get('auto_id')

    if auto_id:
        cursor.execute("SELECT * FROM auto WHERE id = %s", (auto_id,))
        automobile = cursor.fetchone()

        if automobile:
            return jsonify({'automobile': {
                'id': automobile[0],
                'region_id': automobile[1],
                'name_car': automobile[3],
                'hp_car': automobile[4],
                'production_year_car': automobile[5],
                'auto_tax': automobile[6]
            }}), 200
        else:
            return jsonify({'error': 'BAD REQUEST'}), 400
    else:
        cursor.execute("SELECT * FROM auto")
        automobiles = cursor.fetchall()

        automobiles_list = []
        for automobile in automobiles:
            automobiles_list.append({
                'id': automobile[0],
                'region_id': automobile[1],
                'name_car': automobile[3],
                'hp_car': automobile[4],
                'production_year_car': automobile[5],
                'auto_tax': automobile[6]
            })

        return jsonify({'automobiles': automobiles_list}), 200


if __name__ == "__main__":
    app.run(debug=True)
