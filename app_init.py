from flask import Flask
from app.routes import main
from app.model import load_model
import os

def create_app():
    # Указываем путь к папке с шаблонами
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
    app.config.from_object('config.Config')

    app.register_blueprint(main)
    
    # Загружаем модель
    app.model = load_model(app.config['MODEL_PATH'])
    
    return app
