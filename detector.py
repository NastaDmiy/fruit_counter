import cv2
from ultralytics import YOLO
import os

# Загружаем модель YOLOv8n
model = YOLO('yolov8n.pt')

# Классы фруктов в наборе данных COCO:
# 46 - banana, 47 - apple, 48 - orange
# 32 - sports ball (иногда модель видит апельсины как мячи)

FRUIT_CLASSES = [46, 47]
FRUIT_NAMES = {
    46: 'Банан',
    47: 'Яблоко'
}


def detect_fruits(image_path):
    """
    Детектирует фрукты на изображении.
    Возвращает:
        total_count - общее количество фруктов
        fruit_details - словарь {название: количество}
        output_path - путь к сохранённому изображению с рамками
    """
    # Читаем изображение
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение: {image_path}")

    # Прогоняем через нейросеть
    results = model(img)

    # --- ОТЛАДКА: выводим все найденные классы ---
    print("\n" + "=" * 50)
    print("НАЙДЕННЫЕ ОБЪЕКТЫ НА ИЗОБРАЖЕНИИ:")
    print("=" * 50)

    all_objects = {}
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            name = model.names[cls]
            all_objects[name] = all_objects.get(name, 0) + 1

    if all_objects:
        for name, count in all_objects.items():
            print(f"  {name}: {count} шт.")
    else:
        print("Объекты не найдены!")

    print("\n" + "-" * 50)
    print("ПРОВЕРКА ФРУКТОВ:")
    print("-" * 50)
    # --------------------------------------------

    # Счётчики
    fruit_counts = {}
    total_count = 0

    # Обрабатываем результаты
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls in FRUIT_CLASSES:
                total_count += 1
                name = FRUIT_NAMES.get(cls, 'Неизвестный фрукт')
                fruit_counts[name] = fruit_counts.get(name, 0) + 1
                print(f"НАЙДЕН: {name} (класс {cls})")
            else:
                print(f"Игнорируем: {model.names[cls]} (класс {cls})")

    print("-" * 50)
    print(f"ВСЕГО ФРУКТОВ: {total_count}")
    if fruit_counts:
        for name, count in fruit_counts.items():
            print(f"  {name}: {count} шт.")
    else:
        print("Фрукты не обнаружены!")
    print("=" * 50 + "\n")

    # Сохраняем изображение с рамками
    img_with_boxes = results[0].plot()
    output_filename = f"result_{os.path.basename(image_path)}"
    output_path = os.path.join('static', output_filename)
    cv2.imwrite(output_path, img_with_boxes)

    return total_count, fruit_counts, output_path


# Для тестирования
if __name__ == '__main__':
    test_path = 'test.jpg'
    if os.path.exists(test_path):
        total, details, out = detect_fruits(test_path)
        print(f"Результат сохранён: {out}")
    else:
        print("Положите test.jpg в папку для теста")