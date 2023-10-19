from flask import Blueprint

region_bp = Blueprint('region', __name__)
car_bp = Blueprint('car', __name__)
area_bp = Blueprint('area', __name__)

from . import region_route, car_route, area_route

