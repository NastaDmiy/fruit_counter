# Fruit Counter — Подсчёт фруктов на изображениях

Веб-приложение для автоматического подсчёта фруктов (бананов и яблок) на изображениях с использованием нейросетевой модели YOLOv8.

## Функциональные возможности

- Загрузка изображений (JPG, PNG, WEBP)
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

## Установка и запуск

```bash
# 1. Клонирование репозитория
git clone https://github.com/NastaDmiy/fruit_counter.git
cd fruit_counter

# 2. Создание виртуального окружения
python -m venv venv
source venv/Scripts/activate   # для Windows (Git Bash)
# или
venv\Scripts\activate          # для Windows (CMD)

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Запуск приложения
python app.py
# или
py app.py
```

Откройте в браузере: `http://127.0.0.1:5000`

## Структура проекта
# Структура проекта

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

## Результаты тестирования

- Точность детекции: 100% на тестовых выборках
- Среднее время обработки: 0,416 секунды
- Поддерживаемые классы: банан (46), яблоко (47)

## Автор

Дмитриева Анастасия Алексеевна, группа УБВТ2401
