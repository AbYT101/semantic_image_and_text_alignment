from flask import Flask
from config import Config
from routes import compose, evaluate, synthesis_storyboard, index
from flask_cors import CORS  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(compose.bp)
    app.register_blueprint(evaluate.bp)
    app.register_blueprint(synthesis_storyboard.bp)

    return app
