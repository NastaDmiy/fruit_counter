# Fruit Counter — Подсчёт фруктов на изображениях

Веб-приложение для автоматического подсчёта фруктов (бананов и яблок) на изображениях с использованием нейросетевой модели YOLOv8.

## Функциональные возможности

- Загрузка изображений (форматы JPG, PNG, WEBP)
- Детекция бананов и яблок с помощью YOLOv8n
- Подсчёт количества фруктов по видам
- Отображение результата с ограничивающими рамками
- Сохранение истории обработки в SQLite
- Экспорт истории в Microsoft Excel

## Стек технологий

- Python 3.12
- YOLOv8 (Ultralytics)
- Flask
- OpenCV
- SQLite
- HTML + CSS + JavaScript

## Структура проекта

fruit_counter

- app.py
- detector.py
- requirements.txt
- README.md
- history.db
- .gitignore
- yolov8n.pt

- templates
  - index.html

- static
  - result_*.jpg

- uploads

- venv

## Установка и запуск

1. Клонируйте репозиторий:

git clone https://github.com/NastaDmiy/fruit_counter.git

cd fruit_counter

2. Создайте виртуальное окружение:

python -m venv venv

source venv/Scripts/activate # для Windows (Git Bash)

## ИЛИ

venv\Scripts\activate # для Windows (CMD)

3. Установите зависимости:

pip install -r requirements.txt

4. Запустите приложение:

python app.py

## ИЛИ

py app.py

5. Откройте в браузере:

http://127.0.0.1:5000


## Результаты тестирования

- Точность детекции: 100% на тестовых выборках
- Среднее время обработки: 0,416 секунды
- Поддерживаемые классы: банан (46), яблоко (47)

## Автор

Дмитриева Анастасия Алексеевна, группа УБВТ2401
