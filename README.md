Что это
===================


Небольшой наипростейший сайт для внутреннего пользования школы

----------


Что нужно для работы
-------------

Если Вы никогда не работали с фреймворком Django, то рекомендуется посетить [серию уроков](http://tutorial.djangogirls.org/ru/) . Поймут даже блондинки:) 

> **Note:**

> - Для работы необходимы уже установленные **python3**. Проверить версию питона можно командой `python -V `
> - Не обязательно, но желательно запускать всё в виртуальном окружении. Автор использовал пакет **virtualenv**.
> - Для удобства можно ещё поставить обертку **virtualenvwrapper**. 

#### Чистый комп

1. На чистую систему (автор пишет о linux-подобных) устанавливаются пакеты python3 и virtualenv привычным для вас способом (консоль или менеджер пакетов). Также ставим пакеты pip. 
2. Стоит обновить pip до последней версии `sudo pip install --upgrade pip`.
3. Далее ставим обертку `pip install virtualenvwrapper ` . 
4. Команда `which virtualenvwrapper.sh` покажет путь к файлу virtualenvwrapper.sh. 
5. В домашней директории открываем .bashrc и записываем туда строки 

    `export WORKON_HOME=$HOME/.virtualenvs #здесь все окружения будут храниться`
    `source *путь, который выдал шаг 4*/virtualenvwrapper.sh`
    
6. В консоли выполняем `source .bashrc` - всё, наши команды работают.
7. Создайте виртуальное окружение с Python3 и Django 1.9. Используйте `mkvirtualenv --python=/usr/bin/python3 python3` , если системная версия языка ниже третьей. Установить django можно `pip install Django 1.9`

#### Порядок действий при первом запуске

*Для начала необходимо создать таблицы в базе данных. Сделать это можно при помощи команды `$ python manage.py migrate` или `$ python manage.py syncdb`
*Загрузить данные `$ python manage.py loaddata initial_data`
*Заупустить сервер `$python manage.py runserver`

> **Note:**

> - Если вы хотите изменить порт, укажите его как аргумент. Например, эта команда запускает сервер используя порт 8080: `python manage.py runserver 8080` .
> - Если вы хотите изменить IP, передайте его вместе со значением порта. Например, эта команда слушает все публичные IP: `python manage.py runserver  0.0.0.0:8000` 
