import os

class Config:
    SECRET_KEY = os.urandom(24)  # Используется для защиты сессий
    DEBUG = True  # Включение режима отладки
    MODEL_PATH = 'student_performance_model.pkl'  # Путь к модели
