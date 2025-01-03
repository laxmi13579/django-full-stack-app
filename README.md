# 1. Django

## a. Pass value through the URL patterns

Using kwargs we can pass the value shown in the **index** views

## b. Static file setup

main.html

<!DOCTYPE html>

{% load static %}

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'app1/css/style.css' %}">
    <title>Document</title>
</head>
<body>
    <h1>Welcome to main page</h1>
    <button onclick="disp()">alert</button>
    <img src="{% static 'app1/images/lax.jpg' %}" width="200px" alt="laxmi pic">
    <script src="{% static 'app1/js/script.js' %}"></script>
</body>
</html>

script.js

function disp() {
alert('Hello Laxmi Yadav')
}

style.js

body {
background-color: gray;
}

## c. Tailwind setup for Django project

Use below link to installation django with tailwind

https://django-tailwind.readthedocs.io/en/latest/installation.html

## d. URL setup

url.py

    path('', views.main, name="main"),

base.html

    <a href="{% url 'main' %}" class="block px-4 py-2">Home</a>

## d. Template setup

Created seperate navbar.html page and include it in base.html file
