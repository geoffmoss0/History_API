from flask import Flask, jsonify, request

app = Flask(__name__)

data = []


@app.route("/", methods=["GET"])
def home():
    return "Hewwo?"


@app.route("/add/", methods=["POST"])
def add_data():
    data_in = request.form

    data.append(data_in)


@app.route("/look/", methods=["GET"])
def look():
    return str(data)


def main():
    app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
