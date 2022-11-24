SUPPORT="ИМЯ ПОДДЕРЖКИ"
import horoscopedb as horoscopedb
from datetime import datetime
MANAGER_TOKEN="5118975151:AAFCILKAZCH7Z2OIv8ZzAqQ2l16-GKEP6Uk"
# TOKEN="5321240856:AAGg8_PBKSMin50vxhKzWud0-xR95sp_QMQ"#astrologyEveryDay
TOKEN = "5321240856:AAGg8_PBKSMin50vxhKzWud0-xR95sp_QMQ"

photos={"inter_name":"days/name.png",
"inter_gender":"days/gender.png",
"inter_city":"days/city.png",
"inter_date":"days/date.png",
"inter_time":"days/birth_time.png",
"inter_time_option":"days/time.png",
}
def select_all_active_until_table(id=None):
    try:
    
        today_data=datetime.now().date()
        conn=horoscopedb.ConnectDb()
        cur = conn.cursor()
        if id ==None:
            cur.execute("SELECT TelegramID, ActiveUntil FROM Users")
        else:
            cur.execute("SELECT TelegramID, ActiveUntil FROM Users WHERE (TelegramID = %s)",(id,))
        res = list()
        records = cur.fetchall()
        cur.close()
        conn.commit()
        for row in records:
            if row[1]!="":
                end_date=row[1]
                days_till_end=end_date-today_data
                days_till_end=days_till_end.days
                end_date=datetime.strftime(end_date,"%d.%m.%Y")
                res.append({"id":row[0],"active_until":end_date,"days_till_end":days_till_end})
        res[0]=dict(res[0])
        if id==None:
            return res
        else:
            return(res[0])
    except Exception as error:
        return(list())
    finally:    
        if cur:
            cur.close()
            conn.close()

text_for_friends="текст для друга "
managers=[952863788,214207257, 778327202,5312336082,1098353716]
bots=["5393264409:AAFd137o2MSINcbYLK_9s2UZso_0OAXUBmU"]
bot_name="@EveryDayAstrologyBot"
cost={30:69,
180:330,365:580}
url_for_all="<a href='https://google.com'>url из конфига</a>"
url_for_costs={30:'''"<a href='https://google.com'>в конфиге указать url на 30</a>"''',
180:'''"<a href='https://google.com'>в конфиге указать url на 180</a>"''',365:'''"<a href='https://google.com'>в конфиге указать url на 365</a>"'''}
cost_text='''Доступно 3 варианта продления подписки: на 30, 180 и 365 дней.

✅ Стоимость подписки на месяц - 69 рублей

На полугодовой и годовой тариф действует скидка 20 и 30 % соответственно:

✅ Стоимость подписки на пол года - <strike>414</strike> 330 ₽

✅ Стоимость подписки на год: <strike>828</strike> 580 ₽

При продлении сроки подписок
суммируются.

Выбери подходящий тариф!'''
info_text="В подписку входит общее описание дня с точки зрения расположения звезд и планет, ваш персональный гороскоп, который будет составляться и направляться вам каждый день в указанное вами время."
start_message="Привет! Добро пожаловать в первый персональный Астробот!\n\nЧто умеет этот бот ?\n\n⭐ Создает ваш личный персональный гороскоп! Он формируется, исходя из даты, времени и места вашего рождения. Каждый гороскоп индивидуален.\n\n"
start_message2="Давайте прямо сейчас сформируем ваш первый гороскоп!\n\nОн создается на основе вашей натальной карты - это координаты расположения планет и созвездий на небе в момент вашего рождения.\n\nНатальная карта строго индивидуальна для каждого человека. Чтобы ее сформировать, нужно ответить всего на 5 вопросов!\n\nЭто займет не более 1 минуты"
inter_name="Пожалуйста, введите свое имя"
inter_gender=""
inter_city="Пожалуйста, введите место своего рождения"
inter_date="Пожалуйста, введите дату своего рождения в формате 15.11.2001"
inter_time="Пожалуйста, введите время своего рождения в таком формате 12:00"
inter_time_option="""Утром - гороскоп на сегодняшний день
Вечером - гороскоп на завтрашний день"""
message_after_registaration="Отлично, все данные заполнены!\n\nФормирование вашей натальной карты и вашего первого персонального гороскопа займет немного времени. Пожалуйста, потерпите."
after_form_natal_map="Ваша натальная карта сформирована!\n\nПожалуйста, подождите еще немного. После анализа вашей натальной карты будет составлен ваш первый персональный гороскоп."
after_sending_horo="<b>Отлично, ваш первый персональный гороскоп уже у вас!</b>\n\nСледующий гороскоп будет сформирован и отправлен в выбранный вами промежуток: утром или вечером.\n\nЕсли при вводе данных была допущена ошибка, то пожалуйста, пришлите актуальную информацию на @AstroBot_support."
def last_message(Des_time_ID):
#     if Des_time_ID==1:
#         return('''
#     ✅ В 13.30 по московскому времени вы получишь первую статью о том, какое астрологическое явление сегодня оказывает максимальное влияние на людей, и как сложится день, исходя из этого.

# ✅ А в 9.30 ты узнаешь расшифровку натальных карт знаменитостей и их совместимость!

# 📌 Чтобы точно не пропустить эти посты и свой следующий гороскоп, закрепи "Астробот" в  телеграмме ''')
#     else:
#         return('''В 13.30 по московскому времени ты получишь первую статью о том, какое астрологическое явление сегодня оказывает максимальное влияние на людей, и как сложится день, исходя из этого.

    return('''✅ А в 18.30  ты узнаешь расшифровку натальных карт знаменитостей и их совместимость!

📌 Чтобы точно не пропустить эти посты и свой следующий гороскоп, закрепи "Астробот" в  телеграмме ''')
if_horo_sended="Ваш гороскоп уже был сформирован и отправлен. Отправляем его повторно!"
if_not_horo_sended="Идет формирование вашего гороскопа, подождите некоторое время"
change_data='Если вы хотите изменить данные, то, пожалуйста, напишите в свободной форме и отправьте на @AstroBot_support, что нужно поменять. Например, "Я ошиблась при вводе имени, пожалуйста, исправьте на Татьяна"'
support='''Чтобы связаться с нами, отправьте сообщение в аккаунт @AstroBot_support.

Вы можете задать любые вопросы как по функционалу бота, так и вопросы, касающиеся собственных астрологических прогнозов!

Мы ответим на ваш вопрос в течение 24 часов!

Если у вас возникла ошибка в работе бота, то, пожалуйста, отправьте скриншот или описание проблемы.
'''

before_first_horo='''Пока мы рассчитываем ваш первый гороскоп, коротко расскажем, из чего он состоит.

Общий гороскоп дня. Одинаков для всех наших пользователей описывает основные взаимодействия светил в этот день и составлен одним из лучших астрологов России. Для расчета звездной карты используется широта и долгота Москвы.

Ваш персональный гороскоп рассчитывается каждый день индивидуально для вас на основе программы, разработанной нашей командой астрологов. Он состоит из 4 разделов:

🎯🎯🎯 – возможности, которые открываются в этот день

❤️❤️❤️ – прогноз по отношениям с самыми близкими людьми

🍔🥑😊 – советы по правильному питанию

💰💰💰– работа, деньги.

Приятного использования! 🌸🌸🌸
Ваш Астробот.'''
commands=["/subscribe", "/send", "/feedback","/manager_access","/gen_user_mes"]
friend_block_start='''Вы можете получить гороскоп для друга, нужно ответить на несколько вопросов о нем.\n
После этого Астробот сформирует персональный гороскоп вашего друга, которым можно будет поделиться с ним.\n
Первый вопрос - как зовут вашего друга?'''
friend_block_insert_gender='''Отлично. Теперь, пожалуйста, введите его пол одной буквой - женский (Ж) или мужской (М).'''
friend_block_insert_Birthday='''Теперь введите дату его рождения.

Пожалуйста, пришлите ее в формате: дд.мм.гггг, например: 29.11.1985'''
friend_block_final_message='''Персональный гороскоп вашего друга на сегодня сформирован, ему будет интересно узнать свой гороскоп - поделитесь!

Если ваш друг в будущем захочет получать еще более точный персональный гороскоп, при регистрации ему надо будет ввести еще и время своего рождения.

'''
server_url="192.168.7.199"
port="443"
err_mess="Данные заполнены некорректно. Пожалуйста, введите их точно, как написано в предыдущем сообщении."

days_for_mailing=[3,0,1]

def form_notification(id):
    end_date=str(select_all_active_until_table(id)["active_until"])
    mes='Спасибо, что пользуетесь Астроботом.\n\nВ данный момент у вас активна подписка. Она действует до  '+end_date+'\n\nВы можете прямо сейчас продлить подписку.\n\nВ таком случае оставшееся время пробного периода суммируется с временем подписки.\n\nЕсли вы хотите отказаться от подписки, то нажмите на соответствующую кнопку.\n\nОбратите внимание, что при отказе от подписки функции бота отключаются и денежные средства, оставшиеся до окончания подписки, не возвращаются.'
    return mes

thanks_for_payment="Спасибо за ваш платеж, вы успешно оформили подписку"



friend_horo_text="! \n\nЯ пользуюсь астрологическим ботом, он составляет мне персональный гороскоп на каждый день с учетом натальной карты. \n\nЯ сформировала в нем гороскоп для тебя, но только я не помню время твоего рождения, поэтому гороскоп может быть неточным!\n\nМожешь перейти в бота и ввести все данные, чтобы получить точный персональный гороскоп.\n\n_________________________________\n\n"
def sub_type1_text(id):

    end_time=str(select_all_active_until_table(id)["days_till_end"]+1)
    return 'Спасибо, что пользуетесь Астроботом.\n\nВ данный момент у вас действует пробный период, подписки. Для вас доступны все функции бота!\n\nДо конца пробного периода осталось еще ' +str(end_time)+' дней.\n\nВы можете прямо сейчас активировать платную подписку.\n\nВ таком случае оставшееся время пробного периода суммируется с временем подписки.'
def sub_type3_text(id):
    
    end_date = str(select_all_active_until_table(id)["active_until"])
    return 'Спасибо, что пользуетесь Астроботом.\n\nВ данный момент у вас активна подписка. Она действует до  '+end_date +'\n\nВы можете прямо сейчас продлить подписку.\n\nВ таком случае оставшееся время пробного периода суммируется с временем подписки.\n\nЕсли вы хотите отказаться от подписки, то нажмите на соответствующую кнопку.\n\nОбратите внимание, что при отказе от подписки функции бота отключаются и денежные средства, оставшиеся до окончания подписки, не возвращаются.'
def sub_type4_text(id=None):
    return 'Ваша подписка в данный момент неактивна. Вы можете в любой момент активировать ее заново.'
offert='''<a href="https://docs.google.com/document/d/1jwpcUW2Dj2nPr7M_gsBoXmwuXYiGoyk5o6o5WVOebDI/edit?usp=sharing">Соглашение на обработку персональных данных</a>

<a href="https://docs.google.com/document/d/1e2BED-8saLTsVIc0_fyMMKn8i5xnqwcF_k9oY_BHkJw/edit)">Соглашение на обработку рекуррентных платежей.</a>

<a href="https://docs.google.com/document/d/1zGaul1srvBDIy1OnaoggKnXfmtDrP5UOSyKSjHYRLVU"> Оферта оказания услуг</a> '''

#CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'password';

