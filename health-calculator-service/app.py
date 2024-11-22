from flask import Flask, request, render_template, jsonify # type: ignore
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

# Page d'accueil avec message de bienvenue
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route pour calculer le BMI
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        result = calculate_bmi(height, weight)
        return render_template('result.html', result=result, calculation_type="BMI")
    return render_template('bmi_form.html')

# Route pour calculer le BMR
@app.route('/bmr', methods=['GET', 'POST'])
def bmr():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        age = int(request.form['age'])
        gender = request.form['gender']
        result = calculate_bmr(height, weight, age, gender)
        return render_template('result.html', result=result, calculation_type="BMR")
    return render_template('bmr_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
