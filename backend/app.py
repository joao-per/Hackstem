from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def hello_world():
    data = {
        'name': 'John Doe',
        'age': 25,
        'city': 'Example City'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
