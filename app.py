from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmi')
def bmi():
    return "Strona kalkulatora BMI"

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    if height <= 0 or weight <= 0:
        return "Nieprawidłowe dane. Wzrost i waga muszą być większe niż zero."
    bmi = weight / (height / 100) ** 2
    return f"Twoje BMI wynosi {bmi:.2f}"

@app.route('/calculate', methods=['POST'])
def calculate():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    height = float(request.form['height'])
    weight = float(request.form['weight'])

    bmi = weight / (height / 100) ** 2
    bmi_category = ''
    if bmi < 18.5:
        bmi_category = 'Niedowaga'
    elif 18.5 <= bmi < 24.9:
        bmi_category = 'W normie'
    elif 25 <= bmi < 29.9:
        bmi_category = 'Nadwaga'
    else:
        bmi_category = 'Otyłość'

    return render_template('result.html', first_name=first_name, last_name=last_name, bmi=bmi, bmi_category=bmi_category)

if __name__ == '__main__':
    app.run(debug=True)
