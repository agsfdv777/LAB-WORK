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

### Завдання

- вкажіть у звіті що вивела пограма або зробіть скріншот та вставте у звіт;

**Програма вивела**:

``` text
Let's Start!
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
          
This is object: <__main__.MyName object at 0x7f7e88744280> 
This is object attribute: Bogdan / 1
This is <class 'property'>: My name is Bogdan / Bogdan@itcollege.lviv.ua
This is <class 'method'> call: Bogdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
          
This is object: <__main__.MyName object at 0x7f7e88744f70> 
This is object attribute: Notbogdan / 2
This is <class 'property'>: My name is Notbogdan / Notbogdan@itcollege.lviv.ua
This is <class 'method'> call: Notbogdan@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<
          
This is object: <__main__.MyName object at 0x7f7e88744fd0> 
This is object attribute: Anonymous / 4
This is <class 'property'>: My name is Anonymous / Anonymous@itcollege.lviv.ua
This is <class 'method'> call: Anonymous@itcollege.lviv.ua
This is static <class 'function'> with defaults: You say: Hello to everyone! 
This is class variable <class 'int'>: from class 4 / from object 4
<*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*><*>
We are done. We create 4 names! ??? Why 4?
```

- ознайомтесь з кодом та зрозумійте за що відповідає кожен з рядків; Зрозуіло.
- Модифікуйте програму додавши своє імя в список; Є

#### дайте відповідь на запитання

1. Чому коли передаємо значення None створюється обєкт з іменем Anonymous?
Тому, що класовий метод (анонімний користувач) створює об'єкт, передаючи в параметр Anonymous.

  ```python
   self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
  ```

  Цей метод було викликано при перевірці параметра в "конструкторі" на те, чи  він має значення None(не існуючий, нічого,як я зрозумів)
2. Як змінити текст привітання при виклику методу say_hello()? Допишіть цю частину коду.
Або змінити параметр(аргумент) за замовчуванням, або передачи інше значення при виклику цього метода

```python
This is static {type(MyName.say_hello)} with defaults: {me.say_hello("f*ck you, Nvidia")} 
```

```text
This is static <class 'function'> with defaults: You say: f*ck you, Nvidia 
```

> сказав Лінус Торвальдс  

Лінус поганого не скаже...  
3. Допишіть функцію в класі яка порахує кількість букв і імені (підказка: використайте функцію len());

```python
    def __len__(self) -> str:
        """Class property
        return: name.len()
        """
        return len(self.name)
```  

зроблено
4. Порахуйте кількість імен у списку names та порівняйте із виведеним результатом. Дайте відповідь чому маємо різну кількість імен?
у списку є два імені, і нічого.
Нічого -- далося ім'я анонім.
3 імені.
При створенні аноніма, змінна **total_names** збільшилася на 1 двічі.Це помилка!

- **Помилку було виправлено**

```python
    __anonymous_name = "Anonymous"

    def __init__(self, name=None) -> None:
        MyName.total_names += 1  # modify class variable
        
        # Class attributes / Instance variables
        self.name = name if name is not None else self.__anonymous_name  
        self.my_id = self.total_names

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls(cls.__anonymous_name)
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
