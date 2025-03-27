import pickle
import config  # Правильный импорт

def load_model(model_path):
    """
    Загружает модель из файла
    """
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model
