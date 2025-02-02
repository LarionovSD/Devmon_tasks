import os
from dotenv import load_dotenv
load_dotenv()
import smtplib

sender_email = 'devmanorg@yandex.ru' # арес отправителя
recipient_email = 'iCloudCD@yandex.ru' # адрес получателя
theme = 'Приглашение!' # тема письма
my_name = 'Сергей' # имя отправителя
friend_name = 'Павел' # имя получателя
web_site = 'https://dvmn.org/profession-ref-program/id77480752/InhEP/' # имя сайта

letter = """\
From: {from_who}
To: {to_who}
Subject: {theme_of_letter}

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
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format(\
from_who=sender_email, to_who=recipient_email, theme_of_letter=theme)

letter = letter.replace('%my_name%', my_name)
letter = letter.replace('%friend_name%', friend_name)
letter = letter.replace('%website%', web_site)

letter = letter.encode("UTF-8")

LOGIN = os.getenv('MY_LOGIN')
TOKEN = os.getenv('MY_TOKEN')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(LOGIN, TOKEN)
server.sendmail(sender_email, recipient_email, letter)
server.quit()