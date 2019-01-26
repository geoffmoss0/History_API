from flask import Flask, jsonify, request
import sqlite3
from sqlite3 import Error
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Table
from sqlalchemy.orm import sessionmaker, query

app = Flask(__name__)

engine = create_engine("sqlite:///data.db", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    name = Column(String, primary_key=True)
    data = Column(String)
    number = Column(Integer)

    def __repr__(self):
        return "<User(name='{}', data='{}', number={})>".format(self.name, self.data, self.number)

    def __init__(self, name, data, number):
        self.name = name
        self.data = data
        self.number = number


def create_conn():
    try:
        conn = sqlite3.connect("data.db")
        return conn
    except Error as e:
        print(e)
    return None


@app.route("/add/", methods=["POST"])
def add_data():
    data_in = request.form
    print(request.form)
    conn = create_conn()
    c = conn.cursor()

    print(data_in.get('username'))
    c.execute('INSERT INTO Users(username, data, number) Values ("{}", "{}", {});'.format(data_in.get('username'), data_in.get('data'), data_in.get('number')))
    return str(data_in)


@app.route("/look/", methods=["GET"])
def look():
    conn = create_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    rows = c.fetchall()
    print(len(rows))
    for row in rows:
        # out.append("username: " + str(row[0]) + ", data: " + str(row[1]) + ", number: " + str(row[2]))
        print(row)

    return "At least it'll say something"


def main():
    Base.metadata.create_all(engine)
    user = User(name="geo", data="nothing important really", number=0)
    Session = sessionmaker(bind=engine)
    session = sessionmaker()
    session.configure(bind=engine)
    sesh = Session()
    sesh.add(user)
    get = sesh.query(User).first()
    print(get)
    # app.run(host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()
