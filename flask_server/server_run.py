from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_area', methods=['GET'])
def get_area_names():
    response = jsonify({
        'area': util.get_area_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    bds = int(request.form['bds'])
    ba = int(request.form['ba'])
    area = request.form['area']

    response = jsonify({
        'estimated_price': util.get_estimated_price(area, bds, ba, sqft)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run()
