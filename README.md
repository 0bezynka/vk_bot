# Скрипты для накрутки друзей ВК
### Простой скрипт по накрутке
Получайт список  друзей(10) вк которые сейчас онлайн. У каждого пользователя находит друга(4) который тоже онлайн, отправляет ему заявку. Всего отправляется 40 заявок, ограничение ВК 50 в сутки. Скрипт поставить на крон раз в сутки и хватит.
+ lite_bot.py
###### (Лично у меня проблем не возникало, успешно накрутил 400 др, на этом тест и закончил)
### Уже что то по интересней ...
Скрипт по сложнее его функции: получает список подписчиков/заявок в др, обобряет всё. Затем возвращает список возможных друзей(42), отправляет заявки этим пользователям. Иногда вылетают ошибки.    
Частая ошибка: пользователь в подписчиках но он ЗАБЛОКИРОВАН, он его не может добавить т.к. его не существует.      
Решение: сделать фильтр таких или вырезать эту часть кода.       
+ nbot.py
