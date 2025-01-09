from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        # Validate input
        if height <= 0 or weight <= 0:
            return render_template('error.html', message="Wzrost i waga muszą być większe od 0", back_url=url_for('index'))

        bmi = weight / (height / 100) ** 2
        bmi_category = ''
        require_email = False
        if bmi < 18.5:
            bmi_category = 'Niedowaga'
        elif 18.5 <= bmi < 24.9:
            bmi_category = 'W normie'
        elif 25 <= bmi < 29.9:
            bmi_category = 'Nadwaga'
            require_email = True
        else:
            bmi_category = 'Otyłość'
            require_email = True

        if require_email:
            return render_template('contact.html', first_name=first_name, last_name=last_name, bmi=bmi, bmi_category=bmi_category, message="Mail do kontaktu z dietetykiem")

        return render_template('result.html', first_name=first_name, last_name=last_name, bmi=bmi, bmi_category=bmi_category)

    except ValueError:
        return render_template('error.html', message="Wprowadzone dane muszą być liczbami.", back_url=url_for('index'))

@app.route('/email-sent', methods=['POST'])
def email_sent():
    email = request.form['email']
    return render_template('email_sent.html', message="Mail wysłany. Zapraszamy do ponownych obliczeń!", back_url=url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)