from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    bmi_result = None
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birth_date = request.form.get('birth_date')
        email = request.form.get('email')
        height = request.form.get('height')
        weight = request.form.get('weight')

        if '@' not in email:
            return render_template('form.html', error="Nieprawidłowy adres email!")

        try:
            height = float(height)
            weight = float(weight)
            bmi_result = round(weight / (height / 100) ** 2, 2)
        except ValueError:
            return render_template('form.html', error="Wzrost i waga muszą być liczbami!")

    return render_template('form.html', bmi_result=bmi_result)

if __name__ == '__main__':
    app.run(debug=True)
