from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    bmi = None

    if request.method == "POST":
        if 'Weight' in request.form and 'Height' in request.form:
            try:
                # Get values and convert to float
                weight = float(request.form.get('Weight'))
                height = float(request.form.get('Height'))

                # BMI calculation
                bmi = round(weight / ((height / 100) ** 2), 2)

            except:
                bmi = "Invalid input"

    return render_template("index.html", bmi=bmi)


if __name__ == "__main__":
    app.run(debug=True)
