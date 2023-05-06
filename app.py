from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import numpy as np

dataset = load_iris()
X = dataset.data[:, :2]
y = dataset.target

log_reg = LogisticRegression(random_state=0).fit(X, y)


app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
     sepal_length = float(request.args.get('sepal_length'))
     sepal_width = float(request.args.get('sepal_width'))


     X_args = np.array([[sepal_length, sepal_width]])
     y_prediction = log_reg.predict(X_args)[0]

     prediction_actual_name = dataset.target_names[y_prediction]


     response = {
             'species' : prediction_actual_name
             }
     return jsonify(response)


if __name__ == "__main__":
    app.run()
