from flask import Flask, request, render_template, jsonify
import joblib


app = Flask(__name__)

# Load models and encoders
rf_exercises = joblib.load('rf_exercises_model.pkl')
rf_diet = joblib.load('rf_diet_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        user_features = [
            int(request.form['Sex']),
            int(request.form['Age']),
            float(request.form['Height']),
            float(request.form['Weight']),
            float(request.form['BMI']),
            int(request.form['Hypertension']),
            int(request.form['Diabetes']),
            int(request.form['Level']),
            int(request.form['Fitness Goal']),
            int(request.form['Fitness Type'])
        ]

        # Predict Exercise
        exercise_prediction = rf_exercises.predict([user_features])[0]
        # Predict Diet
        diet_prediction = rf_diet.predict([user_features])[0]

        # Decode predictions with error handling
        exercise_result = label_encoders['Exercises'].inverse_transform([exercise_prediction])[0]
        diet_result = label_encoders['Diet'].inverse_transform([diet_prediction])[0]

        return render_template('result.html', exercise=exercise_result, diet=diet_result)
    except KeyError as ke:
        return render_template('error.html', error=f"Missing key: {ke}")
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)
