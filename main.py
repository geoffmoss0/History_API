from flask import Flask, request
from flaskext.mysql import MySQL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import ArgumentError, IntegrityError
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tits123'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'history'
mysql.init_app(app)


engine = create_engine("mysql://root:tits123@localhost/history", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    name = Column(String(60), primary_key=True)
    data = Column(String(60))
    number = Column(Integer)

    def __repr__(self):
        return "<User(name='{}', data='{}', number={})>".format(self.name, self.data, self.number)

    def __init__(self, name, data, number):
        self.name = name
        self.data = data
        self.number = number


@app.route('/add', methods=['POST'])
def add():
    print("got here")
    name = request.form['username']
    data = request.form['data']
    number = request.form['number']
    user = User(name=name, data=data, number=number)
    session = get_session()
    session.add(user)
    try:
        session.commit()
    except ArgumentError as e:
        return str(e)
    except IntegrityError as e:
        return str(e)
    print(name)
    return name


def main():
    app.run(host="127.0.0.1", port=5000)
    Base.metadata.create_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    session = sessionmaker()
    session.configure(bind=engine)
    sesh = Session()
    return sesh


if __name__ == "__main__":
    main()
