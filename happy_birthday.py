import datetime
from LiteVkApi import Vk
from config import my_token
from random import choice

vk_session = Vk.login(tok=my_token, userbot=True)
bdate_info = Vk.VkMethod(vk_session, 'friends.get', {'fields': 'bdate'})
persons = bdate_info['items']

congrats_list = ['Congratulation!']

date = datetime.datetime.today()
current_date = str(date.day)+'.'+str(date.month)

for person in persons:
    person_id = str(person['id'])
    person_bdate = person.get('bdate', '0')

    splited_bdate = person_bdate.split('.')[:2]
    current_person_bdate = '.'.join(splited_bdate)

    if current_person_bdate == current_date:
        Vk.msg(vk_session, text=choice(congrats_list), userid=person_id)
        print(f'Поздравление отправлено пользователю {person["first_name"]} {person["last_name"]}.')
