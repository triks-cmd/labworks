from app.app_init import create_app  # Импортируем из app_init.py

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
