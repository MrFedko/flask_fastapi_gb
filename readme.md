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
Написать функцию, которая будет выводить на экран HTML
страницу с таблицей, содержащей информацию о студентах.
Таблица должна содержать следующие поля: 
- "Имя"
- "Фамилия" 
- "Возраст" 
- "Средний балл"

Данные о студентах должны быть переданы в шаблон через
контекст.
[link for app](/seminar_1/app_stud.py)

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
