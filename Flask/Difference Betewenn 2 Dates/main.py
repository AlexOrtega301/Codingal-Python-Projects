from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", result=None, error=None)

@app.route("/calculate", methods=["POST"])
def calculate_difference():
    date1_str = request.form.get("date1")
    date2_str = request.form.get("date2")

    if not date1_str or not date2_str:
        return render_template("index.html", result=None, error="Please enter both dates.")

    try:
        date1 = datetime.strptime(date1_str, "%Y-%m-%d")
        date2 = datetime.strptime(date2_str, "%Y-%m-%d")

        # Asegurar orden correcto
        if date1 > date2:
            date1, date2 = date2, date1

        delta = date2 - date1
        days = delta.days

        # Aproximaciones para meses y años
        years = days // 365
        months = days // 30

        result = {
            "days": days,
            "months": months,
            "years": years
        }

        return render_template("index.html", result=result, error=None)

    except ValueError:
        return render_template("index.html", result=None, error="Invalid date format.")

if __name__ == "__main__":
    app.run(debug=True)
