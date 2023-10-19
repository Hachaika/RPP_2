from app.routes.region_route import region_bp
from app.routes.car_route import car_bp
from app.routes.area_route import area_bp
from app import app

app.register_blueprint(region_bp)
app.register_blueprint(car_bp)
app.register_blueprint(area_bp)


if __name__ == '__main__':
    app.run(debug=True)