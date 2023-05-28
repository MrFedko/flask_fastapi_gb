# Семинар 1. Знакомство с Flask


[link for app](/seminar_1/app_1.py)
## Задание №1
 - Напишите простое веб-приложение на Flask, которое будет
выводить на экран текст "Hello, World!".

```python
@app.route('/')
def hello_world():
    return 'Hello World!'
```

   

## Задание №2
Дорабатываем задачу 1.
Добавьте две дополнительные страницы в ваше вебприложение:
- страницу "about"
- страницу "contact".

```python
@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'

```


## Задание №3
Написать функцию, которая будет принимать на вход два
числа и выводить на экран их сумму.

```python
@app.route('/<int:a>/<int:b>')
def summa(a, b):
    return str(a + b)
```

## Задание №4
Написать функцию, которая будет принимать на вход строку и
выводить на экран ее длину.


```python
@app.route('/<string:text>/')
def string(text):
    return str(len(text))
```

## Задание №5
Написать функцию, которая будет выводить на экран HTML
страницу с заголовком "Моя первая HTML страница" и
абзацем "Привет, мир!".

```python
@app.route('/index/')
def index():
    return render_template('base.html')
```

## Задание №6
[link for app](/seminar_1/app_stud.py)

Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: 
- "Имя"
- "Фамилия" 
- "Возраст" 
- "Средний балл"

Данные о студентах должны быть переданы в шаблон через
контекст.

```python
@app.route('/')
def students():
    return render_template('students.html', stud=stud)
```
```html
    <table>
    <tr>
        <th>Name</th>
        <th>Surname</th>
        <th>Age</th>
        <th>AVG score</th>
    </tr>
    {% for person in stud %}
        <tr>
            <td>{{person.name}}</td>
            <td>{{person.surname}}</td>
            <td>{{person.age}}</td>
            <td>{{person.avg_score}}</td>
        </tr>
    {% endfor %}
    </table>
```

## Задание №7
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.

Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.

Данные о новостях должны быть переданы в шаблон через
контекст.

```python
@app.route('/news/')
def news_page():
    return render_template('news.html', news=news)
```

```html
    {% for art in news %}
        <h2>{{ art.title }}</h2>
        <h5>{{ art.date }}</h5>
        <p>{{ art.text }}</p>
    {% endfor %}
```

## Задание №8

[link for app](/seminar_1/app_store.py)

Создать [базовый шаблон](/seminar_1/templates/store.html) для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.

Например, создать страницу ["О нас"](/seminar_1/templates/store_info.html) и ["Контакты"](/seminar_1/templates/store_contacts.html),
используя базовый шаблон.

## Задание №9
Создать [базовый шаблон](/seminar_1/templates/store.html) для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
```html
    <h2>Select category:</h2>
    <ul>
        {% for cat in category %}
        <li>
            <a href="{{ url_for(cat.func_name) }}">{{ cat.title }}</a>
        </li>
        {% endfor %}
    </ul>
```

Например, создать страницы ["Одежда"](/seminar_1/templates/store_dress.html), ["Обувь"](/seminar_1/templates/store_shoes.html) и ["Игрушки"](/seminar_1/templates/store_toys.html),
используя базовый шаблон.

```python
category = [
    {"title": 'Одежда', "func_name": 'dress'},
    {"title": 'Обувь', "func_name": 'shoes'},
    {"title": 'Игрушки', "func_name": 'toys'}
]

@app.route('/')
@app.route('/index/')
def index():
    return render_template('store_index.html', category=category)

@app.route('/dress/')
def dress():
    return render_template('store_dress.html')


@app.route('/shoes/')
def shoes():
    return render_template('store_shoes.html')


@app.route('/toys/')
def toys():
    return render_template('store_toys.html')
```


# Семинар 2. Погружение во Flask.
[link for folder](/seminar_2)

## Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.

```python
@app.route('/button/', methods=['GET', 'POST'])
def button():
    if request.method == 'POST':
        return 'Hello Bob'
    return render_template('button.html')
```
```html
    <form method="post">
        <input type="submit" value="Press button">
    </form>
```

## Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.

```python
@app.route('/image/')
def image():
    return render_template('image.html')


@app.get('/upload/')
def image_get():
    return render_template('upload.html')


@app.post('/upload/')
def image_post():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
    return f"Файл {file_name} загружен на сервер"
```

```html
<img src="/static/img.png" width="300px">
<a href="/upload"> upload image </a>
```
```html
  <h1>Загружаем новый файл на сервер</h1>
  <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Загрузить>
  </form>
```

## Задание №3
Создать страницу, на которой будет форма для ввода логина
и пароля

При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.

```python
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and password == info[username]:
            return f"Hello {username}"
        else:
            return render_template('login.html')
    return render_template('login.html')
```

```html
<form method="post">
    <input type="text" name="username" placeholder="Имя">
    <input type="password" name="password" placeholder="Пароль">
    <input type="submit" value="Отправить">
</form>
```

## Задание №4
Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить".

При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.

```python
@app.route('/send_text/', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        text = escape(request.form.get('text'))
        return f"количество слов {len(text.split(' '))}"
    return render_template("text.html")
```

```html
<form method="post">
    <input type="text" name="text" placeholder="Имя">
    <input type="submit" value="Отправить">
</form>
```

## Задание №5
Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"

При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.

```python
@app.route('/calculate/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        first = float(request.form.get('firstnum'))
        second = float(request.form.get('secondnum'))
        operation = request.form.get('operation')
        res = 0
        match operation:
            case "+":
                res = first + second
            case "-":
                res = first - second
            case "/":
                res = first / second
            case "*":
                res = first * second
        return f"{first} {operation} {second} = {res}"
    return render_template('calculate.html')
```

```html
    <form method="post">
        <input type="number" name="firstnum" placeholder="первое число" required>
        <input type="number" name="secondnum" placeholder="второе число" required>
        <fieldset>
            <legend>Select operation</legend>
            <div>
              <input type="radio" id="sum" name="operation" value="+">
              <label for="sum"> + Сложить</label>
            </div>

            <div>
              <input type="radio" id="sub" name="operation" value="-">
              <label for="sub">- Вычесть</label>
            </div>

            <div>
              <input type="radio" id="mul" name="operation" value="*">
              <label for="mul">* Умножить</label>
            </div>

            <div>
              <input type="radio" id="div" name="divoperation" value="/">
              <label for="div">/ Разделить</label>
            </div>
        </fieldset>
        <input type="submit" value="Посчитать">
    </form>
```

## Задание №6
Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"

При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.


```python
@app.route('/check_age/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        age = int(request.form.get('age'))
        if age >= 18:
            return "Можно"
        return "Нельзя"
    return render_template('check_age.html')
```

```html
    <form method="post">
        <input type="text" name="name" placeholder="Имя">
        <input type="number" name="age" placeholder="Возраст">
        <input type="submit" value="Отправить">
    </form>
```

## Задание №7
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"

При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.

```python
@app.route('/square/', methods=['GET', 'POST'])
def square():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        data = {"number": number, "square": number ** 2}
        return render_template('square.html', data=data)
    return render_template('square.html')
```

```html
    {% if data %}
        <p>{{data.number}} ** 2 = {{data.square}}</p>
    {% else %}
    <form method="post">
        <input type="number" name="number" placeholder="Введитея число">
        <input type="submit" value="Отправить">
    </form>
    {% endif %}
```

## Задание №8
Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"

При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".

```python
app.secret_key = secrets.token_hex()

@app.route('/flas/', methods=['GET', 'POST'])
def flas():
    if request.method == 'POST':
        name = escape(request.form.get('name'))
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flas'))
    return render_template('flas.html')
```

```html
    <form action="/flas" method="post">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <input type="text" name="name" placeholder="Имя">
        <input type="submit" value="Отправить">
    </form>
```

## Задание №9
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя

Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

```python
@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
```

```html
    <form method="post">
        <input type="text" name="username" placeholder="Имя">
        <input type="email" name="email" placeholder="E-mail">
        <input type="submit" value="Отправить">
    </form>
```

И немного подправим стартовую страницу

```html
    {% if session.username %}
        <h1>Привет {{ session.username }}</h1>
        <a href="/logout">Log out</a>
    {% else %}
        <a href="/log">Login</a>
    {% endif %}
```


# Семинар 3. Дополнительные возможности Flask
[link for folder](seminar_3)

## Задание №1
- Создать базу данных для хранения информации о студентах университета.
- База данных должна содержать две таблицы: "Студенты" и "Факультеты".
- В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.
 ```python
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
```
- В таблице "Факультеты" должны быть следующие поля: id и название
факультета.
```python
class Faq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty', lazy=True)
    
    def __repr__(self):
        return f'Faculty ({self.title})'
```
- Необходимо создать связь между таблицами "Студенты" и "Факультеты".
- Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
```python
@app.route('/all_students/')
def get_all():
    students = Student.query.all()
    context = {'students': students}
    return render_template('all_stud.html', **context)
```
```html
{% block content %}
    <h1>List of students</h1>

    {% for student in students %}
        <li> {{ student.name }} - {{ student.faculty }} </li>
    {% endfor %}
{% endblock %}
```

## Задание №2
- Создать базу данных для хранения информации о книгах в библиотеке.
- База данных должна содержать две таблицы: "Книги" и "Авторы".
- В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
```python
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer)
    author = db.Column(db.Integer, db.ForeignKey('author.id'))
    
    def __repr__(self):
        return f'Book ({self.title})'
```
- В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    books = db.relationship('Book', backref='author_name', lazy=True)

    def __repr__(self):
        return f'Author ({self.name} {self.surname})'
```
- Необходимо создать связь между таблицами "Книги" и "Авторы".
- Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
```python
@app.route('/all_books/')
def get_all_books():
    books = Book.query.all()
    context = {'books': books}
    return render_template('all_books.html', **context)
```
```html
{% block content %}
    <h1>List of books</h1>

    {% for book in books %}
        <li> {{ book.title }} - {{ book.author_name }} </li>
    {% endfor %}
{% endblock %}
```

## Задание №3
Доработаем задача про студентов
- Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
- База данных должна содержать две таблицы: "Студенты" и "Оценки".
- В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
- В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
```python
class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship('Student', backref='estimates', lazy=True)
    faculty = db.Column(db.String, db.ForeignKey('faq.title'))
    faq = db.relationship('Faq', backref='estimates', lazy=True)
    value = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.value}'
```
- Необходимо создать связь между таблицами "Студенты" и "Оценки".
- Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
```python
@app.route('/estimates/')
def get_all_est():
    students = Student.query.all()
    return render_template('all_estimates.html', students=students)
```
```html
{% block content %}
    <h1>List of estimates</h1>

    {% for student in students %}
        <li> {{ student.name }} - {{ student.estimates }} </li>
    {% endfor %}
{% endblock %}
```

## Задание №4
- Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
  - Имя пользователя (обязательное поле)
  - Электронная почта (обязательное поле, с валидацией на корректность ввода email)
  - Пароль (обязательное поле, с валидацией на минимальную длину пароля)
  - Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
  ```python
  class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
  ```
- После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
заполнено или данные не прошли валидацию, то должно выводиться соответствующее
сообщение об ошибке.
- Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
об ошибке.
```python
@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = form.username.data.lower()
        email = form.email.data
        user = User(username=username, email=email)
        if User.query.filter(User.username == username).first() or User.query.filter(User.email == email).first():
            flash(f'Пользователь с username {username} или e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration'))
    return render_template('registration.html', form=form)
```

```html
{% block content %}
    <h1>Registration page</h1>
    <form method="POST" action="{{ url_for('registration') }}">
        {{ form.csrf_token }}
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>
            {{ form.confirm_password.label }}<br>
            {{ form.confirm_password(size=32) }}
        </p>
        <p>
        <input type="submit" value="Login">
        </p>
    </form>
{% endblock %}

```

## Задание №5
Создать форму регистрации для пользователя.
- Форма должна содержать поля: имя, электронная почта,
пароль (с подтверждением), дата рождения, согласие на
обработку персональных данных.
```python
class Registration2Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Сonsent to the processing of user data', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```
- Валидация должна проверять, что все поля заполнены
корректно (например, дата рождения должна быть в
формате дд.мм.гггг).
- При успешной регистрации пользователь должен быть
перенаправлен на страницу подтверждения регистрации.
```python
@app.route('/registration2/', methods=['GET', 'POST'])
def registration2():
    form = Registration2Form()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = form.username.data.lower()
        email = form.email.data
        date = form.date_of_birth.data
        user = User(username=username, email=email, date_of_birth=date)
        if User.query.filter(User.username == username).first() or User.query.filter(User.email == email).first():
            flash(f'Пользователь с username {username} или e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration2'))
    return render_template('registration2.html', form=form)
```

```html
{% block content %}
    <h1>Registration 2 page</h1>
    <form method="POST" action="{{ url_for('registration2') }}">
        {{ form.csrf_token }}
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}
        </p>
        <p>
            {{ form.date_of_birth.label }}<br>
            {{ form.date_of_birth() }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>
            {{ form.confirm_password.label }}<br>
            {{ form.confirm_password(size=32) }}
        </p>
        <p>
            {{ form.check.label }}<br>
            {{ form.check }}
        </p>
        <p>
        <input type="submit" value="Login">
        </p>
    </form>
{% endblock %}
```

## Задание №8
- Создать форму для регистрации пользователей на сайте.
```python
class Registration3Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    check = BooleanField('Сonsent to the processing of user data', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```
- Форма должна содержать поля "Имя", "Фамилия", "Email",
"Пароль" и кнопку "Зарегистрироваться".
```python
# models.py()
class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```
- При отправке формы данные должны сохраняться в базе
данных, а пароль должен быть зашифрован.
```python
@app.route('/registration3/', methods=['GET', 'POST'])
def registration3():
    form = Registration3Form()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User2(name=name, surname=surname, email=email)
        if User2.query.filter(User2.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration3'))
    return render_template('registration3.html', form=form)
```

```html
{% block content %}
    <h1>Registration 3 page</h1>
    <form method="POST" action="{{ url_for('registration3') }}">
        {{ form.csrf_token }}
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">
                        {{ message }}
                    </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <p>
            {{ form.name.label }}<br>
            {{ form.name(size=32) }}
        </p>
        <p>
            {{ form.surname.label }}<br>
            {{ form.surname(size=32) }}
        </p>
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=32) }}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}
        </p>
        <p>
            {{ form.confirm_password.label }}<br>
            {{ form.confirm_password(size=32) }}
        </p>
        <p>
            {{ form.check.label }}<br>
            {{ form.check }}
        </p>
        <p>
        <input type="submit" value="Login">
        </p>
    </form>
{% endblock %}
```

