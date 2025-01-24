import os
from dotenv import load_dotenv
load_dotenv()

import smtplib

letter = """\
From: {from_who}
To: {to_who}
Subject: {theme}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём Gitub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(from_who='devmanorg@yandex.ru', to_who='iCloudCD@yandex.ru', theme='Приглашение')

letter = letter.replace('%website%', 'https://dvmn.org/profession-ref-program/id77480752/InhEP/') # имя сайта
letter = letter.replace('%friend_name%', 'Павел') # имя друга
letter = letter.replace('%my_name%', 'Сергей') # имя отправителя

letter = letter.encode("UTF-8")

LOGIN = os.getenv('MY_LOGIN')
TOKEN = os.getenv('MY_TOKEN')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(LOGIN, TOKEN)
server.sendmail('devmanorg@yandex.ru', 'iCloudCD@yandex.ru', letter)
server.quit()

print(letter)