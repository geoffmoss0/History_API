from flask import Flask, jsonify, request
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
