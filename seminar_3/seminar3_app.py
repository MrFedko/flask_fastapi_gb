from flask import Flask, render_template
import os
from config import Config
from models import db, Student, Faq, GenderEnum, Author, Book, Estimate
from random import choice

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

category = [
    {"title": 'Home page', "func_name": 'index'},
    {"title": 'All students', "func_name": 'get_all'},
    {"title": 'All books', "func_name": 'get_all_books'},
    {"title": 'All estimates', "func_name": 'get_all_est'}
]


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', category=category)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-students")
def fill_tables():
    count = 5
    # Добавляем факультеты
    for faq in range(1, count + 1):
        new_faq = Faq(title=f'faq{faq}')
        db.session.add(new_faq)
    db.session.commit()
    # Добавляем студентов
    for student in range(1, count ** 2):
        faq = choice(range(1, 6))
        new_student = Student(name=f'Student{student}', surname=f'surname{student}', age=choice(range(18, 100)),
                              gender=choice([GenderEnum.MALE, GenderEnum.FEMALE]), group=choice(range(10, 15)),
                              faq=faq)
        db.session.add(new_student)
    db.session.commit()


@app.route('/all_students/')
def get_all():
    students = Student.query.all()
    context = {'students': students}
    return render_template('all_stud.html', **context)


@app.cli.command("fill-books")
def fill_tables():
    count = 5
    # Добавляем авторов
    for author in range(1, count + 1):
        new_author = Author(name=f'Author{author}', surname=f'Surname{author}')
        db.session.add(new_author)
    db.session.commit()
    # Добавляем книги
    for book in range(1, count ** 2):
        author = choice(range(1, 6))
        new_book = Book(title=f'Title{book}', year=choice(range(1990, 2024)), count=choice(range(1, 999999)),
                        author=author)
        db.session.add(new_book)
    db.session.commit()


@app.route('/all_books/')
def get_all_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('all_books.html', **context)


@app.cli.command("fill-estimates")
def fill_tables():
    count = 5
    for _ in range(1, count ** 4):
        student_id = choice([stud.id for stud in Student.query.all()])
        faculty = choice([faq.title for faq in Faq.query.all()])
        value = choice(range(1, 101))
        new_estimate = Estimate(student_id=student_id, faculty=faculty, value=value)
        db.session.add(new_estimate)
    db.session.commit()


@app.route('/estimates/')
def get_all_est():
    students = Student.query.all()
    return render_template('all_estimates.html', students=students)


if __name__ == '__main__':
    app.run()
