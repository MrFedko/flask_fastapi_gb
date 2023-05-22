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
