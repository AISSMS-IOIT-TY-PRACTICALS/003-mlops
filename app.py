from flask import Flask, request, jsonify, render_template_string
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = 'iris_model.pkl'
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    html = '''
    <form action="/predict" method="post">
        Sepal Length: <input type="number" step="0.1" name="sepal_length" required><br>
        Sepal Width: <input type="number" step="0.1" name="sepal_width" required><br>
        Petal Length: <input type="number" step="0.1" name="petal_length" required><br>
        Petal Width: <input type="number" step="0.1" name="petal_width" required><br>
        <input type="submit" value="Predict">
    </form>
    '''
    return render_template_string(html)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        return f'Predicted Iris Class: {int(prediction[0])}'
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)