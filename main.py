import telebot
from telebot import types

from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import choices

import figurestophoto as fp

import requests
import socket
import threading
import smtplib as root

print('Bot succefull runned.')
bot = telebot.TeleBot('1111001859:AAGYy4uSLgGCFcnkqcKyBOY4OEDRsOjxMI0')
post = "https://nekobin.com/api/documents"
SYMBOLS = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"


@bot.message_handler(commands=['commands'])
def start(message):

    msg = "💰            » <b>Список доступных команд:</b>\n<code>Бот создан в ознакомительных целях, прошу не использовать его во вред.</code>\n\n     » На данный момент функции бота доступны <b>всем</b> без групп и ограничений.\n\n"
    hcommands = "   🎗» <u>Hacks and Checks Utils</u>\n1. » <b>/send_mail</b> (ваша почта) (пароль) (кому) - Отправление спам-писем на указанную почту. (Ваша почта должна быть от mail.ru)\n2. » <b>/gen_pass</b> - Генератор рандомного сложного пароля\n"
    hcommands1 = "3. » <b>/dos</b> (ip) - Не очень сильная DoS атака для теста\n4. » <b>/scan_port</b> (ip) (до какого порта) - Скан-портов на открытые у указанного IP.#\n5. » <b>/parser</b> - Парсер сайтов HTML кода.\n"
    hcommands2 = "6. » <b>/checkip</b> (ip) - Полная информация о человеке по его IP\n7. » <b>/checkph</b> (phone) - Полная информация о человеке с его неточным местом нахождением."
    hcommands3 = "\n8. » <b>/ping</b> (site) - Чекер качества коннектов сайта\n\n"
    autils = "   🎗<u>Other Utils</u> »\n9. » <b>/nekobin</b> - Выгрузка текста на текстовый сайт для более удобного взаимодействия.\n10. » <b>/textimage</b> - Преобразование текста в картинку.\n\n"
    games = "   🎗<u>Mini-games</u> »\n 11. » <b>.П или Д</b> - Правда или Действие\n 12. » <b>.КНБ</b> - Камень, ножница, бумага"
    about = "\n\n   🎗<u>About</u> »\n Inst: @thestrikem\n Steam: Strike_777\n Vk: @thestrikem\n GitHub: @thestrikem\n\n@strikemtestbot"

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Чек IP', 'Чек Номер', 'Некобин', 'Сканнер Портов', 'Спамер почты', 'Генератор паролей')

    bot.send_message(message.chat.id, f"{msg} {hcommands} {hcommands1} {hcommands2} {hcommands3} {autils} {games} {about}", parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['nekobin'])
def start(message):
    text = '💰 » Итак, введите <b>текст</b>, который хотите обратить в текстовый сайт nekobin.com'
    bot.register_next_step_handler(bot.send_message(message.chat.id, text, parse_mode='html'), text_a)

def text_a(message):
    msg = message.text
    paste = requests.post(post, data={"content": msg})
    paste.raise_for_status()
    result = f"✅ » <b>Ваш текст успешно загружен!</b>\n\n» Ссылка на текст: https://nekobin.com/{paste.json()['result']['key']}\n\n@strikemtestbot"
    bot.send_message(message.chat.id, result, parse_mode='html')

@bot.message_handler(commands=['ip'])
def start(message):
    args = message.text.split(" ")
    ip = args[1]
    ips = socket.gethostbyname(f"{ip}")
    bot.send_message(message.chat.id, f"Айпи: {ips}")

@bot.message_handler(commands=['ping']) #НЕ РАБОТАЕТ
def start(message):
    try:
        args = message.text.split(" ")
        get_ping = args[1]

        def info():
            response = requests.get(f'https://check-host.net/check-ping?host={get_ping}&max_nodes=5')

            check_id = response.json()['request_id']

            responselast = requests.get(f'https://check-host.net/check-result/{check_id}')

            result = response.json()

            global resultate
            resultate = f"Результат: {result}"

            bot.send_message(message.chat.id, resultate)

        def main():
            info()

        main()

    except Exception as e:
        print(e)

@bot.message_handler(commands=['gen_pass'])
def start(message):
    try:
        args = message.text.split(" ")
        lenght = int(args[1])
        id1 = message.chat.id

        if lenght >= 101: bot.send_message(id1, 'Зачем тебе такой пароль, неее')

        else:
            password = ''.join(choices(SYMBOLS, k=lenght))
            result = f"✅ » Результат: <b>{password}</b>\n» Кол-во символов: <b>{lenght}</b>\n\n@strikemtestbot"
            bot.send_message(message.chat.id, result, parse_mode='html')

    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Ошибка')

@bot.message_handler(commands=['send_mail'])
def start(message):
    try:
        args = message.text.split(" ")
        L = args[1]
        P = args[2]
        U = args[3]
        To = args[4]
        T = args[5].replace('+', ' ')
        M = args[6].replace('+', ' ')
        N = args[7]

        for value in range(int(N)):
            msg = MIMEMultipart()

            msg['Subject'] = T
            msg['From'] = L
            body = M
            msg.attach(MIMEText(body, 'plain'))

            server = root.SMTP_SSL(U, 465)
            server.login(L, P)
            server.sendmail(L, To, msg.as_string())
            server.quit()

            value += 1

        inet = f"✅ » Почте <b>{To}</b> успешно отправлено <b>{N}</b>, от <b>{L}</b>"
        bot.send_message(message.chat.id, inet, parse_mode='html')
    except Exception as e:
        print(e)


@bot.message_handler(commands=['checkip'])
def start(message):
    try:
        args = message.text.split(" ")
        get_ip = args[1]

        def info():
            response = requests.get(f'http://ipinfo.io/{get_ip}/json')

            user_ip = response.json()['ip']
            user_city = response.json()['city']
            user_region = response.json()['region']
            user_country = response.json()['country']
            user_location = response.json()['loc']
            #user_org = response.json()['org']
            user_timezone = response.json()['timezone']

            global all_info
            all_info = f"✅ » Информация по IP <b>{user_ip}</b>:\n\n» Город: <b>{user_city}</b>\n» Регион: <b>{user_region}</b>\n» Страна: <b>{user_country}</b>\n» Локация: <b>{user_location}</b>\n» Временный пояс: <b>{user_timezone}</b>\n\n@strikemtestbot"

            bot.send_message(message.chat.id, all_info, parse_mode='html')

        def main():
            info()

        main()
    except Exception as e:
        print(e)

@bot.message_handler(commands=['checkph'])
def start(message):
    try:
        args = message.text.split(" ")
        get_phone = args[1]

        def info():
            response = requests.get(f'https://htmlweb.ru/geo/api.php?json&telcod={get_phone}')

            user_country = response.json()['country']['english']
            user_namec = response.json()['country']['name']
            user_fullnamec = response.json()['country']['fullname']
            user_code = response.json()['country']['country_code3']
            user_iso = response.json()['country']['iso']
            user_telecod = response.json()['country']['telcod']
            user_lang = response.json()['country']['lang']
            user_id = response.json()['country']['id']
            user_location = response.json()['country']['location']
            user_city = response.json()['capital']['name']
            user_area = response.json()['capital']['area']
            user_tt = response.json()['capital']['telcod']
            user_width = response.json()['capital']['latitude']
            user_lenth = response.json()['capital']['longitude']
            user_timez = response.json()['time_zone']
            user_imgf = response.json()['ImgFlag']
            user_post = response.json()['capital']['post']
            user_oper = response.json()['0']['oper']
            user_idoper = response.json()['0']['oper_id']
            user_fulloper = response.json()['0']['oper_brand']
            user_def = response.json()['0']['def']

            if user_id == "UZ":
                global all_info1
                global capitalin
                global info0
                all_info1 = f"✅ » <u>Информация по текущему узбекскому номеру: (@thestrikem)</u>\n<code>     {get_phone}</code>\n\n     <b>🇺🇿 Страна номера:</b>\n» Страна: {user_namec}\n» Полное название: {user_fullnamec}\n» Язык: {user_lang}\n» ID: {user_id}\n» Код: {user_code}\n» ISO: {user_iso}\n» Телекод: {user_telecod}\n\n     <b>🇺🇿 Город номера:</b>\n"
                capitalin = f"» Город: {user_city}\n» Телекод Города: {user_tt}\n» Area: {user_area}\n» Широта: {user_width}\n» Долгота: {user_lenth}\n» Временная зона: {user_timez}\n» Пост: {user_post}\n"
                info0 = f"\n     <b>🇺🇿 Оператор:</b>\n» Главный оператор: {user_oper}\n» Передавающий оператор: {user_fulloper}\n» ID Оператора: {user_idoper}\n» Def: {user_def}\n\n@strikemtestbot"

                photo = open('uz.jpg', 'rb')

                bot.send_message(message.chat.id, f"{all_info1} {capitalin} {info0}", parse_mode='html')
                bot.send_photo(message.chat.id, photo)

            if user_id == "RU":
                all_info1 = f"✅ » <u>Информация по текущему русскому номеру: (@thestrikem)</u>\n<code>     {get_phone}</code>\n\n     <b>🇷🇺 Страна номера:</b>\n» Страна: {user_namec}\n» Полное название: {user_fullnamec}\n» Язык: {user_lang}\n» ID: {user_id}\n» Код: {user_code}\n» ISO: {user_iso}\n» Телекод: {user_telecod}\n\n     <b>🇷🇺 Город номера:</b>\n"
                capitalin = f"» Город: {user_city}\n» Телекод Города: {user_tt}\n» Area: {user_area}\n» Широта: {user_width}\n» Долгота: {user_lenth}\n» Временная зона: {user_timez}\n» Пост: {user_post}\n"
                info0 = f"\n     <b>🇷🇺 Оператор:</b>\n» Главный оператор: {user_oper}\n» Передавающий оператор: {user_fulloper}\n» ID Оператора: {user_idoper}\n» Def: {user_def}\n\n@strikemtestbot"

                photo1 = open('ru.jpg', 'rb')

                bot.send_message(message.chat.id, f"{all_info1} {capitalin} {info0}", parse_mode='html')
                bot.send_photo(message.chat.id, photo1)

        def main():
            info()

        main()
    except Exception as e:
        print(e)

@bot.message_handler(commands=['g'])
def start(message):
    msg = bot.send_message(message.chat.id, '✅ » Окей, что будем искать?')
    bot.register_next_step_handler(msg, next_event)

def next_event(message):
    text = message.text
    url = f'https://www.google.com/search?b-d&q=' + str(text).replace(' ', '+')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

    def parser(question, url, headers):
        r = requests.get(url, headers = headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        items = soup.findAll('div', class_ = "rc")

        comps = []

        for item in items:
            comps.append({
                'link': item.find('a').get('href'),
                'title': item.find('h3', class_ = 'LC20lb DKV0Md').get_text(strip = True)
            })

        for comp in comps:
            bot.send_message(message.chat.id, str('✅ » Найдено: ') +comp['title'] + ' -- ' + comp['link'])

    parser(text, url, headers)

@bot.message_handler(commands=['scan_port'])
def start(message):
    args = message.text.split(" ")
    ips = args[1]
    ports = int(args[2])
    bot.send_message(message.chat.id, '✅ » Идет поиск открытых портов...\n» Если все порты будуте закрыты, ничего не напишет.')
    try:
        def scan_port(ip, port):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if client.connect_ex((ip, port)):
                print(f"порт : {port} окозался закрытым для айпи : {ip}")
            else:
                bot.send_message(message.chat.id, f"✅ » Обнаружен открытый порт: <b>{port}</b> от айпи адреса: <b>{ip}</b>", parse_mode='html')
                print(f"открытый порт : {port} от айпи адреса : {ip} ")

        ip = socket.gethostbyname(f"{ips}")

        def scan_por():
            scan_port(ip, i)

        for i in range(ports):
            threading.Thread(target=scan_por).start()
    except Exception as e:
        print(e)

@bot.message_handler(content_types=['text'])
def start(message):
    text = message.text
    id = message.chat.id
    if text == 'Чек IP':
        bot.send_message(id, "💰 » Использование: <b>/checkip (айпи)</b>\n» Чтобы узнать IP сайта используйте - /ip (ссылка)", parse_mode='html')

    if text == 'Чек Номер':
        bot.send_message(id, "💰 » Использование: <b>/checkph (номер)</b>", parse_mode='html')

    if text == 'Некобин':
        bot.send_message(id, "💰 » Использование: <b>/nekobin</b>\n» Далее просто вводите текст.", parse_mode='html')

    if text == 'Сканнер Портов':
        bot.send_message(id, "💰 » Использование: <b>/scan_port (айпи) (до какого порта)</b>\n» Работает в тестовом режиме.", parse_mode='html')

    if text == 'Спамер почты':
        msg = "» Примечания: Ваша почта должна быть от mail.ru (временное ограничение), smtp.mail.ru необходимо указывать и не менять, в теме сообщения и сообщении вместо пробелов необходимо использовать знак '+', рекомендуемое кол-во писем за раз: 15."
        bot.send_message(id, f"💰 » Использование: <b>/send_mail ваша_почта пароль_почты smtp.mail.ru почта_получателя тема_сообщения сообщение кол-во_писем</b>\n{msg}", parse_mode='html')

    if text == 'Генератор паролей':
        bot.send_message(id, f"💰 » Использование: <b>/gen_pass кол-во_символов в пароле")


bot.polling(none_stop=True)