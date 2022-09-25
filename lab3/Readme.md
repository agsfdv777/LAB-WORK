# Звіт до роботи

## Тема: _згідно теми_

### Мета роботи: _згідно теми_

---

### Виконання роботи

- Результати виконання завдання _1...N_;
    1. Навчились програмувати в ОО стилі на мові python :snake:
- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті);

> якщо графічних файлів багато то краще помістити їх у окрему папку, наприклад у мене це папка `pictures`. Уважно дивіться коли вставляєте URL - файл має бути представленим як `raw`.

![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")

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
  **Поменше коду за раз, і розлядати кожну властивість ооп окремо**

---
