# Geometry Library

![CI](https://github.com/leynhf/unit_test_for_geometry_lib/actions/workflows/main.yml/badge.svg)

Библиотека для вычисления площади и периметра простых геометрических фигур:
- Круг
- Квадрат
- Прямоугольник
- Треугольник

✅ 100% покрытие тестами  
✅ Автоматический запуск тестов через GitHub Actions  
✅ HTML отчёт покрытия (скачивается из Artifacts)  
✅ flake8 проверка качества кода  

---

## ✅ Функциональность

| Фигура | Площадь | Периметр |
|--------|---------|----------|
| Круг | `π * r²` | `2 * π * r` |
| Квадрат | `a²` | `4a` |
| Прямоугольник | `a * b` | `2(a + b)` |
| Треугольник | `a * h / 2` | `a + b + c` |

---

## ✅ Пример использования

```python
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area
from square import perimeter as square_perimeter

print(circle_area(3))          # 28.2743...
print(circle_perimeter(3))     # 18.8495...
print(rectangle_area(4, 6))    # 24
print(square_perimeter(2.5))   # 10
```

---

## ✅ Запуск тестов

```
python3 -m unittest discover .
```

---

## ✅ Покрытие тестами
```
python3 -m coverage run -m unittest discover .

python3 -m coverage report

python3 -m coverage html
```
HTML отчёт появится в папке:
htmlcov/index.html

---

## ✅ CI / GitHub Actions

Каждый ```push``` и ```pull_request``` автоматически запускает:

✔ тесты

✔ coverage

✔ flake8

✔ загрузку coverage в Artifacts

---

## ✅ Установка
```
pip install geometric-lib
```

---

## Автор
Софья Тесленок, М3123