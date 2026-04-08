from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    number_of_vowels = None

    if request.method == 'POST' and 'input_string' in request.form:
        # Get input string
        input_string = request.form.get('input_string')

        # Convert to lowercase
        input_string = input_string.lower()

        number_of_vowels = 0

        # Count vowels using loop
        for i in input_string:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                number_of_vowels += 1

    return render_template('index.html', number_of_vowels=number_of_vowels)


if __name__ == "__main__":
    app.run(debug=True)
