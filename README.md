# UI Тесты интeрнет магазина [sad-i-ogorod.ru](https://sad-i-ogorod.ru/)

## Фреймворк PyTest
---
Структура каталогов проекта;

Проект содержит следующие основные каталоги:


`base` — Каталог с базовыми методами;
	`base_class.py` -;
`pages` — Каталог с методами страниц сайта;
	`main_page.py` -; 
	`login_page.py` -;
	`novinli_page.py` -;
	`seeds_page.py` -;
	`card_pages.py` -;
	`order_page.py` -;
`tests` — Каталог с файлами авто тестов;
	`test_login.py` -;

`utilites` — Каталог с внешними методами;

`requirements.txt` - это список всех модулей и пакетов Python, которые нужны для полноценной работы;

Для того чтобы установить пакеты из requirements.txt, необходимо открыть командную строку, перейти в каталог проекта;
и ввести следующую команду: `pip install -r requirements.txt`

Запуск `python -m pytest -s -v`
