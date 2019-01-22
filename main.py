from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("data.db")

conn.execute("""CREATE TABLE IF NOT EXISTS Users (
                username text
                data text
                number int
            )""")


@app.route("/", methods=["GET"])
def home():
    return "Hewwo?"


@app.route("/add/", methods=["POST"])
def add_data():
    data_in = request.form
    connect = sqlite3.connect("data.db")

    print(data_in.get('username'))
    connect.execute("INSERT INTO Users (username, data, number) Values ({}, {}, {});".format(data_in.get('username'), data_in.get('data'), data_in.get('number')))
    return str(data_in)


@app.route("/look/", methods=["GET"])
def look():
    cursor = conn.execute("SELECT username, data, number from Users")
    for row in cursor:
        print("username: " + str(row[0]) + ", data: " + str(row[1]) + ", number: " + str(row[2]))

    return 0


def main():
    app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
