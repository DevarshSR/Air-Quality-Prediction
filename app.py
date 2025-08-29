from flask import Flask, render_template, request, jsonify
import pickle,joblib
import numpy as np

# Load model
model = joblib.load(open('air_quality_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({'message': 'Use POST to submit data for prediction.'})
    try:
        data = request.get_json(force=True)
        # Get values in the order expected by the model
        PM25 = float(data['PM25'])
        PM10 = float(data['PM10'])
        NOx = float(data['NOx'])
        CO = float(data['CO'])
        SO2 = float(data['SO2'])
        user_input = np.array([[PM25, PM10, NOx, CO, SO2]])
        prediction = model.predict(user_input)
        return jsonify({'predicted_AQI': f'{prediction[0]:.2f}'})
    except Exception as e:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)