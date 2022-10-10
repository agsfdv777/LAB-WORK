# Звіт до роботи

## Тема: _згідно теми_

### Мета роботи: _згідно теми_

---

### Виконання роботи

- Результати виконання завдання _1...N_;
  
  1. Розробили/Створили ...
  2. Програма вивела значення ...
  3. Отримано наступні результати ...
  4. Навчились ...

- вставлені рисунки (скріншоти екрана або фотографії виконаного завдання у зошиті);
  
  > якщо графічних файлів багато то краще помістити їх у окрему папку, наприклад у мене це папка `pictures`. Уважно дивіться коли вставляєте URL - файл має бути представленим як `raw`.
  > ![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")

- вставлений код / текстовий або числовий результат / інші результати:
  
  ```python
  def simple_function_example():
    pass
  ```
  
  ```text
  << SOME text HERE >>
  ```

- результати виконання індивідуального завдання (якщо такі є); 
  
  **Основи роботи з сторонніми бібліотеками**
  
  1. Перевірте чи  встановлений pip на компютері
     
     ```text
     pip 22.2.2 from /home/bogdandev/.local/lib/python3.10/site-packages/pip (python 3.10)
     ```
  
  2. Передивіться які дії можна зробити за допомогою `pip`. Перевірте які бібліотеки вже інстальовані на Вашому компютері та вкажіть їх у звіті (скріншот або стрічки що вивелись);
     **Commands:**
     
     ```bash
       install                     Install packages.
       download                    Download packages.
       uninstall                   Uninstall packages.
       freeze                      Output installed packages in requirements format.
       inspect                     Inspect the python environment.
       list                        List installed packages.
       show                        Show information about installed packages.
       check                       Verify installed packages have compatible dependencies.
       config                      Manage local and global configuration.
       search                      Search PyPI for packages.
       cache                       Inspect and manage pip's wheel cache.
       index                       Inspect information available from package indexes.
       wheel                       Build wheels from your requirements.
       hash                        Compute hashes of package archives.
       completion                  A helper command used for command completion.
       debug                       Show information useful for debugging.
       help                        Show help for commands.
     
     ```
     
     **pip list**  (не повний)
     
     >  pip list
     > Package                      Version
     > 
     > ---------------------------- -----------------
     > 
     > anytree                      2.8.0
     > appdirs                      1.4.4
     > argon2-cffi                  21.3.0
     > argon2-cffi-bindings         21.2.0
     > asciidoc                     10.2.0
     > asttokens                    2.0.8
     > async-timeout                4.0.2
     > attrs                        22.1.0
     > autocommand                  2.2.1
     > Automat                      20.2.0
     > autopep8                     1.6.0
     > Babel                        2.10.3
     > backcall                     0.2.0
     > beautifulsoup4               4.11.1
     > bleach                       5.0.1
     > Brotli                       1.0.9
     > btrfsutil                    5.19.1
     > certifi                      2022.9.24
     > cffi                         1.15.1
  
  3. Будь-яку сторонню бібліотеку можна встановити на комп'ютер за допомогою `pip install` команди та зразу почати її використовувати,   наприклад встановимо бібліотеку [requests](https://requests.readthedocs.io/en/latest/):
  
  4. Вставте у звіт результат виконання команд (скріншот або стрічки що вивелись);
     
     ![d]()
  
  5. Ознайомтесь які ще методи є в бібліотеці [requests, та спробуйте їх використати](https://requests.readthedocs.io/en/latest/user/quickstart/);
6. Даний спосіб інсталяції робить бібліотеку загальнодоступною для даної системи. Будь-яке оновлення бібліотеки буде застосоване до всіх Python проектів на Вашому комп'ютері;
   
   ```text
   pip show requests
   pip install requests==2.1
   pip show requests
   pip uninstall requests
   ```

7.  Вкажіть у звіті результат виконання команд 
   
   1. **pip show requests**
      
      > Name: requests
      > Version: 2.28.1
      > Summary: Python HTTP for Humans.
      > Home-page: https://requests.readthedocs.io
      > Author: Kenneth Reitz
      > Author-email: me@kennethreitz.org
      > License: Apache 2.0
      > Location: /usr/lib/python3.10/site-packages
      > Requires: idna, urllib3
      > Required-by: requests-file, tldextract
   
   2. **pip install requests==2.1**
      
      > Defaulting to user installation because normal site-packages is not writeable
      > Collecting requests==2.1
      >   Downloading requests-2.1.0-py2.py3-none-any.whl (445 kB)
      > 
      >      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 445.3/445.3 kB 517.0 kB/s eta 0:00:00
      > 
      > Installing collected packages: requests
      > Successfully installed requests-2.1.0
   
   3. **pip show requests**
      
      > requests
      > Successfully installed requests-2.1.0
      > [bogdandev@bogdandev lab4]$ pip show requests
      > Name: requests
      > Version: 2.1.0
      > Summary: Python HTTP for Humans.
      > Home-page: http://python-requests.org
      > Author: Kenneth Reitz
      > Author-email: me@kennethreitz.com
      > License: Copyright 2013 Kenneth Reitz
      > Location: /home/bogdandev/.local/lib/python3.10/site-packages
      > Requires: 
      > Required-by: requests-file, tldextract
   
   4. **pip uninstall requests**
      
      > pip uninstall requests
      > Found existing installation: requests 2.1.0
      > Uninstalling requests-2.1.0:
      >   Would remove:
      > 
      >     /home/bogdandev/.local/lib/python3.10/site-packages/requests-2.1.0.dist-info/*
      >     /home/bogdandev/.local/lib/python3.10/site-packages/requests/*
      > 
      > Proceed (Y/n)? y
      >   Successfully uninstalled requests-2.1.0

**Робота у віртуальному середовищі**

1. [Віртуальні середовища в Python](https://docs.python.org/3/library/venv.html) - це ізольовані середовища для роботи з 'замороженою' версією Python та його бібліотек. Середовище створюється для кожного проекту окремо і буде мати ті самі характеристики в не залежності де та на якій системі буде запущено;

2. Для створення :male_sign: `VENV`:male_sign: та його активації виконайте команди: 
   
   ```text
   python -m venv ./my_env
   source my_env/bin/activate
   pip install requests
   deactivate
   pip show requests
   ```

3. Вкажіть у звіті що вивела остання команда та чому
   
   > Name: requests
   > Version: 2.28.1
   > Summary: Python HTTP for Humans.
   > Home-page: https://requests.readthedocs.io
   > Author: Kenneth Reitz
   > Author-email: me@kennethreitz.org
   > License: Apache 2.0
   > Location: /usr/lib/python3.10/site-packages
   > Requires: idna, urllib3
   > Required-by: requests-file, tldextract
   
   Ця команда видала позитивний результат тому, що ця бібліотека встановлена через пакетний менеджер мого дистрибутиву :water_buffalo:GNU/Linux :penguin:  (як залежність). :nerd_face:

4.  Всі створені файли НЕ потрібно комітити в репозиторій. Щоб уникнути такого автоматично створіть файл `.gitignore` у кореневій папці та вкажіть в ньому папки які потрібно ігнорувати. Ok buddy!

**Робота з Pipenv**

1. [Pipenv](https://pipenv.pypa.io/en/latest/) - це інструмент для спрощення інсталяції сторонніх бібліотек та створення віруального середовища для кожного проекту. Для його інсталяції застосуйте команду:
   
   ```text
   pip install pipenv
   # Після успішного виконання команди виконайте
   pipenv --help
   ```

2.  Вкажіть у звіті які команди можна виконувати за допомогою `pipenv`
   
   ```bash
     check         Checks for PyUp Safety security vulnerabilities and against
                   PEP 508 markers provided in Pipfile.
     clean         Uninstalls all packages not specified in Pipfile.lock.
     graph         Displays currently-installed dependency graph information.
     install       Installs provided packages and adds them to Pipfile, or (if no
                   packages are given), installs all packages from Pipfile.
     lock          Generates Pipfile.lock.
     open          View a given module in your editor.
     requirements  Generate a requirements.txt from Pipfile.lock.
     run           Spawns a command installed into the virtualenv.
     scripts       Lists scripts in current environment config.
     shell         Spawns a shell within the virtualenv.
     sync          Installs all packages specified in Pipfile.lock.
     uninstall     Uninstalls a provided package and removes it from Pipfile.
     update        Runs lock, then sync.
     verify        Verify the hash in Pipfile.lock is up-to-date.
   
   ```

3. 

### Висновок

> у висновку потрібно відповісти на запитання:

- :question: Що зроблено в роботі;

- :question: Чи досягнуто мети роботи;

- :question: Які нові знання отримано;
  
  Краще освоїв  редактор MarkText

- :question: Чи вдалось відповісти на всі питання задані в ході роботи;

- :question: Чи вдалося виконати всі завдання;
  
  :male_sign: yes sir :male_sign:

- :question: Чи виникли складності у виконанні завдання;

- :question: Чи подобається такий формат здачі роботи (Feedback);
  
  that's :male_sign: amazing :male_sign:

- :question: Побажання для покращення (Suggestions);

---
