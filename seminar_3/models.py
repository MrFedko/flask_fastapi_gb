from flask_sqlalchemy import SQLAlchemy
import enum


db = SQLAlchemy()


class GenderEnum(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.Enum(GenderEnum))
    group = db.Column(db.Integer)
    faq = db.Column(db.Integer, db.ForeignKey('faq.id'))

    def __repr__(self):
        return f'Student ({self.name})'


class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty ({self.title})'


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer)
    author = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return f'Book ({self.title})'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', backref='author_name', lazy=True)

    def __repr__(self):
        return f'Author ({self.name} {self.surname})'
