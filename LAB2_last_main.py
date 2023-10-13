from flask import Flask
from add_route import add_app
from fetch_route import fetch_app
from update_route import update_app

app = Flask(__name__)

app.register_blueprint(add_app)
app.register_blueprint(fetch_app)
app.register_blueprint(update_app)

if __name__ == '__main__':
    app.run(debug=True)