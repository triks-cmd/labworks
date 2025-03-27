from flask import Blueprint, render_template, request, current_app
from app.feedback import get_feedback
import numpy as np

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    error_message = None
    
    if request.method == "POST":
        try:
            grade = float(request.form["grade"])
            attendance = float(request.form["attendance"])
            assignment_rate = float(request.form["assignment_rate"])
            
            input_data = [[grade, attendance, assignment_rate]]
            performance_label = current_app.model.predict(input_data)[0]
            feedback = get_feedback(performance_label, grade, attendance, assignment_rate)
        except Exception as e:
            error_message = "Ошибка при обработке данных: " + str(e)
    
    return render_template("index.html", feedback=feedback, error_message=error_message)
