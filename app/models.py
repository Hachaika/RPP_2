from app import db


class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class CarTaxParam(db.Model):
    __tablename__ = 'car_tax_param'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Numeric, nullable=False)


class AreaTaxParam(db.Model):
    __tablename__ = 'area_tax_param'

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    rate = db.Column(db.Numeric, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'city_id': self.city_id,
            'rate': int(self.rate)
        }
