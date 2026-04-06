from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def check_leap_year():
    try:
        year = int(request.form["year"])

        if year < 1:
            return render_template(
                "index.html",
                error="Please enter a valid positive year.",
                result=None
            )

        # Lógica de año bisiesto
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            result = f"{year} is a leap year 🟢"
        else:
            result = f"{year} is NOT a leap year 🔴"

        return render_template("index.html", result=result, error=None)

    except ValueError:
        return render_template(
            "index.html",
            error="Please enter a valid number.",
            result=None
        )

if __name__ == "__main__":
    app.run(debug=True)
