# Звіт до роботи

## Тема: ООП в мові :snake: Пайтон

### Мета роботи

Зрозуміти що таке ООП, класи та їм методи, змінні(в інших джерелах їх називають властивостями), навичтися користуватися ними,зрозуміти відмінність звичайного та об'єктно-орієнтованого представлення даних.

---

### Виконання роботи

- Результати виконання завдання _1...N_;
    1. Навчились програмувати в ОО стилі на мові python :snake:
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті);

> якщо графічних файлів багато то краще помістити їх у окрему папку, наприклад у мене це папка `pictures`. Уважно дивіться коли вставляєте URL - файл має бути представленим як `raw`.

![alt text](https://github.com/zayats1/ItCollegeDB/raw/31b1cf1fb4ccca5a8564d8b03be58abbf7df42c6/lab3/screenshots/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-09-25%2014-25-50.png)

### Decorators

![alt text](https://github.com/zayats1/ItCollegeDB/raw/31b1cf1fb4ccca5a8564d8b03be58abbf7df42c6/lab3/screenshots/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-09-25%2014-25-01.png)

### Class methods

![alt text](https://github.com/zayats1/ItCollegeDB/raw/31b1cf1fb4ccca5a8564d8b03be58abbf7df42c6/lab3/screenshots/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-09-25%2014-34-51.png)

- вставлений код / текстовий або числовий результат / інші результати:

```python
from datetime import datetime
class MyAnimals:
    def __init__(self, animal_type, name, age) -> None:
        self.type = animal_type
        self.name = name
        self.age = age
    
    @property
    def get_my_pet_bithrday(self):
        return f"The {self.type} called {self.name} is {self.age} years old now" 
    
    def add_one_year(self):
        self.age += 1
        
pig = MyAnimals("Pig","Duff",1)

print(pig.get_my_pet_bithrday)

pig.add_one_year()

print(pig.get_my_pet_bithrday)
```

```text
The Pig called Duff is 1 years old now
The Pig called Duff is 2 years old now
```

### Висновок

> у висновку потрібно відповісти на запитання:

- :question: Що зроблено в роботі;
- :question: Чи досягнуто мети роботи :male_sign: Yes sir :male_sign:;
- :question: Які нові знання отримано OOP;
- :question: Чи вдалось відповісти на всі питання задані в ході роботи? yeah;
- :question: Чи вдалося виконати всі завдання; "Yes sir"
- :question: Чи виникли складності у виконанні завдання;
   Yes, my master... :cry:
- :question: Чи подобається такий формат здачі роботи (Feedback);
  Yes, but actualy no.
- :question: Побажання для покращення (Suggestions);
  **Поменше коду за одне заняття**

---
