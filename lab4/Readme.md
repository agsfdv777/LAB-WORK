# Звіт до роботи 4

## Тема: Віртуальні середовища

### Мета роботи: ознайомитися із віртуальними середовищами та програмою для полегшення роботи з ними,пакетним менеджером pip та деякими бібліотеками,  методами видалення та встановлення їх.

---

### Виконання роботи

#### Основи роботи з сторонніми бібліотеками

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
   
   ```python
   pip install requests
   python #Зайдіть в пайтон інтерпретатор
   >>> import requests
   >>> r = requests.get('https://google.com')
   >>> r.status_code
   >>> exit()
   ```

4. Вставте у звіт результат виконання команд (скріншот або стрічки що вивелись);
   
   ![d](https://github.com/zayats1/ItCollegeDB/raw/master/lab4/screenshoths/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-10-09%2020-35-36.png)

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

#### Робота у віртуальному середовищі

1. [Віртуальні середовища в Python](https://docs.python.org/3/library/venv.html) - це ізольовані середовища для роботи з 'замороженою' версією Python та його бібліотек. Середовище створюється для кожного проекту окремо і буде мати ті самі характеристики в не залежності де та на якій системі буде запущено;

2. Для створення :male_sign: `VENV`:male_sign: та його активації виконайте команди(bash :penguin:): 
   
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

#### Робота з Pipenv

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
   
   Options:
     --where                         Output project home information.
     --venv                          Output virtualenv information.
     --py                            Output Python interpreter information.
     --envs                          Output Environment Variable options.
     --rm                            Remove the virtualenv.
     --bare                          Minimal output.
     --man                           Display manpage.
     --support                       Output diagnostic information for use in
                                     GitHub issues.
     --site-packages / --no-site-packages
                                     Enable site-packages for the virtualenv.
                                     [env var: PIPENV_SITE_PACKAGES]
     --python TEXT                   Specify which version of Python virtualenv
                                     should use.
     --three                         Use Python 3 when creating virtualenv.
                                     Deprecated
     --clear                         Clears caches (pipenv, pip).  [env var:
                                     PIPENV_CLEAR]
     -q, --quiet                     Quiet mode.
     -v, --verbose                   Verbose mode.
     --pypi-mirror TEXT              Specify a PyPI mirror.
     --version                       Show the version and exit.
     -h, --help                      Show this message and exit.
   ```

3. Для створення середовища я ввів наступні команди 
   
   ```shell
   pipenv --python 3.10
   
   pipenv --venv
   
   pipenv run python -V
   
   pipenv install requests
   ```
   
    Пізніше мені прийшлося видозмінити Pipfile -- видалив повну версію( хоча можна було б видалити лише загальну версію, а повну -- залишити )
   
   ![ s](https://github.com/zayats1/ItCollegeDB/raw/master/lab4/screenshoths/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-10-10%2021-24-10.png)

4.  Переконайтесь що у Вас створились файли `Pipfile` та `Pipfile.lock`. Що в них знаходиться
   
   в цих файлах знаходиться інформація про пакети,їх версії. Pypfile.lock зберігає інформацію про пакети(бібліотеки, пайтон рантайми)   
   
   разом із хешами.

5. Створіть пайтон файл та запишіть в нього наступну програму: (Зроблено :male_sign: sir :male_sign:)
   
   ```python
   import requests
   
   response = requests.get('https://httpbin.org/')
   for line in response.iter_lines():
       print(line)
   ```

6. Спробуйте запустити програму з Visual Studio. Запустіть програму з командної стрічки. Запустіть програму зайшовши у віртуальне середовище за допомогою команди `pipenv shell`. Результати запишіть у звіт.
   
   ![dd](https://github.com/zayats1/ItCollegeDB/raw/master/lab4/screenshoths/%D0%97%D0%BD%D1%96%D0%BC%D0%BE%D0%BA%20%D0%B5%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%B7%202022-10-10%2021-45-08.png)

7. 

### Висновок

> у висновку потрібно відповісти на запитання:

- :question: Що зроблено в роботі;

- :question: Чи досягнуто мети роботи;
  
  Yes, my master, BobasB.

- :question: Які нові знання отримано;
  
  Краще освоїв  редактор MarkText, навчився додавати програми в PATH   на  Linux (bash)

- :question: Чи вдалось відповісти на всі питання задані в ході роботи;
  
  :male_sign: yes, my master  :male_sign:

- :question: Чи вдалося виконати всі завдання;
  
  :male_sign: yes sir :male_sign:

- :question: Чи виникли складності у виконанні завдання;
  
  так, деякі команди в методичці були під вінду:cactus:,pipenv потребувало створення деяких системних змінних та стирання одніє версії
  
   пайтона  або глобальної, або повної.

- :question: Чи подобається такий формат здачі роботи (Feedback);
  
  that's :male_sign: amazing :male_sign:
  
  дякую за навчання користуванню Пайтоном!

- :question: Побажання для покращення (Suggestions);
  
  В методичках вказувати варіанти для Un*x POSIX,  а не лише для вінди.
  
  Давати менше завдань за одну роботу(краще знати менше, але досконало)

---
