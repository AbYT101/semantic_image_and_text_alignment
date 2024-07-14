from flask import Flask
from config import Config
from routes import compose, evaluate, synthesis_storyboard, index

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(index.bp)
    app.register_blueprint(compose.bp)
    app.register_blueprint(evaluate.bp)
    app.register_blueprint(synthesis_storyboard.bp)

    return app
